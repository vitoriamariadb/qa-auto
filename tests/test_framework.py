import pytest
from utils.data_loader import load_users, load_api_endpoints
from utils.report_generator import ReportGenerator
from utils.async_runner import fetch_multiple_urls
from pathlib import Path


def test_data_loader_users():
    users = load_users()
    assert isinstance(users, list)
    assert len(users) > 0
    assert "name" in users[0]


def test_data_loader_endpoints():
    endpoints = load_api_endpoints()
    assert isinstance(endpoints, list)
    assert len(endpoints) > 0
    assert "endpoint" in endpoints[0]


def test_report_generator_creation():
    generator = ReportGenerator()
    assert generator.output_dir.exists()


def test_report_generator_html():
    generator = ReportGenerator()
    results = {"total": 10, "passed": 8, "failed": 2}
    filename = generator.generate_html(results)
    assert filename.exists()
    filename.unlink()


def test_report_generator_json():
    generator = ReportGenerator()
    results = {"total": 10, "passed": 8, "failed": 2}
    filename = generator.generate_json(results)
    assert filename.exists()
    filename.unlink()


@pytest.mark.asyncio
async def test_async_runner():
    urls = [
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/users/2",
    ]
    results = await fetch_multiple_urls(urls)
    assert len(results) == 2
    assert all(r["status"] == 200 for r in results)
