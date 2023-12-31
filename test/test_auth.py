import pytest

from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage
from pages.locators import AuthPage
from settings import valid_phone, valid_password, valid_email, invalid_phone, invalid_password, invalid_email


def test_auth_page_open(browser):
    page = AuthPage(browser)
    assert page.get_relative_link() == "/auth/realms/b2c/protocol/openid-connect/auth"


def test_auth_page_with_valid_phone(web_browser):
    page = AuthPage(web_browser)
    page.enter_phone(valid_phone)
    page.enter_pass(valid_password)
    page.btn_click()

    assert web_browser.find_element(By.ID,"lk-btn"), "login error"
    assert page.get_relative_link() == '/account_b2c/page', "login error"


def test_auth_page_with_valid_mail(web_browser):
    page = AuthPage(web_browser)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()

    assert web_browser.find_element(By.ID, "lk-btn"), "login error"
    assert page.get_relative_link() == '/account_b2c/page', "login error"


def test_auth_page_with_invalid_phone(web_browser):
    page = AuthPage(web_browser)
    page.enter_phone(invalid_phone)
    page.enter_pass(valid_password)
    page.btn_click()

    assert web_browser.find_element(By.CSS_SELECTOR, "span[id='form-error-message']")
    assert page.get_relative_link() != '/account_b2c/page', "login error"


def test_auth_page_with_valid_phone_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.enter_phone(valid_phone)
    page.enter_pass(invalid_password)
    page.btn_click()

    assert web_browser.find_element(By.CSS_SELECTOR, "span[id='form-error-message']")
    assert page.get_relative_link() != '/account_b2c/page', "login error"


def test_auth_page_with_invalid_mail(web_browser):
    page = AuthPage(web_browser)
    page.enter_email(invalid_email)
    page.enter_pass(valid_password)
    page.btn_click()

    assert web_browser.find_element(By.CSS_SELECTOR, "span[id='form-error-message']")
    assert page.get_relative_link() != '/account_b2c/page', "login error"


def test_auth_page_with_valid_mail_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.enter_email(valid_email)
    page.enter_pass(invalid_password)
    page.btn_click()

    assert web_browser.find_element(By.CSS_SELECTOR, "span[id='form-error-message']")
    assert page.get_relative_link() != '/account_b2c/page', "login error"


def test_auth_by_vk(browser):
    page = AuthPage(browser)
    page.auth_by_vk.click()
    assert page.get_relative_link() == "/authorize"


def test_auth_by_odhoklassniky(browser):
    page = AuthPage(browser)
    page.auth_by_odnoklassniky.click()
    assert page.get_relative_link() == "/dk"


def test_auth_by_mail(browser):
    page = AuthPage(browser)
    page.auth_by_mail.click()
    assert page.get_relative_link() == "/oauth/authorize"

def test_auth_by_yandex(browser):
    page = AuthPage(browser)
    page.auth_by_yandex.click()
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"
