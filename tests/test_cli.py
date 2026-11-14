import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from repolens.cli import app, write_report
from repolens.sources import RepoLensError

runner = CliRunner()


def test_version_and_help():
    assert "0.1.0" in runner.invoke(app, ["version"]).stdout
    assert runner.invoke(app, ["analyze", "--help"]).exit_code == 0


def test_offline_cli_json(tmp_path):
    root = tmp_path / "repo with spaces"
    root.mkdir()
    (root / "main.py").write_text("def main(): pass\n", encoding="utf-8")
    result = runner.invoke(app, ["analyze", str(root), "--local", "--format", "json"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.stdout)
    assert data["file_count"] == 1
    assert data["modules"][0]["symbols"][0]["name"] == "main"
    assert "已扫描" in result.stderr


def test_output_does_not_overwrite(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    output = tmp_path / "report.md"
    output.write_text("keep me", encoding="utf-8")
    result = runner.invoke(app, ["analyze", str(root), "-o", str(output)])
    assert result.exit_code == 1
    assert output.read_text() == "keep me"
    result = runner.invoke(app, ["analyze", str(root), "-o", str(output), "--force"])
    assert result.exit_code == 0
    assert "RepoLens" in output.read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "args", [["--format", "xml"], ["--max-files", "0"], ["--timeout", "0"], ["--max-requests", "2"]]
)
def test_invalid_arguments(args):
    assert runner.invoke(app, ["analyze", ".", *args]).exit_code == 2


def test_ref_rejected_for_local(tmp_path):
    result = runner.invoke(app, ["analyze", str(tmp_path), "--ref", "main"])
    assert result.exit_code == 1 and "--ref" in result.stderr


def test_write_atomic_cleanup_and_no_overwrite(tmp_path):
    output = tmp_path / "nested" / "report.md"
    write_report(output, "hello", False)
    assert output.read_text() == "hello"
    with pytest.raises(RepoLensError):
        write_report(output, "overwrite", False)
    assert sorted(p.name for p in output.parent.iterdir()) == ["report.md"]


def test_demo_fixture_end_to_end(tmp_path):
    demo = Path(__file__).resolve().parents[1] / "examples" / "demo_repo"
    output = tmp_path / "demo.md"
    result = runner.invoke(app, ["analyze", str(demo), "--local", "-o", str(output)])
    assert result.exit_code == 0, result.output
    text = output.read_text(encoding="utf-8")
    assert "tiny-tasks" in text
    assert "Task" in text
