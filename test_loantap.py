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
    test_data = {
        "loan_amt": 15000,
        "term": 36,
        "int_rate": 12,
        "installment": 3600,
        "income": 36000
    }
    resp=client.post('/predict',json=test_data)
    assert resp.text=='Loan Approved'
