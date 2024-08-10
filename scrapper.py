from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver import Driver

class Scrapper:

    def __init__(self, chrome: Driver):
        self.chrome = chrome

    def find_by_total_medals(self, quantity: int) -> None:
        self.chrome.click_element('//*[@id="onetrust-accept-btn-handler"]')
        self.chrome.click_element('//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')
        self.chrome.click_element('//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]')  
        self.chrome.click_element('/html/body/div[4]/div[1]/div[2]')
        countries_info = []

        for index in (1, quantity+1):
            country_info = []
            country = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/div/span[3]')
            gold = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[1]')
            silver = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[2]')
            bronce = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[3]')
            total = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[4]')
            country_info.append(country.text)
            country_info.append(gold.text)
            country_info.append(silver.text)
            country_info.append(bronce.text)
            country_info.append(total.text)
            countries_info.append(country_info)
        
        self.write_countries_csv(countries_info, "total_medals.csv")


    def find_by_alphabetical_order(self, quantity: int) -> None:
        self.chrome.click_element('//*[@id="onetrust-accept-btn-handler"]')
        self.chrome.click_element('//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')
        self.chrome.click_element('//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]')  
        self.chrome.click_element('/html/body/div[4]/div[1]/div[3]')
        countries_info = []

        for index in (1, quantity+1):
            country_info = []
            country = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/div/span[3]')
            gold = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[1]')
            silver = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[2]')
            bronce = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[3]')
            total = self.chrome.find_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[{index}]/div/div/span[4]')
            country_info.append(country.text)
            country_info.append(gold.text)
            country_info.append(silver.text)
            country_info.append(bronce.text)
            country_info.append(total.text)
            countries_info.append(country_info)
        
        self.write_countries_csv(countries_info, "alphabetical_order.csv")

        

    def write_countries_csv(self, info: list, filename: str) -> None:
        header = "PAIS;OROS;PLATAS;BRONCES;TOTAL\n"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write(header)
            for country in info:
                file.write(f"{country[0].upper};{country[1]};{country[2]};{country[3]};{country[4]}\n")
            file.close()

        print(f"Se ha creado el archivo {filename}\n")