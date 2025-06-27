from playwright.sync_api import Page, expect
from config.config import Config
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = Config.BASE_URL

    @allure.step("Открыть страницу {path}")
    def goto(self, path=""):
        url = f"{self.base_url}/{path}" if path else self.base_url
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)
        allure.attach.file(
            f"screenshots/{name}.png",
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Дождаться элемента {selector}")
    def wait_for_element(self, selector, timeout=30000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)