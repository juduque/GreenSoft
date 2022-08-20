import requests
from fastapi import FastAPI, Response, status

from pydantic import BaseModel # adicionar en los imports en el main.py

app = FastAPI()
url = 'https://62fd7b30b9e38585cd52637e.mockapi.io/udem/taller2/'

#from .auth_users import handler as auth
from info_users import handler as info

app.include_router(info.router)
