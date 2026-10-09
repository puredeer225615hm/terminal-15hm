"""Tiny terminal task manager with JSON persistence."""
import json
import os
import sys

FILE = "tasks.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)


def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show(tasks):
    if not tasks:
        print("No tasks.")
    for i, t in enumerate(tasks, 1):
        print(f"{i:>3}. [{'x' if t['done'] else ' '}] {t['text']}")


def main(argv):
    tasks = load()
    cmd = argv[0] if argv else "list"
    if cmd == "list":
        show(tasks)
    elif cmd == "add":
        tasks.append({"text": " ".join(argv[1:]), "done": False})
        save(tasks)
        show(tasks)
    elif cmd == "done":
        tasks[int(argv[1]) - 1]["done"] = True
        save(tasks)
        show(tasks)
    elif cmd == "rm":
        del tasks[int(argv[1]) - 1]
        save(tasks)
        show(tasks)
    else:
        print("usage: tasks [list | add TEXT | done N | rm N]")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))