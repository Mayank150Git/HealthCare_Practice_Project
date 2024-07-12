from selenium.webdriver.common.by import By


class Login:

    def __init__(self,driver):
        self.driver = driver

    user_name = (By.ID, "txt-username")
    password = (By.ID, "txt-password")
    login_button = (By.ID, "btn-login")




    def user_name_method(self):
        #self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        return self.driver.find_element(*Login.user_name)

    def pass_method(self):
        return self.driver.find_element(*Login.password)

    def button_login(self):
        #self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        return self.driver.find_element(*Login.login_button)




