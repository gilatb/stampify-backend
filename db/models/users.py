
from sqlalchemy import Boolean, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.connection import Base
from utils.enums import UserRole


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    user_role: Mapped[UserRole] = mapped_column(Enum(
        UserRole,
        name='user_role',
        values_callable=lambda enum: [enum_row.value for enum_row in enum]),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    __mapper_args__ = {
        'polymorphic_on': user_role,
        'polymorphic_identity': UserRole.USER
    }


class Customer(User):
    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }
    cards = relationship("Card", back_populates="customer")


class Business(User):
    __mapper_args__ = {
        'polymorphic_identity': 'business'
    }
    cards_templates = relationship("CardTemplate", back_populates="business")
    cards = relationship("Card", back_populates="business")


class Admin(User):
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
