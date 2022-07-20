from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page=LoginPage(browser,browser.current_url)
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    login_page.should_be_login_url()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser,link)
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.should_be_is_not_product()
    basket_page.should_be_is_basket_null()
    