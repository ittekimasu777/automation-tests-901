from .base_page import BasePage
import allure

class ProductsPage(BasePage):
    @allure.step("Добавить товар {product_name} в корзину")
    def add_to_cart(self, product_name):
        self.page.click("a[href='/products']")
        product = self.page.locator(f"text={product_name}").first
        product.hover()
        self.page.click("a.add-to-cart")
        self.page.click("button:has-text('Continue Shopping')")