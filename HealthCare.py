import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_Object = Service()
driver = webdriver.Chrome(service = Service_Object)

#TC1:Hitting the URL
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()

#TC2: Navigating to the Appointment Page
driver.find_element(By.LINK_TEXT, "Make Appointment").click()

#TC3: Login
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID, "btn-login").click()
time.sleep(2)

#TC4: appointment details
driver.find_element(By.ID, "combo_facility").click()

Select_options = Select(driver.find_element(By.ID, "combo_facility"))
Select_options.select_by_visible_text("Hongkong CURA Healthcare Center")


Radio_options = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radio in Radio_options:
    if radio.get_attribute("value") == "Medicaid":
        radio.click()


driver.find_element(By.ID, "txt_visit_date").send_keys("30/07/2024")
time.sleep(2)

driver.find_element(By.ID, "txt_comment").send_keys("This is a dummy Text")

driver.find_element(By.ID, "btn-book-appointment").click()

#TC5: Validating the Confirmation
assert "Appointment Confirmation" in driver.find_element(By.XPATH, "//h2").text


