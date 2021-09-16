from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage:
    driver: WebDriver

    def __init__(self, driver) -> None:
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id("kc-login").click()

    def get_error_message(self):
        return self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/span[2]").text
