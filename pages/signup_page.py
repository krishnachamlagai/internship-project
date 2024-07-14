from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class SignupPage(BasePage):
    FULLNAME_ID_LOCATOR = (By.ID, "Full-Name")
    EMAIL_ID_LOCATOR = (By.ID, "Email-3")
    PHONE_ID_LOCATOR = (By.ID, "phone2")
    PASSWORD_ID_LOCATOR = (By.ID, "field")

    def open_signup_page(self):
        self.open('https://soft.reelly.io/sign-up')

    def enter_account_information(self, fullname, phone, email, password):
        self.enter_fullname(fullname)
        self.enter_email(email)
        self.enter_phone(phone)
        self.enter_password(password)

    def verify_account_information(self, fullname, phone, email, password):
        # make sure they are visible
        # self.wait.until(ec.visibility_of_element_located(self.FULLNAME_ID_LOCATOR))
        # self.wait.until(ec.visibility_of_element_located(self.EMAIL_ID_LOCATOR))
        # self.wait.until(ec.visibility_of_element_located(self.PASSWORD_ID_LOCATOR))
        # self.wait.until(ec.visibility_of_element_located(self.PHONE_ID_LOCATOR))
        # retrieve entered information
        entered_fullname = self.find_element(*self.FULLNAME_ID_LOCATOR).get_attribute("value")
        entered_phone = self.find_element(*self.PHONE_ID_LOCATOR).get_attribute("value")
        entered_email = self.find_element(*self.EMAIL_ID_LOCATOR).get_attribute("value")
        entered_password = self.find_element(*self.PASSWORD_ID_LOCATOR).get_attribute("value")

        # assert the case
        assert entered_fullname == fullname, f"Fullname mismatch: expected '{fullname}', got '{entered_fullname}'"
        assert entered_phone == phone, f"Phone mismatch: expected '{phone}', got '{entered_phone}'"
        assert entered_email == email, f"Email mismatch: expected '{email}', got '{entered_email}'"
        assert entered_password == password, f"Password mismatch: expected '{password}', got '{entered_password}'"

    def enter_fullname(self, fullname):
        self.wait.until(ec.presence_of_element_located(self.FULLNAME_ID_LOCATOR))
        self.find_element(*self.FULLNAME_ID_LOCATOR).send_keys(fullname)

    def enter_phone(self, phone):
        self.find_element(*self.PHONE_ID_LOCATOR).send_keys(phone)

    def enter_email(self, email):
        self.find_element(*self.EMAIL_ID_LOCATOR).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_ID_LOCATOR).send_keys(password)
