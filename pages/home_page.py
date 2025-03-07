from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    HEADING = (By.TAG_NAME, "h1")
    PARAGRAPH = (By.TAG_NAME, "p")
    LINK = (By.TAG_NAME, "a")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def open(self):
        self.navigate_to(self.base_url)

    def get_heading_text(self):
        return self.find_element(self.HEADING).text

    def get_paragraph_text(self):
        return self.find_element(self.PARAGRAPH).text

    def click_link(self):
        self.click(self.LINK)

    def is_loaded(self):
        return self.is_visible(self.HEADING)

