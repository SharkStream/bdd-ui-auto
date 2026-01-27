from behave import then, given
from utils.encryption import decrypt


@then('I can see the welcome dashboard with "{username}" user')
def step_impl(context, username):
    expected_welcome_text = f"Hi, {username}!"
    # expected_welcome_text = f"Your password is invalid!"
    secure_page = context.page_factory.get_secure_page(context)
    secure_page.verify_text_present(expected_welcome_text)

@then('I can see "{link}" link on the page')
def step_impl(context, link):
    secure_page = context.page_factory.get_secure_page(context)
    secure_page.verify_link_present(link)

@given('I am on the login page by logging in through "{username}" user')
def step_impl(context, username):
    username = getattr(context.USERS, f"{username}")
    password = decrypt(getattr(context.USERS, f"{username}_password"))
    login_page = context.page_factory.get_login_page(context)
    login_page.navigate_to(context.ENDPOINTS.login)
    login_page.fill_name_input(username)
    login_page.fill_password_input(password)
    login_page.click_login_button()