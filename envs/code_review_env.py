from models.schema import Observation, Action, Reward
from tasks.task_definition import TASKS
from grader.code_grader import grade


class CodeReviewEnv:

    def __init__(self):
        self.current_task = None
        self.task_id = None
        self.history = []

    # 🔹 Reset environment
    def reset(self, task_id="easy"):
        self.task_id = task_id
        self.current_task = TASKS[task_id]
        self.history = []

        return Observation(
            code=self.current_task["code"],
            task_id=task_id
        )

    # 🔹 Step function (core logic)
    def step(self, action: Action):
        score = grade(self.current_task, action)

        reward = Reward(
            score=score,
            feedback=f"Score: {score}"
        )

        self.history.append(action)

        done = True  # one-step task

        return (
            Observation(
                code=self.current_task["code"],
                task_id=self.task_id
            ),
            reward,
            done,
            {}
        )

    # 🔹 Return current state
    def state(self):
        return {
            "task_id": self.task_id,
            "history": self.history
        }