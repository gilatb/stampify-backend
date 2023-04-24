import uvicorn
from fastapi import FastAPI
from starlette import status

from config import settings
from models.cards import CardsResponse

app = FastAPI()


@app.get("/{customer_id}/cards", status_code=status.HTTP_200_OK)
def get_customer_cards(customer_id: int):
    return CardsResponse(user_id=customer_id, cards=[])


@app.post("/{customer_id}/cards", status_code=status.HTTP_201_CREATED)
def create_customer_cards(customer_id: int):
    pass


@app.put("/{customer_id}/cards/{card_id}")
def update_customer_cards(customer_id: int, card_id: int):
    pass


@app.get("/{business_id}/card_templates")
def get_business_card_templates(business_id: int):
    pass


if __name__ == '__main__':
    uvicorn.run(
        'web:app',
        reload=settings.autoreload,
        host=settings.service_host,
        port=settings.service_port,
        log_level=settings.log_level.lower(),
    )
