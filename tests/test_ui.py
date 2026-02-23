import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_page_title(browser, base_url):
    browser.get(base_url)
    assert "Example" in browser.title


@pytest.mark.ui
def test_page_load(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    assert body is not None


@pytest.mark.ui
def test_heading_present(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text != ""


@pytest.mark.ui
@pytest.mark.slow
def test_multiple_pages(browser):
    urls = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net",
    ]
    for url in urls:
        browser.get(url)
        assert browser.current_url == url + "/"
