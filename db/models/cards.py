from sqlalchemy import Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.connection import Base
from utils.enums import CardStatus


class CardTemplate(Base):
    __tablename__ = "card_templates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, index=True)

    business = relationship("Business", back_populates="cards_templates")


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    stamp_count: int
    status: Mapped[CardStatus] = mapped_column(Enum(
        CardStatus,
        name='status',
        values_callable=lambda enum: [enum_row.value for enum_row in enum]),
        nullable=False,
    )

    card_template = relationship("CardTemplate", back_populates="cards")
    customer = relationship("Customer", back_populates="cards")
    business = relationship("Business", back_populates="cards")
