from selenium.webdriver.chrome.webdriver import WebDriver


class MenuPage:
    driver: WebDriver

    def __init__(self, driver) -> None:
        self.driver = driver

    def click_hamburger_menu(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/nav/div[2]/button').click()

    def click_hamburger_home(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/nav/div[2]/button/ul/li[1]/a').click()

    def click_hamburger_company(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/nav/div[2]/button/ul/li[2]/a').click()

    def click_hamburger_profile(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/nav/div[2]/button/ul/li[3]/a').click()

    def click_hamburger_logout(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/nav/div[2]/button/ul/li[4]/a').click()
