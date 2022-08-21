import requests
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py
from log_config import init_loggers

# Initiate logger messages 
logger = init_loggers()


# Initiate App
app = FastAPI()


logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warn message')
logger.error('Error message')
logger.critical('Critical message')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/")
def read_root():
    url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
