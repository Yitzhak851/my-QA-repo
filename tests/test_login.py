from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage

def test_login_success(driver, base_url):
    login = LoginPage(driver)
    dash = DashboardPage(driver)

    login.open(base_url)
    login.login("admin", "1234")
    dash.wait_loaded()

    assert "Welcome, admin" in dash.welcome_text()

def test_login_failure(driver, base_url):
    login = LoginPage(driver)

    login.open(base_url)
    login.login("admin", "wrong")
    assert login.get_error() == "Invalid credentials"

def test_intentional_failure():
    assert False
