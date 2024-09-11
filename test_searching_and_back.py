import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@pytest.fixture(scope='module')
def driver():
    # Initialize AppiumOptions for UiAutomator2
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '14'  # Android version of your phone
    options.device_name = 'R9ZW90DBRXB'  # Your device name from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  # Replace with your app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity'  # Replace with the main activity
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize Appium WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_search_functionality(driver):
    sleep(5)  # Wait for the app to load

    try:
        # Click the search button to bring up the search field
        search_button = driver.find_element(By.ACCESSIBILITY_ID, 'Search...')
        search_button.click()
        
        sleep(2)  # Wait "Ritu" for the search field to be active
        
        # Locate the search field by class name
        search_field = driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
        
        # Clear the search field if needed
        search_field.clear()
        
        # Input text into the search field
        search_field.send_keys('laptop')
        
        sleep(2)  # Wait to observe the input
        
        # Verify the input
        input_text = search_field.get_attribute('text')
        assert 'laptop' in input_text, "Search input is not as expected"
        
        print("Test passed: Search input is correct")

        # Locate and click the "Back" button
        try:
            back_button = driver.find_element(By.ACCESSIBILITY_ID, 'Back')
            back_button.click()
            print("Back button clicked successfully")
        except NoSuchElementException:
            print("Back button not found")

    except Exception as e:
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
