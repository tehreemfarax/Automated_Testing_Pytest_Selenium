import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to set up and tear down the WebDriver
@pytest.fixture
def browser():
    # Set up the WebDriver (you may need to change the executable_path based on your system and browser)
    driver = webdriver.Chrome()
    yield driver
    # Tear down the WebDriver after the test
    driver.quit()

# Fixture to provide login credentials
@pytest.fixture(params=[
    {"username": "student", "password": "Password123"},
    {"username": "your_username2", "password": "your_password2"}
])
def login_credentials(request):
    return request.param

# Test function with parameterization
def test_successful_login(browser, login_credentials):
    # Navigate to the login page
    browser.get("https://practicetestautomation.com/practice-test-login/")

    # Find the username, password input fields, and submit button
    username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
    submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "submit")))

    # Enter credentials
    username_input.send_keys(login_credentials["username"])
    password_input.send_keys(login_credentials["password"])

    # Click the submit button
    submit_button.click()

    # Wait for the page to load
    WebDriverWait(browser, 5).until(EC.url_to_be("https://practicetestautomation.com/logged-in-successfully/"))

    # Assert that the current URL is the expected URL after successful login
    assert browser.current_url == "https://practicetestautomation.com/logged-in-successfully/"
