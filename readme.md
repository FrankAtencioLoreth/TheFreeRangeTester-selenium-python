# TheFreeRangeTester-selenium-python

This repository contains automated tests using Selenium with Python, following the Free Range Tester approach. The project is organized to facilitate the development and execution of web application tests.

## Requirements

- **Python**: Ensure that Python (version 3.5 or higher) is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

- **Selenium**: Install the Selenium library for Python using `pip`:

  ```bash
  pip install selenium
  ```

- **WebDriver**: Depending on the browser you intend to use for testing, download and install the appropriate WebDriver:

  - **Firefox**: Requires [GeckoDriver](https://github.com/mozilla/geckodriver/releases).
  - **Chrome**: Requires [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

  Ensure that the WebDriver executable is in your system's PATH.

- **pytest**: For running the tests, install `pytest`:

  ```bash
  pip install pytest
  ```

## Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/FrankAtencioLoreth/TheFreeRangeTester-selenium-python.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd TheFreeRangeTester-selenium-python
   ```

3. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment**:

   - On Windows:

     ```bash
     .\env\Scriptsctivate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

5. **Install the required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not provided, manually install the dependencies:

   ```bash
   pip install selenium pytest
   ```

## Project Structure

The project is organized as follows:

```
TheFreeRangeTester-selenium-python/
├── .idea/
├── .vscode/
├── TestEnv/
├── pages/
├── testData/
├── tests/
├── .gitignore
├── instructions.txt
├── pytest.ini
└── requierements.txt

```

- `.idea/` and `.vscode/`: Configuration files for IDEs like PyCharm and Visual Studio Code.
- `TestEnv/`: Environment setup files or configurations.
- `pages/`: Page Object Models (POM) representing the web pages under test.
- `testData/`: Test data files used during test execution.
- `tests/`: Contains the test cases.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `instructions.txt`: Additional instructions or notes.
- `pytest.ini`: Configuration file for pytest.
- `requirements.txt`: libraries

## Running the Tests

1. **Activate the virtual environment** (if not already active):

   - On Windows:

     ```bash
     .\env\Scriptsctivate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

2. **Navigate to the `tests` directory**:

   ```bash
   cd tests
   ```

3. **Execute the tests using `pytest`**:

   ```bash
   pytest
   ```
4. **Run an specific test by filename**
   ```bash 
   pytest route\test_example.py
   ```
5. **Run an specific test by tag name**
    
    ```bash
       pytest -m tagname
    ```
6. **Run pytest using parallel tests**
   ```bash
    pytest test_name.py -n <number of workers>
   ```
7. **Run test using allure reports**
    ```bash
    pytest test --alluredir reports
    allure serve allure-reports
   ```

   This will automatically discover and run all test cases in the `tests` directory.

## Additional Notes

- Ensure that the version of the WebDriver matches the version of the browser installed on your system.
- Keep your Python packages updated to the latest versions to avoid compatibility issues.
- Refer to the Selenium [documentation](https://www.selenium.dev/documentation/en/) for more details on writing and running tests.

---

This `README.md` provides an overview of the project setup, requirements, and instructions to run the tests. For more detailed information, refer to the specific files and directories mentioned above.
