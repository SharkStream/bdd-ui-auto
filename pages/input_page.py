from playwright.sync_api import expect
from .base_page import BasePage

class InputPage(BasePage):
    NUMBER_INPUT_LOCATOR = 'input#input-number'
    TEXT_INPUT_LOCATOR = 'input#input-text'
    PASSWORD_INPUT_LOCATOR = 'input#input-password'
    DATE_INPUT_LOCATOR = 'input#input-date'
    NUMBER_OUTPUT_LOCATOR = 'strong#output-number'
    TEXT_OUTPUT_LOCATOR = 'strong#output-text'
    PASSWORD_OUTPUT_LOCATOR = 'strong#output-password'
    DATE_OUTPUT_LOCATOR = 'strong#output-date'

    def fill_number_input(self, value: str):
        self.fill_input(self.NUMBER_INPUT_LOCATOR, value)

    def fill_text_input(self, value: str):
        self.fill_input(self.TEXT_INPUT_LOCATOR, value)

    def fill_password_input(self, value: str):
        self.fill_input(self.PASSWORD_INPUT_LOCATOR, value)

    def fill_date_input(self, value: str):
        self.fill_input(self.DATE_INPUT_LOCATOR, value)
    
    def verify_number_output(self, value: str) -> None:
        number_output_element = self.page.locator(self.NUMBER_OUTPUT_LOCATOR)
        expect(number_output_element).to_have_text(value)

    def verify_text_output(self, value: str) -> None:
        text_output_element = self.page.locator(self.TEXT_OUTPUT_LOCATOR)
        expect(text_output_element).to_have_text(value)

    def verify_password_output(self, value: str) -> None:
        password_output_element = self.page.locator(self.PASSWORD_OUTPUT_LOCATOR)
        expect(password_output_element).to_have_text(value)

    def verify_date_output(self, value: str) -> None:
        date_output_element = self.page.locator(self.DATE_OUTPUT_LOCATOR)
        expect(date_output_element).to_have_text(value)