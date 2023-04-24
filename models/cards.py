from pydantic import BaseModel

from utils.enums import CardStatus


class CardTemplate(BaseModel):
    _id: int
    business_id: int
    stamps_required: int
    promotion: str


class Card(BaseModel):
    _id: int
    card_template_id: int
    customer_id: int
    stamp_count: int
    status: CardStatus


class CardsResponse(BaseModel):
    user_id: int
    cards: list[Card]
