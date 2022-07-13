from src.app import app

def test_index():
    response = app.test_client().get("/")
    assert response.data.decode('utf-8') == 'Hello world'

def test_message_post():
    pass

def test_message_get():
    response = app.test_client().get("/message/hello")
    assert (response != None)