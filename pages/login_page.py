from .base_page import BasePage

class LoginPage(BasePage):
    NAME_INPUT_LOCATOR = 'input#username'
    PASSWORD_INPUT_LOCATOR = 'input#password'
    LOGIN_BUTTON_LOCATOR = 'button#submit-login'

    def fill_name_input(self, value: str):
        self.fill_input(self.NAME_INPUT_LOCATOR, value)

    def fill_password_input(self, value: str):
        self.fill_input(self.PASSWORD_INPUT_LOCATOR, value)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON_LOCATOR)