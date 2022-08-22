import pytest
from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_post_auth_NOT_DATA_CREATE():
    data = {}
    response = client.post(
        '/authUsers',
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] == "NOT_DATA_CREATE"

def test_post_auth_DATA_INCORRECT():
    data = {"hola": "mundo", "email": { "hello": "world"}}
    response = client.post(
        '/authUsers',
        json = data
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [ { "loc": [ "body", "email" ], "msg": "str type expected", "type": "type_error.str" } ]
    }

def test_post_auth_CREATE():
    data = {"email": "asd@co.co", "password": "123456", "encryptedToken": "100"}
    response = client.post(
        '/authUsers',
        json = data
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json()['message'] == "USER_CREATED"
    assert response.json()['data']['email'] == 'asd@co.co'
    assert response.json()['data']['password'] == '123456'
    assert response.json()['data']['encryptedToken'] == '100'

def test_get_auth_USER_NOT_FOUND():
    response = client.get('/authUsers/999')
    assert response.status_code == 204

def test_get_auth_USER_FOUND():
    total = client.get('/authUsers')
    response = client.get('/authUsers/' + str(total.json()['total']))
    assert response.status_code == 200
    assert response.json()['email'] == 'asd@co.co'
    assert response.json()['password'] == '123456'
    assert response.json()['encryptedToken'] == '100'

def test_put_auth_NOT_DATA_UPDATE():
    total = client.get('/authUsers')
    data = {}
    response = client.put(
        '/authUsers/' + str(total.json()['total']), 
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] == 'NOT_DATA_UPDATE'

def test_put_auth_USER_NOT_EXIST():
    data = {'email': 'asd2@co.co'}
    response = client.put(
        '/authUsers/999', 
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] ==  'USER_NOT_EXIST'

def test_put_auth_USER_UPDATED():
    data = {'email': 'asd2@co.co'}
    total = client.get('/authUsers')
    response = client.put(
        '/authUsers/' + str(total.json()['total']), 
        json = data
    )
    assert response.status_code == 200
    assert response.json()['message'] == 'USER_UPDATED'

def test_delete_auth_USER_DELETED():
    total = client.get('/authUsers')
    response = client.delete('/authUsers/' + str(total.json()['total']))
    assert response.status_code == 200
    assert response.json()['message'] == 'USER_DELETED'

def test_delete_auth_DELETE_USER_NOT_FOUND():
    response = client.delete('/authUsers/999')
    assert response.status_code == 404
    assert response.json()['message'] == 'USER_NOT_FOUND'
