import pytest
from IPython.extensions.storemagic import restore_data

from loantap import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp=client.get('/')
    assert resp.status_code==200

def test_predict(client):
    resp=client.get('/predict')
    assert resp.status_code==200
