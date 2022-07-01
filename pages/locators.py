from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_IN = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER = (By.CSS_SELECTOR, "[value='Register']")

class ProductPageLocators():
    ADD_PRODUCT=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_main h1")
    PRODUCT_NAME_M=(By.CSS_SELECTOR,"#messages>.alert:nth-child(1) strong")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".product_main .price_color")
    PRODUCT_PRICE_M=(By.CSS_SELECTOR,"#messages>.alert:nth-child(3) strong")