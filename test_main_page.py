from selenium.webdriver.common.by import By

#тестовые данные
link = "http://selenium1py.pythonanywhere.com/"

# Открыть страницу логина (в отдельной функции)
def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

# Тест
def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)