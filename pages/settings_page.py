from support.logger import logger

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class SettingsPage(BasePage):
    COMMUNITY_LINK_XPATH = (By.XPATH, "//a[@href='/community' and contains(@class, 'page-setting-block')]")

    def open_community_link(self):
        try:
            community_link = self.wait.until(ec.element_to_be_clickable(self.COMMUNITY_LINK_XPATH))
            community_link.click()
        except TimeoutException as te:
            logger.warning(f"Community link is not opened: {te}")


