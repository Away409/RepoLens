from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


def completed(tasks: list[Task]) -> int:
    return sum(task.done for task in tasks)
