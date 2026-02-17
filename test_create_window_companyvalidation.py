from venv import create

import pytest
import time

import select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver():

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver

def test_window(driver):
    driver.get("C:\\Users\\NijilMeethale\\PycharmProjects\\PythonAutomatiom_Nijil\\TestWebSite.html")
    #driver.find_element(By.ID,"company").send_keys("Nijil&CO")
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div/div[5]/button[2]").click()
    text = driver.find_element(By.ID,'companyErr')
    time.sleep(2)
    #driver.switch_to.alert.accept()


    time.sleep(2)
    driver.quit()

    if text == "Company required":
        print("Company Mandatory Validation Successfull")
        assert False, "Validation Displayed!"
    else:
        print("Company Mandatory Validation Successfull")
        assert True, "Validation Not Displayed!"
        time.sleep(2)
        driver.quit()
