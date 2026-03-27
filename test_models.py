from models.schema import Observation, Action, Reward

# Test Observation
obs = Observation(code="x = 10 / 0", task_id="easy")
print("Observation:", obs)

# Test Action
action = Action(
    issues=["division by zero"],
    severity="high",
    suggestion="Add check for zero",
    reasoning="division by zero causes runtime error"
)
print("Action:", action)

# Test Reward
reward = Reward(score=0.8, feedback="Good job")
print("Reward:", reward)