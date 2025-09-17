from pydantic import BaseModel

class Product(BaseModel):
    name: str
    brand: str
    category: str
    eco_alternatives: list[str] = []
