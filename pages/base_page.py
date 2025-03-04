from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver) -> None:
        """
        Initializes the BasePage with a WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def navigate_to(self, url: str) -> None:
        """
        Navigates to a specified URL.
        :param url: The URL to navigate to
        """
        self.driver.get(url)

    def reload_page(self) -> None:
        """
        Reload the page
       """
        self.driver.refresh()

    def wait_for_elements(self, locator: tuple[str, str], timeout: int = 20) -> WebElement:
        """
        Waits for an element to be visible before proceeding.
        :param locator: The element locator (By strategy and value)
        :param timeout: Maximum wait time in seconds (default is 20 seconds)
        :return: The located web element
        """
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )
    
    def click(self, locator: tuple[str, str]) -> None:
        """
        Clicks on an element after waiting for it to be visible.
        :param locator: The element locator
        """
        self.wait_for_elements(locator).click()

    def type_text(self, text: str, locator: tuple[str, str]) -> None:
        """
        Clears the existing text in an input field and types new text.
        :param text: The text to be entered
        :param locator: The element locator
        """
        element = self.wait_for_elements(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Select an option from a dropdown by visible text.
        :param text: The visible text of the option to select
        :param locator: The dropdown element locator
        """
        dropdown = Select(self.wait_for_elements(locator))
        dropdown.select_by_visible_text(text)

    def select_from_dropdown_by_index(self, index: int, locator: tuple[str, str]) -> None:
        """
        Selects an option from a dropdown by index.
        :param index: The index of the option to select
        :param locator: The dropdown element locator
        """
        dropdown = Select(self.wait_for_elements(locator))
        dropdown.select_by_index(index)

    def get_options_from_dropdown(self, locator: tuple[str, str]) -> list[str]:
        """
        Return the dropdown options
        :param locator: The dropdown element locator
        :return list: The dropdown options
        """
        dropdown = Select(self.wait_for_elements(locator))
        return [option.text for option in dropdown.options]

    def get_selected_option(self, locator: tuple[str, str]) -> str:
        """
        Return the selected option from dropdown
        :param locator: The dropdown element locator
        :return str: The selected option
        """
        return Select(
            self.wait_for_elements(locator)
        ).first_selected_option.text

    def select_element(self, locator: tuple[str, str]) -> None:
        """
        Selects a checkbox or radio button if it is not already selected.
        :param locator: The element locator
        """
        element = self.wait_for_elements(locator)
        if not element.is_selected():
            element.click()

    def unselect_element(self, locator: tuple[str, str]) -> None:
        """
        Deselects a checkbox if it is currently selected.
        :param locator: The element locator
        """
        element = self.wait_for_elements(locator)
        if element.is_selected():
            element.click()
    
    def hover_element(self, locator: tuple[str, str]) -> None:
        """
        Moves the mouse cursor over an element.
        :param locator: The element locator
        """
        element = self.wait_for_elements(locator)
        ActionChains(self.driver).move_to_element(element).perform()