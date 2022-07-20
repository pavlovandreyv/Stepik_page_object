from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Ошибка: В URL нет login части"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN), "Ошибка: Нет кнопки Войти"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER), "Ошибка: Нет кнопки Зарегистрирвоаться"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER).click()