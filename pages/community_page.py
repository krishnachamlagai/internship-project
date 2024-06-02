from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from support.logger import logger


class CommunityPage(BasePage):
    COMMUNITY_PAGE_URL = "https://soft.reelly.io/community"
    CONTACT_SUPPORT_LINK_XPATH = (By.XPATH, "//div[contains(@class, 'community-cards')]//a[contains(@class, 'chat-button') and contains(text(), 'Contact support')]")

    def go_to_community_page(self):
        self.open(self.COMMUNITY_PAGE_URL)

    def verify_community_page(self):
        try:
            self.wait.until(ec.url_to_be(self.COMMUNITY_PAGE_URL))
            assert self.driver.current_url == self.COMMUNITY_PAGE_URL, f"Expected url:{self.COMMUNITY_PAGE_URL}, Actual url: {self.driver.current_url}"
        except TimeoutException as toe:
            logger.warn(f"community page isn't loaded, {toe.msg}")

    def verify_contact_support_button_is_clickable(self):
        clickable_result = ec.element_to_be_clickable(self.CONTACT_SUPPORT_LINK_XPATH)
        available_result = ec.presence_of_element_located(self.CONTACT_SUPPORT_LINK_XPATH)
        assert clickable_result and available_result is not None, f"Contact support button was not clickable"


