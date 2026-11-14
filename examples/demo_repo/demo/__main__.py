from .tasks import Task, completed


def main():
    tasks = [Task("Read README", True), Task("Inspect source")]
    print(f"Completed: {completed(tasks)}/{len(tasks)}")


if __name__ == "__main__":
    main()
