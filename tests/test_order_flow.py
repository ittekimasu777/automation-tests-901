import pytest
import allure
from config.config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
@pytest.mark.parametrize("product", [Config.PRODUCTS[0]])
def test_order_flow(login_page, product):
    with allure.step("Авторизация"):
        login_page.login()

    with allure.step("Добавление товара"):
        products_page = ProductsPage(login_page.page)
        products_page.add_to_cart(product)

    with allure.step("Оформление заказа"):
        checkout_page = CheckoutPage(login_page.page)
        checkout_page.checkout()
        checkout_page.enter_payment()

    with allure.step("Проверка заказа"):
        assert checkout_page.page.is_visible("text=Order Placed!")
        invoice = checkout_page.download_invoice()
        assert invoice.path() is not None