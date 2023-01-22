from selenium.webdriver.common.by import By

class LoginPage:
    textbox_email_name = "Email"
    textbox_password_name = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    # Enter Email
    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.textbox_email_name).clear()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email)

    # Enter Password
    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    # Click Login Button
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    # Click Logout
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()