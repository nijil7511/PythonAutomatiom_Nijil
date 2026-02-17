import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver



def test_properlogin_validation(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.XPATH, ".//input[contains(@id,'username')]").send_keys("student")
    driver.find_element(By.XPATH, ".//input[contains(@id,'password')]").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()


    try:
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[contains(.,'Logged In Successfully')]")))

        print("Pass – Logged In Sucessfully")
        assert True

    except:
        print("Unable to Log In. Test Failed!!!")
        assert False 
    time.sleep(10)
    driver.quit()

