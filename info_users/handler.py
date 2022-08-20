import requests
from fastapi import Response, status, APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/infoUsers",)

url = 'https://62fd7b30b9e38585cd52637e.mockapi.io/udem/taller2/'


class Info(BaseModel):
    idUsuario: str

class Update(BaseModel):
    internalId: str
    idUsuario: str
    name: str

@router.get("/{idUsuario}", status_code=200)
def get_info_users(idUsuario: str, response: Response):
    consult = requests.get(url + 'infoUsers/?idUsuario=' + idUsuario, {}, timeout=5)
    data = consult.json()
    if len(data) != 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    response = data[0]
    return response

@router.post("")
def create_info_users(infoUser: Info):
    requests.post(url + 'infoUsers', {"idUsuario": infoUser.idUsuario}, timeout=5)
    return { "message": "user_created"}

@router.delete("/{idUsuario}", status_code=200)
def delete_info_users(idUsuario: str, response: Response):
    consult = requests.delete(url + 'infoUsers/' + idUsuario, timeout=5)
    data = consult.json() 
    if type(data) is dict: 
        return { "message": "USER_DELETED"}
    response.status_code = status.HTTP_404_NOT_FOUND
    return { "message": "USER_NOT_FOUND"}

@router.put("")
def update_info_users(infoUser:Update):
    body = {}
    for attr, value in vars(infoUser).items():
        if attr != "internalId":
            body[attr] = value
    consult = requests.put(url + 'infoUsers/' + infoUser.internalId, body, timeout=5)
    return { "message": "USER_UPDATED"}

