from selenium.webdriver.common.by import By


class Form:

    option = (By.ID, "combo_facility")
    radios = (By.XPATH, "//input[@type='radio']")
    calendar = (By.ID, "txt_visit_date")
    comment = (By.ID, "txt_comment")
    submit = (By.ID, "btn-book-appointment")

    def __init__(self,driver):
        self.driver = driver

    def option_method(self):
        return self.driver.find_element(*Form.option)
    def radio_method(self):
        return self.driver.find_elements(*Form.radios)
    def calendar_method(self):
        return self.driver.find_element(*Form.calendar)
    def comment_menthod(self):
        return self.driver.find_element(*Form.comment)
    def submit_method(self):
        return self.driver.find_element(*Form.submit)