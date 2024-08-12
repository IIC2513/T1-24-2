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
        
    def find_top_n_sports_from(self, country: str, n:int) -> list:
        # De momento solo funciona para los primeros 8 países por temas de scroll.
        self.chrome.load_page('https://olympics.com/')
        print("Página cargada\n")
        print("durmiendo 2s")
        sleep(1)

        print("seleccionando coockies")
        self.chrome.click_element('//*[@id="onetrust-accept-btn-handler"]')

        print("ir a tablas de medallas") 
        self.chrome.click_element('//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')

        print("Click en botón de filtro")
        self.chrome.click_element('/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/button')

        print("Click en filtro pais")
        self.chrome.click_element('/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/button/div[2]')

        # Tratar de buscar el país, y si no se encuentra, imprimir que no se encontró:
        print("Click en el país")
        self.chrome.click_element(f"//div[@role='option' and contains(text(), '{country}')]")

        print("Click en botón +")
        self.chrome.click_element(f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div') # click en boton +

        print("Esperando 5s")
        sleep(5)
        
        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]'

        sports_info = []
        quantity = n

        for i in range(1, quantity+1):
            try:
                print("Deporte ", i)
                sport = self.chrome.find_element(f'{xpath_father}/div[{i}]/span[1]')
                gold = self.chrome.find_element(f'{xpath_father}/div[{i}]/span[2]')
                silver = self.chrome.find_element(f'{xpath_father}/div[{i}]/span[3]')
                bronze = self.chrome.find_element(f'{xpath_father}/div[{i}]/span[4]')
                total = self.chrome.find_element(f'{xpath_father}/div[{i}]/span[5]')
                
                sports_info.append([sport.text, gold.text, silver.text, bronze.text, total.text])
            except Exception as e:
                print(f"No se encontró el deporte {i} para el país {country}. Error: {e}")
                break

        return sports_info


    def write_countries_csv(self, info: list, filename: str) -> None:
        header = "PAIS;OROS;PLATAS;BRONCES;TOTAL\n"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            file.write(header)
            for country in info:
                file.write(f"{country[0].upper};{country[1]};{country[2]};{country[3]};{country[4]}\n")
            file.close()

        print(f"Se ha creado el archivo {filename}\n")