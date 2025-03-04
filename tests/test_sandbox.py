import pytest
from .conftest import *
from pages.sandbox_page import SandBoxPage


@pytest.mark.sandbox
@pytest.mark.regression
def test_click_send(sandbox_page: pytest.fixture) -> None:
    """
    Test to click the 'Send' button
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    sandbox_page.click_send_button()

@pytest.mark.sandbox
@pytest.mark.regression
def test_click_dynamic_id_button(sandbox_page: pytest.fixture) -> None:
    """
    Test to click the dynamic ID button and verify if the hidden text appears
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    # Click on dynamic id button
    sandbox_page.click_dynamic_id_button()

    # Wait for the hidden text to appear after clicking the button
    hidden_element = sandbox_page.wait_for_elements(
        sandbox_page.HIDDEN_TEXT
    )
    expected_text = (
        "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    )

    # Assert that the expected text matches the displayed text
    assert (
        expected_text in hidden_element.text
    ), "Expected text doesn't match with given text"

@pytest.mark.sandbox
@pytest.mark.regression
def test_hover_send_button(sandbox_page: pytest.fixture) -> None:
    """
    Test to hover over the dynamic ID button and check if the background color changes
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()

    # Wait for the dynamic ID button to be available
    dynamic_button = sandbox_page.wait_for_elements(
        sandbox_page.DYNAMIC_ID_BUTTON
    )
    dynamic_button_color_before_hover = dynamic_button.value_of_css_property("background-color")

    # Perform hover action over the dynamic ID button
    sandbox_page.hover_over_dynamic_id_button()
    dynamic_button_color_after_hover = dynamic_button.value_of_css_property("background-color")

    # Assert that the button color changes after hover
    assert (
        dynamic_button_color_after_hover != dynamic_button_color_before_hover
    ), "The button color did not change after hover"

@pytest.mark.sandbox
@pytest.mark.regression
def test_checkbox(sandbox_page: pytest.fixture) -> None:
    """
    Test to select a check button by a label text
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    # Select a checkbox by text label
    sandbox_page.select_checkbox_by_text("Pasta")

@pytest.mark.sandbox
@pytest.mark.regression
def test_radio_button(sandbox_page: pytest.fixture) -> None:
    """
    Test to select a radio button by a label text
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    # Select a radio button by text label
    sandbox_page.select_radio_button_by_text("Si")

@pytest.mark.sandbox
@pytest.mark.regression
def test_select_by_text(sandbox_page: pytest.fixture) -> None:
    """
    Test to select an option from dropdown
    """

    option = "Basketball"
    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    # Select a specific item through visible text
    sandbox_page.select_sport_by_text(option)

    assert (
        option == sandbox_page.get_sport_selected()
    ),"The option given don't match with the selected option from sport dropdown"

@pytest.mark.sandbox
@pytest.mark.regression
def test_sport_dropdown_options(sandbox_page: pytest.fixture) -> None:
    """
    Test options available from dropdown
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    # Get all options in the dropdown
    options = sandbox_page.get_sport_options_from_dropdown()

    expected_options = ["Selecciona un deporte", "Fútbol", "Tennis", "Basketball"]

    assert (
        option in options for option in expected_options
    ), "Error: not all options is available in the dropdown"

@pytest.mark.sandbox
@pytest.mark.regression
def test_modal_title(sandbox_page: pytest.fixture) -> None:
    """
    Test that validate the modal
    """

    # Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()
    sandbox_page.click_show_modal_button()

    modal_title = sandbox_page.get_modal_title()
    expected_title = "Popup de ejemplo"

    assert (
            modal_title == expected_title
    ), f"The modal title: {modal_title} don't match with the expected title: {expected_title}"

@pytest.mark.sandbox
@pytest.mark.regression
@pytest.mark.table
def test_dynamic_table(sandbox_page: pytest.fixture) -> None:
    """
    Test that validate a dynamic table
    """
    #Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()

    before_value = sandbox_page.get_dynamic_table_values(2,3)

    sandbox_page.reload_page()

    after_value = sandbox_page.get_dynamic_table_values(2,3)

    assert (
        before_value != after_value
    ), f"The before value: {before_value} and after value: {after_value} is not same"

@pytest.mark.sandbox
@pytest.mark.regression
@pytest.mark.static_table
def test_static_table(sandbox_page: pytest.fixture) -> None:
    """
    Test that validate a static table
    """
    #Navigate to sandbox page
    sandbox_page.navigate_to_sandbox()

    before_value = sandbox_page.get_static_table_values(2,3)

    sandbox_page.reload_page()

    after_value = sandbox_page.get_static_table_values(2,3)

    assert (
        before_value == after_value
    ), f"The before value: {before_value} and after value: {after_value} is not same"

