from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Driver:

    def __init__(self, activate_sesion=False):
        self.options = Options()
        self.driver = None

    def initialize_driver(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def load_page(self, page: str) -> None:
        self.driver.get(page)
        sleep(60)

    def click_element(self, xpath: str) -> None:
        sleep(1)
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.click()

    def find_element(self, xpath: str) -> WebElement:
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def close(self) -> None:
        self.driver.quit()
        self.driver = None



if __name__ == '__main__':
    chrome = Driver()
    chrome.initialize_driver()
    chrome.load_page('https://www.google.com')