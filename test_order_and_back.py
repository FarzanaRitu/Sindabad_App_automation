import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope='module')
def driver():
    # Initialize the AppiumOptions for UiAutomator2
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '14'  # Android version of your phone
    options.device_name = 'R9ZW90DBRXB'  # Your device name from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  # Replace with your app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity'  # Replace with the main activity
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize the Appium WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_click_orders_and_back_buttons(driver):
    sleep(5)  # Wait for the app to load

    try:
        # Locate the "Orders" button using accessibility ID
        orders_button = driver.find_element(By.ACCESSIBILITY_ID, 'Orders')
        orders_button.click()
        
        sleep(3)  # Wait for the action to complete
        
        # Optionally verify if the Orders screen is displayed
        # This could involve checking for the presence of a known element
        
        # Locate and"Ritu" click the "Back" button
        back_button = driver.find_element(By.ACCESSIBILITY_ID, 'Back')
        back_button.click()
        
        sleep(3)  # Wait for the action to complete
        
        # Optionally verify if the previous screen was returned to
        # This might involve checking for the presence of a known element
        
        # Example check: Verify if the Orders button is still present
        orders_button = driver.find_element(By.ACCESSIBILITY_ID, 'Orders')
        assert orders_button.is_displayed(), "Orders button is not visible after pressing Back"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
