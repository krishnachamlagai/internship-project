from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class SettingsPage(BasePage):
    COMMUNITY_LINK_XPATH = (By.XPATH, "//a[contains(@href, '/community')]/ div[contains(text(),'Community')]")

    def open_community_link(self):
        self.wait.until(ec.element_to_be_clickable(self.COMMUNITY_LINK_XPATH))
        self.driver.find_element(*self.COMMUNITY_LINK_XPATH).click()


