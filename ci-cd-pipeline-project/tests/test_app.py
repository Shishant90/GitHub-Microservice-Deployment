import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello Dostto I'm Shishant Kanojia" in response.data
    assert b"DevOps Engineer" in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Shishant Kanojia'
    assert 'CI/CD Pipeline Demo' in data['project']

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'