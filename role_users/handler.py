import requests
from fastapi import Response, status, APIRouter
from pydantic import BaseModel
from typing import Union
from log_config import init_loggers

logger = init_loggers()

prefix = "roleUsers"
router = APIRouter(prefix="/"+prefix,)
url = 'https://62fd7b30b9e38585cd52637e.mockapi.io/udem/taller2/'

class IData(BaseModel):
    role: Union[str, None] = None
    expirationDate: Union[str, None] = None
    username: Union[str, None] = None

def checkIsEmpty(data):
    valueData = list(data.values()) #list of values 
    existData = any(elem is not None for elem in valueData) #exist info in role send by user
    if not existData:
        return True

@router.get("", status_code=200)
def get_total_users(response: Response):
    try:
        consult = requests.get(url + prefix, timeout=5)
        data = consult.json()
        logger.info('Info total users in role')
        return {"total": len(data)}
    except:
        logger.error('Error Count users in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_COUNT"}
        
@router.get("/{encryptedToken}", status_code=200)
def get_info_users(encryptedToken: str, response: Response):
    try:
        consult = requests.get(url + prefix + '/?encryptedToken=' + encryptedToken, timeout=5)
        data = consult.json()
        if len(data) == 1:
            logger.info('Info user get in role')
            response = data[0]
            return response
        response.status_code = status.HTTP_204_NO_CONTENT
    except:
        logger.error('Error finding users in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_FINDING_USER"}

@router.post("", status_code=200)
def create_info_users(infoUser: IData, response: Response):
    data = infoUser.dict()
    isEmpty = checkIsEmpty(data)
    if (isEmpty):
        logger.warning('Warn not data to create in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "NOT_DATA_CREATE"}
    try:
        response = requests.post(url + prefix, data, timeout=5)
        if response.status_code == 201:
            logger.info('Info user created in role')
            return { "message": "USER_CREATED", "data": response.json()}
        response.status_code = status.HTTP_404_NOT_FOUND
        logger.error('Error creating users in role in response')
        return { "message": "ERROR_CREATING_USER"}
    except:
        logger.error('Error creating users in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_CREATING_USER"}

@router.delete("/{encryptedToken}", status_code=200)
def delete_info_users(encryptedToken: str, response: Response):
    try:
        consult = requests.delete(url + prefix + '/' + encryptedToken)
        data = consult.json()
        if type(data) is dict: 
            logger.info('Info user deleted in role')
            return { "message": "USER_DELETED"}
        logger.warning('Warn user not found to delete')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "USER_NOT_FOUND"}
    except:
        logger.error('Error finding users to delete in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_FINDING_USER"}

@router.put("/{encryptedToken}", status_code=200)
def update_info_users(encryptedToken: str, infoUser: IData, response: Response):
    data = infoUser.dict() #data in json format
    isEmpty = checkIsEmpty(data)
    if (isEmpty):
        response.status_code = status.HTTP_404_NOT_FOUND
        logger.warning('Warn data not exist to update in role')
        return { "message": "NOT_DATA_UPDATE"}
    try:
        consult = requests.put(url + prefix + '/' + encryptedToken, data)
        if consult.status_code == 200:
            logger.info('Info user update in role')
            return { "message": "USER_UPDATED"}
        logger.warning('Warn user not exist to update in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "USER_NOT_EXIST"}
    except:
        logger.error('Error updating users in role')
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_UPDATING_USER"}