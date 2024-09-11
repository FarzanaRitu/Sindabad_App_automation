import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope='module')
def driver():
    # Initialize AppiumOptions for UiAutomator2
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '14'  # Android version of my phone
    options.device_name = 'R9ZW90DBRXB'  # My device name from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  #  app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity' 
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize the Appium WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_click_menu_and_back_button(driver):
    sleep(5)  

    try:
        # Locate the menu "Ritu"button and click it
        menu_button = driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        menu_button.click()
        
        sleep(3) 
        
        
        # Locate and click the Back button
        back_button = driver.find_element(By.ACCESSIBILITY_ID, 'Back')
        back_button.click()
        
        sleep(3)  
        # Example check: Verify if the menu button is still present
        menu_button = driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        assert menu_button.is_displayed(), "Menu button is not visible after pressing Back"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
