import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.fixture()
def environment_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    yield
    driver.close()


def test_verification_reg(environment_setup):
    driver.find_element(By.NAME, "email").send_keys("xyz@gmail.com")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234#Nr")
    driver.find_element(By.ID, "exampleCheck1").click()

    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Nitesh")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
    message = driver.find_element(By.CLASS_NAME, "alert ").text
    dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
    dropdown.select_by_visible_text("Male")
    dropdown.select_by_index(0)
    print(message)
    #static
    assert "Success! " in message
    driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello bhaiya  ")







    time.sleep(5)
    # id, Xpath, CSSselector, Name, classname, linktext