import playwright.sync_api
from playwright.sync_api import Page, expect
import logging

from utils.logger import log_info_emoji


def ai_selector_healer(context, exception, original_selector="") -> str:
    locator = ""
    log_info_emoji("⚠️ ", "Selector failed, attempting to heal with AI...")

    new_selector = context.ai.heal_selector(
        context=context,
        exception=exception,
        original_selector=original_selector
    )

    try:
        locator = context.page.locator(new_selector)
        locator.wait_for(timeout=5000)
        log_info_emoji(
            "✅ ", "AI-healed selector is valid and found an element.")
    except Exception as e:
        log_info_emoji("❌ ", f"AI-healed selector is invalid: {e}")
    return locator


class BasePage:

    def __init__(self, page: Page, context):
        self.page = page
        self.context = context
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate_to(self, url: str):
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url, timeout=120000)

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def get_page_content(self):
        return self.page.content()

    def click_element(self, selector: str):
        self.page.click(selector)

    def fill_input(self, selector: str, value: str):
        self.page.locator(selector).wait_for(timeout=5000)
        self.page.fill(selector, value)

    def fill_label_input(self, label_text: str, value: str):
        self.page.get_by_label(label_text).fill(value)

    def fill_input_ai(self, selector: str, value: str):
        try:
            self.fill_input(selector, value)
        except Exception as e:
            locator = ai_selector_healer(self.context, e, selector)
            locator.fill(value)

    def verify_label_value(self, label_text: str, expected_value: str):
        expect(self.page.get_by_label(label_text)).to_have_value(expected_value)

    def select_option(self, selector: str, value: str):
        self.page.select_option(selector, value)

    def check_checkbox(self, selector: str):
        self.page.check(selector)

    def uncheck_checkbox(self, selector: str):
        self.page.uncheck(selector)

    def is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def get_element_text(self, selector: str) -> str:
        return self.page.text_content(selector)

    def get_page_text(self) -> str:
        return self.page.content().lower()

    def verify_text_present(self, text: str) -> None:
        expect(self.page.get_by_text(text, exact=True)).to_be_visible()

    def verify_link_present(self, link_text: str) -> None:
        expect(self.page.get_by_role("link", name=link_text)).to_be_visible()

    def click_button_by_exact_text(self, button_text: str) -> None:
        self.page.get_by_role("button", name=button_text, exact=True).click()
