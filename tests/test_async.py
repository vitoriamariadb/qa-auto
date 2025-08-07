import pytest
import asyncio
import aiohttp


@pytest.mark.asyncio
async def test_async_request():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://jsonplaceholder.typicode.com/users/1"
        ) as response:
            assert response.status == 200
            data = await response.json()
            assert "name" in data


@pytest.mark.asyncio
async def test_multiple_async_requests():
    urls = [
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/users/2",
        "https://jsonplaceholder.typicode.com/users/3",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(session.get(url))

        responses = await asyncio.gather(*tasks)

        for response in responses:
            assert response.status == 200


@pytest.mark.asyncio
async def test_concurrent_api_calls():
    async def fetch_user(session, user_id):
        async with session.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        ) as response:
            return await response.json()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, i) for i in range(1, 6)]
        users = await asyncio.gather(*tasks)

        assert len(users) == 5
        for user in users:
            assert "name" in user

