import requests
import random
from pydantic import BaseModel  # adicionar en los imports en el main.py
from info_users import handler as info
from auth_users import handler as auth
from role_users import handler as role
from fastapi import FastAPI, Response, status
from prometheus_client import start_http_server
from prometheus_metrics import process_request, counter, latency

# Print metrics y/n
METRICS = True

# Star App
app = FastAPI()
url = 'https://62fd7b30b9e38585cd52637e.mockapi.io/udem/taller2/'


# Start metrics
process_request(random.random())
counter()
latency()


# from .auth_users import handler as auth
app.include_router(info.router)
app.include_router(auth.router)
app.include_router(role.router)


# Star localhost metrics
if METRICS:
    start_http_server(3000)
