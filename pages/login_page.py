from .base_page import BasePage
from config.config import Config
import allure
from playwright.sync_api import expect


class LoginPage(BasePage):
    @allure.step("Выполнить вход")
    def login(self):
        try:

            self.goto("login")


            self.wait_for_element("input[data-qa='login-email']")
            self.take_screenshot("before_login")


            self.page.fill("input[data-qa='login-email']", Config.LOGIN_EMAIL)
            self.page.fill("input[data-qa='login-password']", Config.LOGIN_PASSWORD)


            with allure.step("Нажать кнопку Login"):
                login_button = self.page.locator("button[data-qa='login-button']")
                expect(login_button).to_be_enabled()
                login_button.click()


            with allure.step("Проверить успешный вход"):
                logged_in_text = self.page.locator("text=Logged in as")
                logged_in_text.wait_for(state="visible", timeout=15000)
                expect(logged_in_text).to_be_visible()

        except Exception as e:
            self.take_screenshot("login_error")
            allure.attach(
                self.page.content(),
                name="page_html",
                attachment_type=allure.attachment_type.HTML
            )
            raise Exception(f"Ошибка авторизации: {str(e)}") from e