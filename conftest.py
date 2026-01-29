import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.base_url = "https://demowebshop.tricentis.com"
    browser.config.window_width = 1400
    browser.config.window_height = 900
