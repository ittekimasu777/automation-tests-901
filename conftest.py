import pytest
from playwright.sync_api import Playwright
from config.config import Config
import allure
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(30000)
    yield page
    if hasattr(pytest, 'test_failed') and pytest.test_failed:
        page.screenshot(path=f"screenshots/{pytest.current_test_name}.png")
        allure.attach.file(
            f"screenshots/{pytest.current_test_name}.png",
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    page.close()

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)