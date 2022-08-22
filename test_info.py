import pytest
from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_post_info_NOT_DATA_CREATE():
    data = {}
    response = client.post(
        '/infoUsers',
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] == "NOT_DATA_CREATE"

def test_post_info_DATA_INCORRECT():
    data = {"hola": "mundo", "phone": { "hello": "world"}}
    response = client.post(
        '/infoUsers',
        json = data
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [ { "loc": [ "body", "phone" ], "msg": "str type expected", "type": "type_error.str" } ]
    }

def test_post_info_CREATE():
    data = {"name": "Alejandro", "last_name": "Soto", "phone": "+573210987654"}
    response = client.post(
        '/infoUsers',
        json = data
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json()['message'] == "USER_CREATED"
    assert response.json()['data']['name'] == 'Alejandro'
    assert response.json()['data']['last_name'] == 'Soto'
    assert response.json()['data']['phone'] == '+573210987654'

def test_get_info_USER_NOT_FOUND():
    response = client.get('/infoUsers/999')
    assert response.status_code == 204

def test_get_info_USER_FOUND():
    total = client.get('/infoUsers')
    response = client.get('/infoUsers/' + str(total.json()['total']))
    assert response.status_code == 200
    assert response.json()['name'] == 'Alejandro'
    assert response.json()['last_name'] == 'Soto'
    assert response.json()['phone'] == '+573210987654'

def test_put_info_NOT_DATA_UPDATE():
    total = client.get('/infoUsers')
    data = {}
    response = client.put(
        '/infoUsers/' + str(total.json()['total']), 
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] == 'NOT_DATA_UPDATE'

def test_put_info_USER_NOT_EXIST():
    data = {'phone': '+573123456789'}
    response = client.put(
        '/infoUsers/999', 
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] ==  'USER_NOT_EXIST'

def test_put_info_USER_UPDATED():
    data = {'name': 'Alejandro 2'}
    total = client.get('/infoUsers')
    response = client.put(
        '/infoUsers/' + str(total.json()['total']), 
        json = data
    )
    assert response.status_code == 200
    assert response.json()['message'] == 'USER_UPDATED'

def test_delete_info_USER_DELETED():
    total = client.get('/infoUsers')
    response = client.delete('/infoUsers/' + str(total.json()['total']))
    assert response.status_code == 200
    assert response.json()['message'] == 'USER_DELETED'

def test_delete_info_DELETE_USER_NOT_FOUND():
    response = client.delete('/infoUsers/999')
    assert response.status_code == 404
    assert response.json()['message'] == 'USER_NOT_FOUND'
