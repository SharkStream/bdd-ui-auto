# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A BDD (Behavior-Driven Development) UI automation testing framework using Python, Playwright, and Behave. Tests are written in Gherkin syntax (.feature files) and executed against web applications. The framework includes AI-powered selector healing for self-healing tests when selectors break.

## Running Tests

```bash
pip install -r requirements.txt               # Install dependencies
python run_tests.py                           # Run all tests (default: chromium, non-headless)
python run_tests.py --headless                # Run in headless mode
python run_tests.py --browser firefox         # Run with Firefox
python run_tests.py --parallel                # Run tests in parallel
python run_tests.py --parallel --workers 7    # Run with 7 parallel workers
python run_tests.py --tags @smoke             # Run tests with specific tags
python run_tests.py features/login.feature    # Run specific feature file
python run_tests.py --tracing                 # Enable Playwright tracing/videos
python run_tests.py --serve-report            # Serve Allure report after tests

allure serve reports/allure-results           # View Allure reports
```

## Architecture

### Test Flow
1. `run_tests.py` - Entry point; parses CLI args, sets up parallel workers, invokes Behave
2. `environment.py` - Behave hooks (before_all, after_all, before_scenario, etc.) initialize browser, context, and page factory
3. `.feature` files - Gherkin test scenarios in `features/`
4. `steps/*.py` - Step definitions mapping Gherkin steps to Python code
5. `pages/*.py` - Page Object Model classes for UI interactions

### Key Components

**Page Object Model:**
- `BasePage` - Common UI operations (click, fill, verify, navigate)
- `PageFactory` - Static factory returning page objects; accessed via `context.page_factory`
- Page classes inherit from `BasePage` and define page-specific selectors and methods

**AI Selector Healing:**
- `AISelectorHealer` in `ai/selector_healer.py` - Uses Ollama LLM to heal broken selectors
- When a selector fails, the AI analyzes the page HTML/screenshot and suggests a new selector
- Model configured in `resources/config.yaml` (e.g., `qwen3-coder:480b-cloud`)
- Methods like `fill_input_ai()` in BasePage trigger AI healing on failure

**Browser Management:**
- `BrowserManager` in `utils/browser/browser.py` - Wraps Playwright browser lifecycle
- Supports chromium, firefox, webkit via `--browser` CLI arg
- Optional tracing mode saves videos, HAR files, and trace zips

**Configuration:**
- `resources/generic/env.json` - Environment URLs (sit, uat, preprod, prod)
- `resources/generic/endpoints.json` - API/page endpoints
- `resources/generic/login.json` - User credentials (encrypted passwords)
- Environment selected via Behave userdata: `behave -D env=sit -D country=cn`

**Context Object:**
- `context.URLS` - Environment URLs from env.json
- `context.USERS` - User credentials from login.json
- `context.ENDPOINTS` - Page endpoints
- `context.page_factory` - Page object factory
- `context.page` - Current Playwright page
- `context.ai` - AI selector healer instance
- `context.store` / `context.scenario.store` - Data storage between steps

## Adding New Tests

1. Create `.feature` file in `features/` using Gherkin syntax
2. Create page class in `pages/` inheriting from `BasePage`
3. Add factory method in `PageFactory.get_page()` mapping
4. Create step definitions in `steps/` using Behave decorators (`@given`, `@when`, `@then`)
5. Add endpoints to `resources/generic/endpoints.json` if needed

## Encrypted Credentials

Passwords in `login.json` are encrypted. Use `utils/encryption.py` to decrypt:
```python
from utils.encryption import decrypt
password = decrypt(getattr(context.USERS, f"{username}_password"))
```