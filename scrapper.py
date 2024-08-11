from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver import Driver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scrapper:

    def __init__(self, chrome: Driver):
        self.chrome = chrome

    def find_top_10_countries(self) -> list:
        self.chrome.load_page('https://olympics.com/')
        print("Página cargada\n")
        print("durmiendo 2s")
        sleep(1)

        print("seleccionando coockies")
        self.chrome.click_element('//*[@id="onetrust-accept-btn-handler"]')

        print("ir a tablas de medallas") 
        self.chrome.click_element('//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')

        #Hacer scroll hasta el elemento con Xpath = /html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[8]/div/div/div
        print("Haciendo scroll para cargar info necesaria")
        self.chrome.scroll_to_element('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[8]/div/div/div')

        countries_info = []
        quantity = 10    # Con hasta 8 funciona, pero 9 y 10 ya no se puede hasta hacer scroll
        
        #emotion-srm-1a32gjt /html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div
        #//*[@id="p2024-main-content"]/div[1]/div[2]/div[2]/div/div[2]
        #/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]
        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/'

        for index in range(1, quantity+1):
            print(index)

            country = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/div/span[3]')
            gold = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[1]')
            silver = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[2]')
            bronze = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[3]')
            total = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[4]')

            # Agregar los datos a la lista de países
            countries_info.append([country.text, gold.text, silver.text, bronze.text, total.text])
        return countries_info
        
    def find_top_3_sports_from(self, country: str) -> list:

        self.chrome.load_page('https://olympics.com/')
        print("Página cargada\n")
        print("durmiendo 2s")
        sleep(1)

        print("seleccionando coockies")
        self.chrome.click_element('//*[@id="onetrust-accept-btn-handler"]')

        print("ir a tablas de medallas") 
        self.chrome.click_element('//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')

        #Hacer scroll hasta el elemento con Xpath = /html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[8]/div/div/div
        # print("Haciendo scroll para cargar info necesaria")
        # self.chrome.scroll_to_element('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[8]/div/div/div')

        maximum_countries = 91

        index = 1
        jump_to_scroll = 8

        found = False
        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/'


        while index <= maximum_countries and not found:
            print("Indice: ", index)
            country_name = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/div/span[3]')
            # si index es divisible por 8, hacer scroll
            if index % jump_to_scroll == 0:
                self.chrome.scroll_to_element(f'{xpath_father}div[{index-1}]/div/div/div/div/span[3]')
                print("Haciendo scroll en while")
                print("Indice: ", index)
                sleep(1)

            if country_name.text.upper() == country.upper():
                found = True
                # info
                print("Encontrado")
                gold = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[1]')
                silver = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[2]')
                bronze = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[3]')
                total = self.chrome.find_element(f'{xpath_father}div[{index}]/div/div/div/span[4]')
                
                print(f"Oros: {gold.text}")
                print(f"Platas: {silver.text}")
                print(f"Bronces: {bronze.text}")
                print(f"Total: {total.text}")
                
                sleep(2)
                break
            index += 1

        return found


    def write_countries_csv(self, info: list, filename: str) -> None:
        header = "PAIS;OROS;PLATAS;BRONCES;TOTAL\n"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write(header)
            for country in info:
                file.write(f"{country[0].upper};{country[1]};{country[2]};{country[3]};{country[4]}\n")
            file.close()

        print(f"Se ha creado el archivo {filename}\n")