import asyncio
import pytest
import pytest_asyncio
import uvicorn
from httpx import AsyncClient
from threading import Thread
from punkapi.app import app

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:5001"

@pytest_asyncio.fixture(scope="session")
async def client(base_url):
    async with AsyncClient(base_url=base_url) as ac:
        yield ac

@pytest.fixture(scope='session', autouse=True)
def start_app():
    config = uvicorn.Config("punkapi.app:app", host="127.0.0.1", port=5001, log_level="info")
    server = uvicorn.Server(config)
    
    thread = Thread(target=server.run)
    thread.start()
    
    yield
    
    server.should_exit = True
    thread.join()