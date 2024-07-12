import time


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from HealthCare_FrameWork.Form_POM import Form
from POM.Login_POM import Login


@pytest.mark.usefixtures("setup")
class Test_HealthConseltation:

    def test_TC1(self):
        self.driver.find_element(By.LINK_TEXT, "Make Appointment").click()
        time.sleep(2)
    def test_TC2(self):
        login_obj = Login(self.driver)
        login_obj.user_name_method().send_keys("John Doe")
        login_obj.pass_method().send_keys("ThisIsNotAPassword")
        login_obj.button_login().click()
        time.sleep(2)
    def test_TC3(self):
        Form_Obj = Form(self.driver)

        Form_Obj.option_method().click()

        Select_options = Select(Form_Obj.option_method())
        Select_options.select_by_visible_text("Hongkong CURA Healthcare Center")

        Radio_options = Form_Obj.radio_method()

        for radio in Radio_options:
            if radio.get_attribute("value") == "Medicaid":
                radio.click()

        Form_Obj.calendar_method().send_keys("30/07/2024")
        time.sleep(2)

        Form_Obj.comment_menthod().send_keys("This is a dummy Text")

        Form_Obj.submit_method().click()
        time.sleep(3)
    def test_TC4(self):
        assert "Appointment Confirmation" in self.driver.find_element(By.XPATH, "//h2").text

