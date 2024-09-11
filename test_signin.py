import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@pytest.fixture(scope='module')
def driver():
    # Initialize the AppiumOptions for UiAutomator2
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '14'  # Android "Ritu" version of my phone
    options.device_name = 'R9ZW90DBRXB'  # My device name from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  #  app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity'  #  main activity
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize the Appium WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_click_signin_button(driver):
    sleep(5)  # Wait for the app to load

    try:
        try:
            # Try to locate the "Sign Up / Sign In" button by accessibility id (content-desc)
            signin_button = driver.find_element(By.ACCESSIBILITY_ID, 'Sign Up / Sign In')
            # Click the "Sign Up / Sign In" button
            signin_button.click()
            
            sleep(3) 
            
            # Re-locate the button to check visibility
            signin_button = driver.find_element(By.ACCESSIBILITY_ID, 'Sign Up / Sign In')
            assert signin_button.is_displayed(), "'Sign Up / Sign In' button is not visible"

        except NoSuchElementException:
            print("Sign Up / Sign In button is not present. The user might be already signed in or using guest mode.")
            
    except Exception as e:
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
