from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):
    SETTINGS_LINK_XPATH = (By.XPATH, "//a[@href='/settings' and contains(@class, 'menu-button-block')]")

    def open(self):
        self.driver.get("https://soft.reelly.io/")

    def click_settings_links(self):
        settings_link = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(self.SETTINGS_LINK_XPATH))
        settings_link.click()



