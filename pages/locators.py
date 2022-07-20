from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET=(By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOG_IN = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER = (By.CSS_SELECTOR, "[value='Register']")
    EMAIL_REGISTER=(By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_REGISTER=(By.CSS_SELECTOR, "[name='registration-password1']")
    PASSWORD_REGISTER2=(By.CSS_SELECTOR, "[name='registration-password2']")

class ProductPageLocators():
    ADD_PRODUCT=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_main h1")
    PRODUCT_NAME_M=(By.CSS_SELECTOR,"#messages>.alert:nth-child(1) strong")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".product_main .price_color")
    PRODUCT_PRICE_M=(By.CSS_SELECTOR,"#messages>.alert:nth-child(3) strong")

class BasketPageLocators():
    BASKET_NULL=(By.CSS_SELECTOR,"#content_inner>p")
    PRODUCT_IN_BASKET=(By.CSS_SELECTOR,".basket-items")