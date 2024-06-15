from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options

#  Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ .\features\tests\community_page.feature


def browser_init(context):
    """
    :param context: Behave context
    """
    # mobile_emulation = {"deviceName": "iPhone 14 Pro Max"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # HEADLESS MODE
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    bs_username = "krishnachamlagai_2mDMiK"
    bs_access = "XzcjZqjXLFuGXBfqiiij"
    bs_url = f"http://{bs_username}:{bs_access}@hub-cloud.browserstack.com/wd/hub"

    options = Options()
    bs_options = {
        "deviceName": "iPhone 15 Pro Max",
        "osVersion": "17",
        "browserName": "chromium",
        "deviceOrientation": "portrait",
    }
    options.set_capability("bstack:options", bs_options)
    context.driver = webdriver.Remote(command_executor=bs_url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    context.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
