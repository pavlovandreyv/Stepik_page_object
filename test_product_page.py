from .pages.product_page import ProductPage
import pytest, time


@pytest.mark.parametrize('link_promo', ["0","1","2","3","4","5","6","7","8","9"])
def test_guest_can_add_product_to_basket(browser,link_promo):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_promo}"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_to_basket()