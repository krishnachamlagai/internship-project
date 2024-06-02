from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def verify_partial_url(self, expected_url):
        self.wait.until(ec.url_contains(expected_url), message=f'Url does not contain {expected_url}')
