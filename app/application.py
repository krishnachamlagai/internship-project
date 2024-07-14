
from pages.community_page import CommunityPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.signup_page import SignupPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)
        self.community_page = CommunityPage(driver)
        self.signup_page = SignupPage(driver)
