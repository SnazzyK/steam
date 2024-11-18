import pytest

from utilities.drivers import WebDriverSingleton


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    driver = WebDriverSingleton.get_driver()
    yield driver
    WebDriverSingleton.quit_driver()
