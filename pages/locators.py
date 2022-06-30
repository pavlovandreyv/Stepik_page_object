from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_IN = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER = (By.CSS_SELECTOR, "[value='Register1']")