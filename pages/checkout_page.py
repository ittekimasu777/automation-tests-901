from .base_page import BasePage
import allure


class CheckoutPage(BasePage):
    @allure.step("Оформить заказ")
    def checkout(self):
        self.page.click("a[href='/view_cart']")
        self.page.click("text=Proceed To Checkout")
        self.page.click("text=Place Order")

    @allure.step("Ввести платежные данные")
    def enter_payment(self):
        self.page.fill("input[name='name_on_card']", "Test User")
        self.page.fill("input[name='card_number']", "4111111111111111")
        self.page.fill("input[name='cvc']", "123")
        self.page.fill("input[name='expiry_month']", "12")
        self.page.fill("input[name='expiry_year']", "2025")
        self.page.click("#submit")

    @allure.step("Скачать инвойс")
    def download_invoice(self):
        with self.page.expect_download() as download:
            self.page.click("text=Download Invoice")
        return download.value