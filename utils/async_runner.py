import asyncio
import aiohttp
from typing import List, Dict


async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict:
    async with session.get(url) as response:
        return {"url": url, "status": response.status, "data": await response.json()}


async def fetch_multiple_urls(urls: List[str]) -> List[Dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)


async def run_async_tests(test_funcs: List):
    tasks = [func() for func in test_funcs]
    return await asyncio.gather(*tasks)
