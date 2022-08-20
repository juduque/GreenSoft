from typing import Union
import requests
from fastapi import FastAPI, Response, status

app = FastAPI()
url = 'https://62fd7b30b9e38585cd52637e.mockapi.io/udem/taller2/'

@app.get("/authUsers/{internalId}", status_code=200)
def get_auth_users(internalId: str, response: Response):
    consult = requests.get(url + 'infoUsers/?internalId=' + internalId, {}, timeout=5)
    data = consult.json()
    if len(data) != 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    internalId = data[0]["encryptedToken"]
    response = { "internalId": internalId, "encryptedToken": encryptedToken }
    return response