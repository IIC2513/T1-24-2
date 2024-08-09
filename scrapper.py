from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver import Driver

class Scrapper:

    def __init__(self, chrome: Driver):
        self.chrome = chrome

    