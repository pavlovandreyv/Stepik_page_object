from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest,time

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link=f"http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page=LoginPage(browser,link)        
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org","passwordpassword")
        page.should_be_authorized_user()
    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page=ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_is_not_element_present()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page=ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_to_basket()

@pytest.mark.need_review
@pytest.mark.xfail
@pytest.mark.parametrize('link_promo', ["0","1","2","3","4","5","6","7","8","9"])
def test_guest_can_add_product_to_basket(browser,link_promo):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_promo}"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_to_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_is_not_element_present()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_element_has_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
  
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.should_be_is_not_product()
    basket_page.should_be_is_basket_null()