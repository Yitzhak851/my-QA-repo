from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_SECTION = (By.ID, "dashboard-section")
    WELCOME = (By.ID, "welcome-msg")
    LOGOUT = (By.ID, "logout-btn")

    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BTN = (By.ID, "search-btn")
    SEARCH_RESULTS = (By.ID, "search-results")

    def wait_loaded(self):
        self.wait_visible(self.DASHBOARD_SECTION)

    def welcome_text(self):
        return self.wait_visible(self.WELCOME).text

    def logout(self):
        self.wait_clickable(self.LOGOUT).click()

    def search(self, query):
        self.wait_visible(self.SEARCH_INPUT).clear()
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(query)
        self.wait_clickable(self.SEARCH_BTN).click()

    def results_text(self):
        ul = self.wait_visible(self.SEARCH_RESULTS)
        return [li.text for li in ul.find_elements(By.TAG_NAME, "li")]
