from types import SimpleNamespace
from typing import Any

from behave.runner import Context
from behave.model import Feature, Scenario, Step

from ai.selector_healer import AISelectorHealer
from utils.browser.browser import prepare_browser
from helpers.constants import REPORTS, ENV_CONFIG_JSON, ENDPOINTS_CONFIG_JSON, USERS_CONFIG_JSON
from pages.page_factory import PageFactory
from utils.logger import log_failure
from utils.reporting import attach_screenshot


def before_all(context: Context) -> None:
    context.ENV = context.config.userdata.get("env", "sit")
    context.COUNTRY = context.config.userdata.get("country", "cn")
    context.RESOURCES = REPORTS
    context.URLS = getattr(ENV_CONFIG_JSON, context.ENV)
    context.USERS = getattr(USERS_CONFIG_JSON, context.COUNTRY)
    context.ENDPOINTS = getattr(ENDPOINTS_CONFIG_JSON, "endpoints")
    context.CONTEXT = getattr(ENDPOINTS_CONFIG_JSON, "context")
    context.BASE_URL = context.URLS.BASE_URL
    prepare_browser(context)
    context.page_factory = PageFactory()
    context.ai = AISelectorHealer()
    context.store: dict[str, Any] = {}


def after_all(context: Context) -> None:
    context.browser_manager.stop()


def before_feature(context: Context, feature: Feature) -> None:
    context.feature.store = {}


def before_scenario(context: Context, scenario: Scenario) -> None:
    context.kwargs = {}
    context.response = None
    context.request = SimpleNamespace()
    context.upload_file = None
    context.scenario.store = {}


def before_step(context: Context, step: Step) -> None:
    context.bdd_step = step.name


def after_step(context: Context, step: Step) -> None:
    if step.status == "failed":
        log_failure(f"Step failed: {step.name}")
        if hasattr(context, "page"):
            attach_screenshot(context, step)
