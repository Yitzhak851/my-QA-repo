# conftest.py
import pytest

import os
import pytest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:8000"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # אפשר להדליק בהמשך (CI)
    options.add_argument("--window-size=1200,900")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(0)  # נעדיף explicit waits
    yield drv
    drv.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            file_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

            driver.save_screenshot(file_path)
