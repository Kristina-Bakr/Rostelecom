import pytest
from selenium import webdriver


# Инициализация браузера и закрытие по окончанию тестов
@pytest.fixture()
def browser():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()
