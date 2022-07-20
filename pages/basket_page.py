from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_is_basket_null(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NULL), "Нет текста 'Ваша корзина пуста'"   

    def should_be_is_not_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Продукт найден на странице"   