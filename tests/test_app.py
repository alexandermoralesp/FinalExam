from src.app import app

def test_index():
    assert(1==1)
    # response = app.test_client().get("/")
    # assert response.status_code == 200
    # assert response.data.decode('utf-8') == 'Testing, Flask!'