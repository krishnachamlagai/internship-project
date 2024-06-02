from time import sleep
from behave import given, when, then


@given("Open the main page")
def open_main_page(context):
    context.app.main_page.open_main_page()


@when("Login to the page")
def login_to_main_page(context):
    context.app.login_page.login()


@then("Click on settings option")
def click_settings(context):
    context.app.main_page.click_settings_links()


@then("Click on community option")
def click_community_menu(context):
    context.app.settings_page.open_community_link()


@then("Verify the right page opens")
def verify_right_page_opens(context):
    context.app.community_page.verify_community_page()


@then("Verify Contact support button is available and clickable")
def verify_contact_support_button(context):
    context.app.community_page.verify_contact_support_button_is_clickable()
