from pydantic import BaseModel

from utils.enums import Feature, UserRole


class User(BaseModel):
    _id: int
    email: str
    role: UserRole
    is_active: bool


class Business(User):
    features: list[Feature] = []


class Customer(User):
    card_ids: list[int]
