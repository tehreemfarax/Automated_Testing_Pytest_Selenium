# Automated_Testing_Pytest_Selenium

### Selenium-Pytest Login Test

This repository contains a set of automated tests for validating the login functionality of a web application using Selenium and pytest.

#### Project Structure

- **`test_login.py`**: Contains the test scenarios for logging into the web application.
- **`README.md`**: Provides information about the test setup, requirements, and execution instructions.
- **`.gitignore`**: Ignores specific files or directories from version control.
- *(Add any other necessary files or directories)*

#### Setup

1. **Prerequisites**:
   - Python installed on your system.
   - WebDriver for the desired browser (in this case, Chrome WebDriver).
  
2. **Installation**:
   - Clone this repository.
   - Install required Python packages: `pip install -r requirements.txt` (if there's a requirements file).

#### Running the Tests

- Execute the tests by running `pytest` from the command line in the project directory.
- Ensure the WebDriver is configured properly and available in the system PATH.

#### Test Scenario
- The test validates the login functionality of a web application using different sets of credentials.
- It uses Selenium to interact with the login page, enters credentials, and verifies successful login by asserting the resulting URL.

#### Notes
- Customize the test data in `test_login.py` to include additional test cases or login credentials.
- Update WebDriver paths or configurations as needed for your environment.
