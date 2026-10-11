"""Terminal Task Manager: add, list, mark done, remove tasks."""
import argparse, sys

tasks = []

def add_task(desc):
    tasks.append({'id': len(tasks)+1, 'desc': desc, 'done': False})

def list_tasks():
    for t in tasks:
        status = '✓' if t['done'] else '✗'
        print(f"{t['id']}. [{status}] {t['desc']}")

def done_task(tid):
    for t in tasks:
        if t['id'] == tid:
            t['done'] = True
            return
    print(f"No task with id {tid}")

def remove_task(tid):
    global tasks
    tasks = [t for t in tasks if t['id'] != tid]

def main():
    parser = argparse.ArgumentParser(prog='taskmanager')
    sub = parser.add_subparsers(dest='cmd')
    sub.add_parser('list')
    add_sub = sub.add_parser('add')
    add_sub.add_argument('desc', nargs='+')
    done_sub = sub.add_parser('done')
    done_sub.add_argument('id', type=int)
    rem_sub = sub.add_parser('remove')
    rem_sub.add_argument('id', type=int)
    if len(sys.argv)==1:
        parser.print_help()
        return
    args = parser.parse_args()
    if args.cmd=='add':
        add_task(' '.join(args.desc))
    elif args.cmd=='list':
        list_tasks()
    elif args.cmd=='done':
        done_task