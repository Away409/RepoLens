import json

import httpx
import pytest
from typer.testing import CliRunner

from repolens.cli import app

runner = CliRunner()


@pytest.fixture
def report(tmp_path):
    repo = tmp_path / "sample"
    repo.mkdir()
    (repo / "main.ts").write_text('export function hello() { return "private-body" }')
    (repo / "README.md").write_text("private-readme")
    path = tmp_path / "report.json"
    result = runner.invoke(app, ["analyze", str(repo), "--format", "json", "-o", str(path)])
    assert result.exit_code == 0
    return path


def mock_api(monkeypatch, handler):
    client = httpx.Client
    monkeypatch.setenv("OPENAI_API_KEY", "mock-key")
    monkeypatch.setattr(
        httpx, "Client", lambda **kw: client(transport=httpx.MockTransport(handler), **kw)
    )


def test_preview_and_overwrite_are_offline(report, monkeypatch):
    mock_api(monkeypatch, lambda _: pytest.fail("unexpected outbound request"))
    out = runner.invoke(app, ["explain", str(report)])
    assert out.exit_code == 0 and "main.ts:1" in out.stdout
    assert "private-readme" not in out.stdout and "private-body" not in out.stdout
    before = report.read_bytes()
    out = runner.invoke(
        app, ["explain", str(report), "--budget-usd", "1", "-o", str(report), "--force"]
    )
    assert out.exit_code == 1 and report.read_bytes() == before


def test_missing_key_and_invalid_input_preserve_existing_notes(report, monkeypatch, tmp_path):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    output = tmp_path / "notes.md"
    output.write_text("existing")
    args = ["explain", str(report), "-o", str(output), "--force", "--budget-usd", "0.01"]
    out = runner.invoke(app, args)
    assert out.exit_code == 1 and "OPENAI_API_KEY" in out.stderr
    report.write_text("{broken")
    out = runner.invoke(app, args)
    assert out.exit_code == 1 and "JSON" in out.stderr
    assert output.read_text() == "existing"


@pytest.mark.parametrize(
    "result", [{"status": "incomplete"}, {"status": "completed", "output": []}]
)
def test_incomplete_or_refused_generation_preserves_existing_notes(
    report, monkeypatch, tmp_path, result
):
    calls = []

    def handler(request):
        calls.append(request.url.path)
        body = {"input_tokens": 20} if len(calls) == 1 else result
        return httpx.Response(200, json=body)

    mock_api(monkeypatch, handler)
    output = tmp_path / "notes.md"
    output.write_text("existing")
    args = ["explain", str(report), "-o", str(output), "--force", "--budget-usd", "0.01"]
    assert runner.invoke(app, args).exit_code == 1
    assert output.read_text() == "existing"
    assert calls == ["/v1/responses/input_tokens", "/v1/responses"]


@pytest.mark.parametrize("budget", ["0", "-1", "NaN", "Infinity", "abc"])
def test_invalid_budgets_stay_offline(report, monkeypatch, budget):
    mock_api(monkeypatch, lambda _: pytest.fail("unexpected outbound request"))
    assert runner.invoke(app, ["explain", str(report), "--budget-usd", budget]).exit_code == 1


def test_partial_budget_never_generates(report, monkeypatch):
    def handler(request):
        assert request.url.path == "/v1/responses/input_tokens"
        return httpx.Response(200, json={"input_tokens": 200})

    mock_api(monkeypatch, handler)
    out = runner.invoke(app, ["explain", str(report), "--budget-usd", "0.00374999999999999999"])
    assert out.exit_code == 1 and "超过预算" in out.stderr


@pytest.mark.parametrize("reference", [1, 200, True])
def test_explanation_must_cite_supplied_evidence(report, monkeypatch, reference):
    counted = {}

    def handler(request):
        data = json.loads(request.content)
        assert request.url.host == "api.openai.com"
        assert request.headers["authorization"] == "Bearer mock-key"
        if request.url.path.endswith("/input_tokens"):
            counted.update(data)
            assert json.loads(data["input"]) == [
                {"id": 1, "path": "main.ts", "line": 1, "detail": "function hello"}
            ]
            return httpx.Response(200, json={"input_tokens": 200})
        assert request.url.path == "/v1/responses"
        assert data == dict(counted, store=False, service_tier="default", max_output_tokens=800)
        notes = {"notes": [{"text": "Read the greeting function.", "evidence_id": reference}]}
        return httpx.Response(
            200,
            json={
                "status": "completed",
                "usage": {"input_tokens": 200, "output_tokens": 100},
                "output": [
                    {
                        "type": "message",
                        "content": [{"type": "output_text", "text": json.dumps(notes)}],
                    }
                ],
            },
        )

    mock_api(monkeypatch, handler)
    out = runner.invoke(app, ["explain", str(report), "--budget-usd", "0.00375"])
    if reference is True or reference == 200:
        assert out.exit_code == 1 and "有效引用" in out.stderr and not out.stdout
    else:
        assert out.exit_code == 0 and "main.ts:1" in out.stdout and "0.0006" in out.stdout


@pytest.mark.parametrize("status", [401, 429, 503])
def test_api_failure_is_not_retried_or_echoed(report, monkeypatch, status):
    calls = []

    def handler(request):
        calls.append(request.url.path)
        return httpx.Response(status, json={"error": "private-error"})

    mock_api(monkeypatch, handler)
    out = runner.invoke(app, ["explain", str(report), "--budget-usd", "1"])
    assert out.exit_code == 1 and str(status) in out.stderr and "private-error" not in out.stderr
    assert calls == ["/v1/responses/input_tokens"]
