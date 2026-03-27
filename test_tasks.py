from tasks.task_definition import TASKS

for name, task in TASKS.items():
    print(f"\n{name.upper()} TASK:")
    print(task["code"])