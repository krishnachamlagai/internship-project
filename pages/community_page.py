from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class CommunityPage(BasePage):
    CONTACT_SUPPORT_LINK_XPATH = (By.XPATH, "//div[contains(@class, 'community-cards')]//a[contains(@class, 'chat-button') and contains(text(), 'Contact support')]")

    def verify_community_page(self):
        self.verify_partial_url('/community')

    def verify_contact_support_button_is_clickable(self):
        clickable_result = ec.element_to_be_clickable(self.CONTACT_SUPPORT_LINK_XPATH)
        available_result = ec.presence_of_element_located(self.CONTACT_SUPPORT_LINK_XPATH)
        assert clickable_result and available_result is not None, f"Contact support button was not clickable"


