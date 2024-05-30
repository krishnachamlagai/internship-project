from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as ec
from pages.base_page import BasePage


class MainPage(BasePage):
    SETTINGS_LINK_XPATH = (By.XPATH, "//a[contains(@href, '/settings')]/ div[contains(@class,'menu-button-text')]")

    def open(self):
        self.driver.get("https://soft.reelly.io/")

    def click_settings_links(self):
        self.wait.until(ec.element_to_be_clickable(self.SETTINGS_LINK_XPATH))
        self.driver.find_element(*self.SETTINGS_LINK_XPATH).click()


