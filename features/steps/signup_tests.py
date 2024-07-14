from behave import given, when, then


@given('Open signup page')
def open_signup_page(context):
    context.app.signup_page.open_signup_page()


@then('Verify entered account information is present')
def verify_entered_account_information(context):
    context.app.signup_page.verify_entered_account_information()


@then("Enter account information {fullname} {phone} {email} {password} in the text fields")
def enter_account_information(context, fullname, phone, email, password):
    context.app.signup_page.enter_account_information(fullname, phone, email, password)


@then("Verify entered account information {fullname} {phone} {email} {password} is present")
def verify_account_information(context, fullname, phone, email, password):
    context.app.signup_page.verify_account_information(fullname, phone, email, password)
