import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope='module')
def driver():
    # Initialize "Ritu" AppiumOptions for UiAutomator2
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platform_version = '14'  # Android version of my phone
    options.device_name = 'R9ZW90DBRXB'  # my device name from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  # sindabad app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity' 
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize the "Ritu" Appium WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_click_categories_and_back_buttons(driver):
    sleep(5)  

    try:
        # Locate the "Categories" button using accessibility ID
        categories_button = driver.find_element(By.ACCESSIBILITY_ID, 'Categories')
        categories_button.click()
        
        sleep(3)  # Wait for the action to complete
        
        
        
        # Locate and click the first "Back" button
        back_button = driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        back_button.click()
        
        sleep(3)  

       
        
     
        
        # Optionally verify if the previous screen was returned to
        # This might involve checking for the presence of a known element
        
        # Example check: Verify if the Categories button is still present
        categories_button = driver.find_element(By.ACCESSIBILITY_ID, 'Categories')
        assert categories_button.is_displayed(), "Categories button is not visible after pressing Back"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
