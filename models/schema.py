from pydantic import BaseModel
from typing import List


# What the agent sees
class Observation(BaseModel):
    code: str
    task_id: str


# What the agent returns
class Action(BaseModel):
    issues: List[str]
    severity: str
    suggestion: str
    reasoning: str


# How we score the agent
class Reward(BaseModel):
    score: float
    feedback: str