from selenium.webdriver.common.by import By
from .base_page import BasePage


class SandBoxPage(BasePage):

    # Locators for different elements on the sandbox page

    # Button to send
    SEND_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Enviar')]"  # Button to send a message
    )

    # Button that generates a dynamic ID and reveals hidden text
    DYNAMIC_ID_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]"
    )

    # Hidden text that appears after clicking the button
    HIDDEN_TEXT = (
        By.XPATH,
        "//p[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]"
    )

    # Sports select that allow to select an item
    SPORTS_DROPDOWN = (
        By.ID,
        "formBasicSelect"
    )

    # Button that show a modal window
    SHOW_MODAL_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Mostrar popup')]"
    )

    # Modal title
    LABEL_MODAL = (
        By.ID,
        "contained-modal-title-vcenter"
    )

    def __init__(self, driver) -> None:
        super().__init__(driver)  # Initialize the base page with the driver instance

    def navigate_to_sandbox(self) -> None:
        """
        Navigate to the sandbox automation testing page.
        """
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")

    def click_send_button(self) -> None:
        """
        Click the 'Send' button on the page.
        """
        self.click(self.SEND_BUTTON)

    def click_dynamic_id_button(self) -> None:
        """
        Click the button that generates a dynamic ID and reveals hidden text.
        """
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self) -> None:
        """
        Hover over the dynamic ID button.
        """
        self.hover_element(self.DYNAMIC_ID_BUTTON)

    def select_checkbox_by_text(self, label_text: str) -> None:
        """
        CLick the check button by label text on the page
        :param label_text: select the checkbox button by label text
        """
        options = ["Pizza", "Hamburguesa", "Pasta", "Helado", "Torta"]
        assert (
                label_text in options
        ), f"The option given don't match, please select an option to match  with given options: {options}"

        checkbox_button = (
            By.XPATH,
            f"//label[contains(.,'{label_text}')]/preceding-sibling::input[@type='checkbox']"
        )
        self.select_element(checkbox_button)

    def select_radio_button_by_text(self, label_text):
        """
       CLick the radio button by label text on the page
       :param label_text: select the radio button by label text
       """
        options = ["Si", "No"]
        assert (
                label_text in options
        ), f"The option given don't match, please select an option to match with given options: {options}"

        radio_button = (
            By.XPATH,
            f"//label[@class='form-check-label' and contains(text(), '{label_text}')]"
        )
        self.select_element(radio_button)

    def select_sport_by_text(self, sport_name: str) -> None:
        """
        Select a sports through a visible text
        :param sport_name: options
        """
        self.select_from_dropdown_by_visible_text(self.SPORTS_DROPDOWN, sport_name)

    def get_sport_options_from_dropdown(self) -> list[str]:
        """
        Get sports from dropdown
        :return sport_list: list of sports available in the dropdown
        """
        return self.get_options_from_dropdown(self.SPORTS_DROPDOWN)

    def get_sport_selected(self) -> str:
        """
        Get a selected sport from sport dropdown
        """
        return self.get_selected_option(self.SPORTS_DROPDOWN)

    def click_show_modal_button(self) -> None:
        """
        Click to show modal
        """
        self.hover_element(self.SHOW_MODAL_BUTTON)
        self.click(self.SHOW_MODAL_BUTTON)

    def get_modal_title(self) -> str:
        """
        Get the modal title
        :return modal_title: The modal title
        """
        return self.wait_for_elements(self.LABEL_MODAL).text

    def get_dynamic_table_values(self, row: int, column: int) -> str:
        """"
        Get cell value from a dynamic table
        :param row: row (int)
        :param column: column (int)
        :return: cell value (str)
        """
        cell_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{row}]/td[{column}]"
        cell = self.wait_for_elements((By.XPATH, cell_xpath))
        return cell.text if cell else None
    
    def get_static_table_values(self, row: int, column: int) -> str:
        """"
        Get cell value from a static table
        :param row: row (int)
        :param column: column (int)
        :return: cell value (str)
        """
        cell_xpath = f"(//h2[normalize-space()='Tabla estática']/following-sibling::table/tbody/tr)[{row}]/td[{column}]"
        cell = self.wait_for_elements((By.XPATH, cell_xpath))
        return cell.text if cell else None
