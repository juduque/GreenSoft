import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# def test_index_route():
#     response = client.get('/items/1')
#     assert response.status_code == 200
#     assert response.json() == {'item_id': 1, 'q': None}

# def test_index_route():
#     response = client.get('/items/hola')
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json() == {'item_id': 1, 'q': None}

def test_index_route():
    response = client.get('/items/1')
    assert response.status_code == 404
