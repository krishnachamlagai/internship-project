from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):
    BASE_URL = "https://soft.reelly.io/sign-in"
    SETTINGS_LINK_XPATH = (By.XPATH, "//a[@href='/settings' and contains(@class, 'menu-button-block')]")
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
        settings_link = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(self.SETTINGS_LINK_XPATH))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", settings_link)
        settings_link.click()



