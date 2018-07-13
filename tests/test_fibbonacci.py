from fibboApp import create_app


def test_fibbo():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_invalidFibbo(client):
    response = client.get('/fibbonacci/api/v1.0/series/-12')
    assert response.data.error == "Please enter a positive integer value"

def test_validFibbo(client):
    response = client.get('/fibbonacci/api/v1.0/series/3')
    assert response.data == [0,1,1]