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
    options.platform_version = '14'  # Android version of my phone
    options.device_name = 'R9ZW90DBRXB'  # My device name from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  #  app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity'  # main activity
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize  Appium WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_exit_button(driver):
    sleep(5)  

    try:
        try:
            # Locate the Exit button by accessibility id "Ritu"
            exit_button = driver.find_element(By.ACCESSIBILITY_ID, 'Exit')
            exit_button.click()
            
            sleep(2)  
            
            # Optionally, verify if the app closed or navigated away
            try:
                # Attempt to interact with a known element (this might fail if the app is closed)
                driver.find_element(By.ACCESSIBILITY_ID, 'SomeKnownElement')
                assert False, "Test failed: App did not close"
            except Exception:
                assert True, "Test passed: App closed or navigated away"
                
        except NoSuchElementException:
            pass  # If the Exit button is not present, do nothing
            
    except Exception as inner_e:
        pytest.fail(f"Interaction failed: {inner_e}")

if __name__ == "__main__":
    pytest.main()
