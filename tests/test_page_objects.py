import pytest
from pages.home_page import HomePage


@pytest.mark.ui
def test_home_page_title(browser, base_url):
    page = HomePage(browser, base_url)
    page.open()
    assert "Example" in page.get_title()


@pytest.mark.ui
def test_home_page_heading(browser, base_url):
    page = HomePage(browser, base_url)
    page.open()
    heading = page.get_heading_text()
    assert heading != ""


@pytest.mark.ui
def test_home_page_loaded(browser, base_url):
    page = HomePage(browser, base_url)
    page.open()
    assert page.is_loaded()
