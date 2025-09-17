from pydantic import BaseModel

class Badge(BaseModel):
    name: str
    description: str
    category: str
