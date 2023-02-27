from enum import Enum


class UserRole(str, Enum):
    ADMIN = 'admin'
    BUSINESS = 'business'
    CUSTOMER = 'customer'


class CardStatus(str, Enum):
    CREATED = 'created'
    ACTIVE = 'active'
    PROMOTION_PENDING = 'promotion_pending'
    PROMOTION_APPLIED = 'promotion_applied'


class Feature(str, Enum):
    BASIC_CARDS = 'basic_cards'
