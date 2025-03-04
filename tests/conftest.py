from email.policy import default

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.sandbox_page import SandBoxPage

def pytest_addoption(parser) -> None:

    # To execute via command line type next: pytest test_name --browser name_browser
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser run tests on"
    )

@pytest.fixture
def browser(request) -> webdriver:
    """
    Browser configuration
    """
    browser_name = request.config.option.browser
    driver = None

    # select a browser agree to match with the parameter --browser given via command line
    match browser_name.lower():
       case "chrome":
           chrome_options = webdriver.ChromeOptions()
           chrome_options.add_argument("--incognito")
           driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
       case "firefox":
           firefox_options =Options()
           firefox_options.set_preference("browser.privatebrowsing.autostart", True)
           driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
       case "edge":
           edge_options = webdriver.EdgeOptions()
           edge_options.add_argument("-inprivate")
           driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
       case _, None:
           print(f"Executing with a default browser {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def sandbox_page(browser: pytest.fixture()) -> SandBoxPage:
    return SandBoxPage(browser)
