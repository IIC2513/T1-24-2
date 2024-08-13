from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

class Driver:

    def __init__(self):
        self.options = Options()
        self.driver = None

    def initialize_driver(self) -> None:
        # En caso que no cuenten con el driver de Chrome, deben descomentar esta linea
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def load_page(self, page: str) -> None:
        self.driver.get(page)
        sleep(5)

    def click_element(self, by: str, xpath: str) -> None:
        sleep(1)
        element = self.driver.find_element(by=by, value=xpath)
        element.click()

    def find_element(self, by: str, xpath: str) -> WebElement:
        return self.driver.find_element(by=by, value=xpath)
    
    def scroll_to_element(self, by: str, xpath: str) -> None:
        element = self.find_element(by, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(5)

    def close(self) -> None:
        self.driver.quit()
        self.driver = None

if __name__ == '__main__':
    chrome = Driver()
    chrome.initialize_driver()
    chrome.load_page('https://www.google.com')