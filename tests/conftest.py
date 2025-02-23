import pytest
import uvicorn
from fastapi.testclient import TestClient
from punkapi.app import app as create_app
from threading import Thread

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture(scope='session')
def client(app):
    return TestClient(app)

@pytest.fixture(scope='session', autouse=True)
def start_app():
    config = uvicorn.Config("punkapi.app:app", host="127.0.0.1", port=5000, log_level="info")
    server = uvicorn.Server(config)
    
    thread = Thread(target=server.run)
    thread.start()
    
    yield
    
    server.should_exit = True
    thread.join()