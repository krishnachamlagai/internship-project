from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = "kanchi_krishna12@yahoo.com"
    PASSWORD = "Flower12"
    USERNAME_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button w-button']")

    def login(self):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(self.USERNAME)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(self.PASSWORD)
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

