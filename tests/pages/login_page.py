from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    LOGIN_MSG = (By.ID, "login-msg")
    LOGIN_SECTION = (By.ID, "login-section")
    DASHBOARD_SECTION = (By.ID, "dashboard-section")

    def open(self, base_url):
        self.driver.get(base_url)
        self.wait_visible(self.LOGIN_SECTION)

    def login(self, username, password):
        self.wait_visible(self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

        self.wait_visible(self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.wait_clickable(self.LOGIN_BTN).click()

    def get_error(self):
        return self.wait_visible(self.LOGIN_MSG).text
