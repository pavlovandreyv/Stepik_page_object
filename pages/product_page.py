from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        add_link.click()

    def should_be_product_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text==self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_M).text, "Название продукта не соответствует"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text==self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_M).text, "Цена продукта не соответствует"