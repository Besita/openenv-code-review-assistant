from envs.code_review_env import CodeReviewEnv
from models.schema import Action

env = CodeReviewEnv()

# Start environment
obs = env.reset("easy")
print("Observation:", obs)

# Dummy action
action = Action(
    issues=["division by zero"],
    severity="high",
    suggestion="Add if b == 0 check",
    reasoning="division by zero causes runtime error"
)


obs, reward, done, _ = env.step(action)

print("Reward:", reward)
print("Done:", done)