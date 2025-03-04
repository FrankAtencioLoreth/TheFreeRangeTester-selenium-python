import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
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
        help="Type of browser: chrome, firefox, edge"
    )

@pytest.fixture(scope="session")
def browser(request) -> any:
    """
    Browser configuration
    """

    browser_name = request.config.getoption("--browser").lower()
    # select a browser agree to match with the parameter --browser given via command line
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name == "firefox":
        firefox_options =Options()
        firefox_options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    elif browser_name == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("-inprivate")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def sandbox_page(browser: any) -> SandBoxPage:
    return SandBoxPage(browser)
