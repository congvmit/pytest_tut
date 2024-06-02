from pydantic import BaseModel


# Schema
class CreateItem(BaseModel):
    name: str
    description: str = None
    price: float
