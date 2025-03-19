import pytest
from utils.selenium_helpers import wait_for_element, is_element_visible
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_selenium_helpers_wait_for_element(browser, base_url):
    browser.get(base_url)
    element = wait_for_element(browser, (By.TAG_NAME, "body"))
    assert element is not None


@pytest.mark.ui
def test_selenium_helpers_is_visible(browser, base_url):
    browser.get(base_url)
    is_visible = is_element_visible(browser, (By.TAG_NAME, "body"))
    assert is_visible is True


@pytest.mark.ui
def test_selenium_helpers_element_not_found(browser, base_url):
    browser.get(base_url)
    element = wait_for_element(browser, (By.ID, "nao-existe"), timeout=1)
    assert element is None
