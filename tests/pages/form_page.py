from selenium.webdriver.common.by import By
from .base_page import BasePage

class FormPage(BasePage):
    TITLE = (By.ID, "title")
    DESC = (By.ID, "desc")
    SUBMIT = (By.ID, "submit-ticket-btn")
    MSG = (By.ID, "ticket-msg")

    def submit_ticket(self, title, desc):
        self.wait_visible(self.TITLE).clear()
        self.driver.find_element(*self.TITLE).send_keys(title)

        self.wait_visible(self.DESC).clear()
        self.driver.find_element(*self.DESC).send_keys(desc)

        self.wait_clickable(self.SUBMIT).click()

    def message(self):
        return self.wait_visible(self.MSG).text
