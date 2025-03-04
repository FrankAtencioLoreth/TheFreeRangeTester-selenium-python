import pytest
import allure
from .conftest import *
from pages.sandbox_page import SandBoxPage

@allure.epic("web user interface")
@allure.feature("test send button")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sandbox
@pytest.mark.regression
def test_click_send(sandbox_page: pytest.fixture) -> None:
    """
    Test to click the 'Send' button
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()
    with allure.step("And I do click on send button"):
        sandbox_page.click_send_button()

@allure.epic("web user interface")
@allure.feature("test dynamic id")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sandbox
@pytest.mark.regression
def test_click_dynamic_id_button(sandbox_page: pytest.fixture) -> None:
    """
    Test to click the dynamic ID button and verify if the hidden text appears
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()
    # Click on dynamic id button
    with allure.step("And I do click on dynamic button"):
        sandbox_page.click_dynamic_id_button()

    with allure.step("Wait for the hidden text to appear after clicking the button"):
    # Wait for the hidden text to appear after clicking the button
        hidden_element = sandbox_page.wait_for_elements(
            sandbox_page.HIDDEN_TEXT
        )
        
    with allure.step("I define the expected value"):
        expected_text = (
            "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
        )

    with allure.step("Assert that the expected text matches the displayed text"):
        assert (
            expected_text in hidden_element.text
        ), "Expected text doesn't match with given text"

@allure.epic("web user interface")
@allure.feature("test send button hover")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sandbox
@pytest.mark.regression
def test_hover_send_button(sandbox_page: pytest.fixture) -> None:
    """
    Test to hover over the dynamic ID button and check if the background color changes
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()

    # Wait for the dynamic ID button to be available
    with allure.step("Wait for the dynamic ID button to be available"):
        dynamic_button = sandbox_page.wait_for_elements(
            sandbox_page.DYNAMIC_ID_BUTTON
        )
    
    with allure.step("I get the background color before hover"):
        dynamic_button_color_before_hover = dynamic_button.value_of_css_property("background-color")

    # Perform hover action over the dynamic ID button
    with allure.step("Perform hover action over the dynamic ID button"):
        sandbox_page.hover_over_dynamic_id_button()
        dynamic_button_color_after_hover = dynamic_button.value_of_css_property("background-color")

    # Assert that the button color changes after hover
    with allure.step("Assert that the button color changes after hover"):
        assert (
            dynamic_button_color_after_hover != dynamic_button_color_before_hover
        ), "The button color did not change after hover"

@allure.epic("web user interface")
@allure.feature("test checkbox")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.sandbox
@pytest.mark.regression
def test_checkbox(sandbox_page: pytest.fixture) -> None:
    """
    Test to select a check button by a label text
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()

    # Select a checkbox by text label
    with allure.step("Select a checkbox by text label"):
        sandbox_page.select_checkbox_by_text("Pasta")

@allure.epic("web user interface")
@allure.feature("test radio button")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.sandbox
@pytest.mark.regression
def test_radio_button(sandbox_page: pytest.fixture) -> None:
    """
    Test to select a radio button by a label text
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()
    
    # Select a radio button by text label
    with allure.step("Select a radio button by text label"):
        sandbox_page.select_radio_button_by_text("Si")

@allure.epic("web user interface")
@allure.feature("test select by text")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.sandbox
@pytest.mark.regression
def test_select_by_text(sandbox_page: pytest.fixture) -> None:
    """
    Test to select an option from dropdown
    """

    option = "Basketball"
    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()
    
    # Select a specific item through visible text
    with allure.step("Select a specific item through visible text"):
        sandbox_page.select_sport_by_text(option)

    with allure.step("Assert"):
        assert (
            option == sandbox_page.get_sport_selected()
        ),"The option given don't match with the selected option from sport dropdown"

@allure.epic("web user interface")
@allure.feature("test select options")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.sandbox
@pytest.mark.regression
def test_sport_dropdown_options(sandbox_page: pytest.fixture) -> None:
    """
    Test options available from dropdown
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()

    # Get all options in the dropdown
    with allure.step("Get all options in the dropdown"):
        options = sandbox_page.get_sport_options_from_dropdown()


    expected_options = ["Selecciona un deporte", "Fútbol", "Tennis", "Basketball"]

    with allure.step("Assert"):
        assert (
            option in options for option in expected_options
        ), "Error: not all options is available in the dropdown"

@allure.epic("web user interface")
@allure.feature("test modal")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.sandbox
@pytest.mark.regression
def test_modal_title(sandbox_page: pytest.fixture) -> None:
    """
    Test that validate the modal
    """

    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()

    # Click on modal button
    with allure.step("Click on modal button"):
        sandbox_page.click_show_modal_button()

    with allure.step("Get modal title"):
        modal_title = sandbox_page.get_modal_title()
        expected_title = "Popup de ejemplo"

    with allure.step("Assert"):
        assert (
                modal_title == expected_title
        ), f"The modal title: {modal_title} don't match with the expected title: {expected_title}"

@allure.epic("web user interface")
@allure.feature("test dynamic table")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sandbox
@pytest.mark.regression
@pytest.mark.dynamictable
def test_dynamic_table(sandbox_page: pytest.fixture) -> None:
    """
    Test that validate a dynamic table
    """
    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()

    with allure.step("Get dynamic table values"):
        before_value = sandbox_page.get_dynamic_table_values(2,3)

    # Reload page
    with allure.step("Reload page"):
        sandbox_page.reload_page()

    with allure.step("Get dynamic table values after reload page"):
        after_value = sandbox_page.get_dynamic_table_values(2,3)

    with allure.step("Assert"):
        assert (
            before_value != after_value
        ), f"The before value: {before_value} and after value: {after_value} is not same"

@allure.epic("web user interface")
@allure.feature("test static table")
@allure.story("user history")
@allure.issue("AUTOMATION-TEST-2025")
@allure.link("https://github.com/FrankAtencioLoreth")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.sandbox
@pytest.mark.regression
@pytest.mark.statictable
def test_static_table(sandbox_page: pytest.fixture) -> None:
    """
    Test that validate a static table
    """
    # Navigate to sandbox page
    with allure.step("Given I navigate to sandbox page"):
        sandbox_page.navigate_to_sandbox()

    with allure.step("Get static table values"):
        before_value = sandbox_page.get_static_table_values(2,3)

    with allure.step("Reload page"):
        sandbox_page.reload_page()

    with allure.step("Get static table values"):
        after_value = sandbox_page.get_static_table_values(2,3)

    with allure.step("Assert"):
        assert (
            before_value == after_value
        ), f"The before value: {before_value} and after value: {after_value} is not same"