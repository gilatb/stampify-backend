from enum import Enum, auto


class UserRole(str, Enum):
    ADMIN = auto()
    BUSINESS = auto()
    CUSTOMER = auto()
    USER = auto()


class CardStatus(str, Enum):
    CREATED = 'created'
    ACTIVE = 'active'
    PROMOTION_PENDING = 'promotion_pending'
    PROMOTION_APPLIED = 'promotion_applied'


class Feature(str, Enum):
    BASIC_CARDS = 'basic_cards'
