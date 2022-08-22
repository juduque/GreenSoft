import pytest
from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_post_role_NOT_DATA_CREATE():
    data = {}
    response = client.post(
        '/roleUsers',
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] == "NOT_DATA_CREATE"

def test_post_role_DATA_INCORRECT():
    data = {"hola": "mundo", "role": { "hello": "world"}}
    response = client.post(
        '/roleUsers',
        json = data
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [ { "loc": [ "body", "role" ], "msg": "str type expected", "type": "type_error.str" } ]
    }

def test_post_role_CREATE():
    data = {"role": "Manager", "expirationDate": "mañana", "username": "asd123"}
    response = client.post(
        '/roleUsers',
        json = data
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json()['message'] == "USER_CREATED"
    assert response.json()['data']['role'] == 'Manager'
    assert response.json()['data']['expirationDate'] == 'mañana'
    assert response.json()['data']['username'] == 'asd123'

def test_get_role_USER_NOT_FOUND():
    response = client.get('/roleUsers/999')
    assert response.status_code == 204

def test_get_role_USER_FOUND():
    total = client.get('/roleUsers')
    response = client.get('/roleUsers/' + str(total.json()['total']))
    assert response.status_code == 200
    assert response.json()['role'] == 'Manager'
    assert response.json()['expirationDate'] == 'mañana'
    assert response.json()['username'] == 'asd123'

def test_put_role_NOT_DATA_UPDATE():
    total = client.get('/roleUsers')
    data = {}
    response = client.put(
        '/roleUsers/' + str(total.json()['total']), 
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] == 'NOT_DATA_UPDATE'

def test_put_role_USER_NOT_EXIST():
    data = {'role': 'Admin'}
    response = client.put(
        '/roleUsers/999', 
        json = data
    )
    assert response.status_code == 404
    assert response.json()['message'] ==  'USER_NOT_EXIST'

def test_put_role_USER_UPDATED():
    data = {'role': 'Admin'}
    total = client.get('/roleUsers')
    print( '/roleUsers/' + str(total.json()['total']))
    response = client.put(
        '/roleUsers/' + str(total.json()['total']), 
        json = data
    )
    assert response.status_code == 200
    assert response.json()['message'] == 'USER_UPDATED'

def test_delete_role_USER_DELETED():
    total = client.get('/roleUsers')
    response = client.delete('/roleUsers/' + str(total.json()['total']))
    assert response.status_code == 200
    assert response.json()['message'] == 'USER_DELETED'

def test_delete_role_DELETE_USER_NOT_FOUND():
    response = client.delete('/roleUsers/999')
    assert response.status_code == 404
    assert response.json()['message'] == 'USER_NOT_FOUND'
