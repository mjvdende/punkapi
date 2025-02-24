import pytest

@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.benchmark
async def test_beers_response_time(client, benchmark):
    async def fetch():
        return await client.get("/beers?page=1")  
    result = benchmark(fetch)  
    response = await result 
    
    assert response.status_code == 200  