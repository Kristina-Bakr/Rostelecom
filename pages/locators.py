import time

from selenium.webdriver.common.by import By


class AuthLocators:
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_LOGIN = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_REG_IN = (By.ID, "kc-register")
    AUTH_BY_VK = (By.ID, "oidc_vk")
    AUTH_BY_OK = (By.ID, "oidc_ok")
    AUTH_BY_MAIL = (By.ID, "oidc_mail")
    AUTH_BY_YANDEX = (By.ID, "oidc_ya")

class AuthPage:
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.reg_in = driver.find_element(*AuthLocators.AUTH_REG_IN)
        self.reg_in = driver.find_element(*AuthLocators.AUTH_REG_IN)
        self.auth_by_vk = driver.find_element(*AuthLocators.AUTH_BY_VK)
        self.auth_by_odnoklassniky = driver.find_element(*AuthLocators.AUTH_BY_OK)
        self.auth_by_mail = driver.find_element(*AuthLocators.AUTH_BY_MAIL)
        self.auth_by_yandex = driver.find_element(*AuthLocators.AUTH_BY_YANDEX)

    def enter_reg_page(self):
        # Нажимаеn на кнопку 'Зарегистрироваться'
        self.reg_in.click()
        time.sleep(10)

    def auth_by_vk(self):
        # Нажимает на иконку авторизации через 'ВКонтакте'
        self.auth_by_vk()
        time.sleep(10)

    def auth_by_odnoklassniky(self):
       # """Нажимает на иконку авторизации через 'Одноклассники'
        self.auth_by_odnoklassniky()
        time.sleep(10)

    def auth_by_mail(self):
        #"""Нажимает на иконку авторизации через mail.ru
        self.auth_by_mail()
        time.sleep(10)


    def auth_by_yandex(self):
        #Нажимает на иконку авторизации через yandex
        self.auth_by_yandex()
        time.sleep(10)


class RegisterLocators:
    FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LASTNAME = (By.CSS_SELECTOR, "input[name='lastName']")
    ADDRESS = (By.CSS_SELECTOR, "input[id='address']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    PASSWORD_CONF = (By.CSS_SELECTOR, "input[id='password-confirm']")
    REG_BTN = (By.CSS_SELECTOR, "button[name='register']")
