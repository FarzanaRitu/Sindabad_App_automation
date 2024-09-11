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
    options.platform_version = '14'  # Android version of My phone
    options.device_name = 'R9ZW90DBRXB'  # My device name "Ritu"from 'adb devices'
    options.app_package = 'com.zgvl.android.sindabad'  #  app package
    options.app_activity = 'com.zgvl.android.sindabad.MainActivity'  # main activity
    options.automation_name = 'UiAutomator2'
    options.no_reset = True

    # Initialize Appium WebDriver "Ritu"
    driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield driver
    driver.quit()

def test_summer_collection_and_back(driver):
    sleep(5)  

    try:
        
        try:
            summer_collection = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.widget.ImageView[1]')
            summer_collection.click()
            print("Summer Collection item clicked successfully")
        except NoSuchElementException:
            print("Summer Collection item not found")
        
        sleep(3)  

        # Click the "Back" button
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
