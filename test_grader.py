from grader.code_grader import grade
from tasks.task_definition import TASKS
from models.schema import Action

task = TASKS["easy"]

action = Action(
    issues=["division by zero"],
    severity="high",
    suggestion="Add check if b == 0",
    reasoning="This causes runtime error"
)

score = grade(task, action)

print("Score:", score)