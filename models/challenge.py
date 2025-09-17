from pydantic import BaseModel
from typing import List

class Challenge(BaseModel):
    name: str
    participants: List[str]
    status: str
    reward_points: int
