from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage
from tests.pages.form_page import FormPage

def test_submit_ticket_success(driver, base_url):
    login = LoginPage(driver)
    dash = DashboardPage(driver)
    form = FormPage(driver)

    login.open(base_url)
    login.login("admin", "1234")
    dash.wait_loaded()

    form.submit_ticket("Bug", "Something is not working")
    assert form.message() == "Ticket submitted successfully!"

def test_submit_ticket_validation(driver, base_url):
    login = LoginPage(driver)
    dash = DashboardPage(driver)
    form = FormPage(driver)

    login.open(base_url)
    login.login("admin", "1234")
    dash.wait_loaded()

    form.submit_ticket("Hi", "12345")  # title קצר מדי
    assert form.message() == "Title must be at least 3 chars"
