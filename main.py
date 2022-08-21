import requests
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py
from log_config import init_loggers
from prometheus_client import Counter

from prometheus_client import start_http_server, Summary
import random
import time

# Initiate logger messages 
logger = init_loggers()

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Initiate App
app = FastAPI()


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


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


# Start up the server to expose the metrics.
start_http_server(3000)
# Generate some requests.
while True:
    process_request(random.random())