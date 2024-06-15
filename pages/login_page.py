from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = "kanchi_krishna12@yahoo.com"
    PASSWORD = "Flower12"
    USERNAME_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button w-button']")

    def go_to_login_page(self):
        self.open("https://soft.reelly.io/sign-in")

    def login(self):
        if ec.url_contains('sign-in'):
            wait = WebDriverWait(self.driver, 10)

            username_field = wait.until(ec.presence_of_element_located(self.USERNAME_FIELD))
            username_field.send_keys(self.USERNAME)

            password_field = wait.until(ec.presence_of_element_located(self.PASSWORD_FIELD))
            password_field.send_keys(self.PASSWORD)

            signin_button = wait.until(ec.element_to_be_clickable(self.SIGN_IN_BUTTON))
            signin_button.click()
        else:
            self.go_to_login_page()
            self.login()

        # if ec.url_contains('sign-in'):
        #     # signin_button = self.find_element(*self.SIGN_IN_BUTTON)
        # signin_button = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(self.SIGN_IN_BUTTON))
        #     username_field = self.find_element(*self.USERNAME_FIELD)
        #     password_field = self.find_element(*self.PASSWORD_FIELD)
        #     username_field.send_keys(self.USERNAME)
        #     password_field.send_keys(self.PASSWORD)
        #     signin_button.click()
        # else:
        #     self.go_to_login_page()
        #     self.login()
