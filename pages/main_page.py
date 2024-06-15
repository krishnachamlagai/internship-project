from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):
    BASE_URL = "https://soft.reelly.io/sign-in"
    SETTINGS_LINK_XPATH = (By.XPATH, "//a[@href='/settings' and contains(@class, 'menu-button-block')]")
    # <a wized="mobileTabProfile" href="/settings" class="menu-button-wrapper w-inline-block">
    # <img src="https://cdn.prod.website-files.com/63c5585ff31e74bfcf46a136/648f771e931d79a81bb2f83f_all-features-menu.svg" loading="lazy" alt=""><
    # div class="mobile-top-menu">Menu</div></a
    # >
    MOBILE_SETTING_ICON_LINK_XPATH = (By.XPATH, "//a[@href='/setting' and contains(@class, 'menu-button-wrapper w-inline-block')]")
    MOBILE_ICON_LINK_XPATH = (By.XPATH, "//a[@wized='mobileTabProfile']")
    LOGIN_BODY = (By.XPATH, "//body[@class='login-body']")

    def open_main_page(self):
        self.open(self.BASE_URL)
        sleep(10)
        # this ensures the redirection happened
        # while True:
        #     current_url = self.driver.current_url
        #     if current_url == self.BASE_URL:
        #         WebDriverWait(self.driver, 10).until(
        #             ec.presence_of_element_located(self.LOGIN_BODY)
        #         )
        #     else:
        #         break

    def click_settings_links(self):
        settings_link = self.wait.until(ec.element_to_be_clickable(self.SETTINGS_LINK_XPATH))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", settings_link)
        settings_link.click()

    def click_mobile_settings_link(self):
        setting_icon_link = self.wait.until(ec.element_to_be_clickable(self.MOBILE_ICON_LINK_XPATH))
        setting_icon_link.click()



