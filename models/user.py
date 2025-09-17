from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: str
    name: str
    email: str
    eco_points: int = 0
    streak: int = 0
    badges: List[str] = []
