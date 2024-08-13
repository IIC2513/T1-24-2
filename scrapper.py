from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver import Driver
from time import sleep



class Scrapper:

    def __init__(self, chrome: Driver):
        self.chrome = chrome

    def find_top_10_countries(self) -> list:
        self.chrome.load_page('https://olympics.com/')
        print("Página cargada\n")
        print("durmiendo 1s")
        sleep(1)

        print("seleccionando coockies")
        # trata de aceptar coockies si existe:
        try:
            self.chrome.click_element(By.XPATH, By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        except:
            pass

        print("ir a tablas de medallas") 
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')

        #Hacer scroll hasta el elemento con Xpath = /html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[8]/div/div/div
        print("Haciendo scroll para cargar info necesaria")
        self.chrome.scroll_to_element('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[8]/div/div/div')

        countries_info = []
        quantity = 10    # Con hasta 8 funciona, pero 9 y 10 ya no se puede hasta hacer scroll
        
        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/'

        for index in range(1, quantity+1):
            print(index)

            country = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/div/span[3]')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[2]')
            bronze = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[4]')

            # Agregar los datos a la lista de países
            countries_info.append([country.text, gold.text, silver.text, bronze.text, total.text])
        return countries_info
        
    def find_top_n_sports_from(self, country: str, n:int) -> list:
        # De momento solo funciona para los primeros 8 países por temas de scroll.
        self.chrome.load_page('https://olympics.com/')
        print("Página cargada\n")
        print("durmiendo 1s")
        sleep(1)

        print("seleccionando coockies")
        # trata de aceptar coockies si existe:
        try:
            self.chrome.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        except:
            pass

        print("ir a tablas de medallas") 
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')

        print("Click en botón de filtro")
        self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/button')

        print("Click en filtro pais")
        self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/button/div[2]')

        # Tratar de buscar el país, y si no se encuentra, imprimir que no se encontró:
        print("Click en el país")
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{country}')]")

        print("Click en botón +")
        self.chrome.click_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div') # click en boton +

        print("Esperando 1s")
        sleep(1)
        
        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]'

        sports_info = []
        quantity = n

        for i in range(1, quantity+1):
            try:
                print("Deporte ", i)
                sport = self.chrome.find_element(By.XPATH, f'{xpath_father}/div[{i}]/span[1]')
                gold = self.chrome.find_element(By.XPATH, f'{xpath_father}/div[{i}]/span[2]')
                silver = self.chrome.find_element(By.XPATH, f'{xpath_father}/div[{i}]/span[3]')
                bronze = self.chrome.find_element(By.XPATH, f'{xpath_father}/div[{i}]/span[4]')
                total = self.chrome.find_element(By.XPATH, f'{xpath_father}/div[{i}]/span[5]')
                
                sports_info.append([sport.text, gold.text, silver.text, bronze.text, total.text])
            except:
                break

        return sports_info

    def find_first_athlete_from(self, countries: list, sport: str) -> list:
        # De momento solo funciona para los primeros 8 países por temas de scroll.
        self.chrome.load_page('https://olympics.com/')
        print("Página cargada\n")
        print("durmiendo 2s")
        sleep(1)

        print("seleccionando coockies")
        # trata de aceptar coockies si existe:
        try:
            self.chrome.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        except:
            pass


        print("ir a tablas de medallas") 
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')

        print("Click en botón de filtro")
        self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/button')
        
        athlete_info = []
        
        for country in countries:
            print(f'País a buscar: {country}')


            print("Click en filtro pais")
            self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/button/div[2]')

            # Tratar de buscar el país, y si no se encuentra, imprimir que no se encontró:
            print("Click en el país")
            self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{country}')]")

            print("Click en filtro deporte")
            self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[3]/button')

            # Tratar de buscar el país, y si no se encuentra, imprimir que no se encontró:
            print("Click en el deporte")
            self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{sport}')]")

            try:
                print("Click en botón +")
                self.chrome.click_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div') # click en boton +

                print("Click en segundo botón +")
                self.chrome.click_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]')

            except:
                pass

            print("Esperando 1s")
            sleep(1)
                    
            # Extraer información
            try:
                name = self.chrome.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a').text
                category = self.chrome.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/a').text
                medal = self.chrome.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/span').text

                print("Categoría: ", category)
                print("Nombre: ", name)
                print("Medalla: ", medal)

                athlete_info.append([name, category, medal, country, sport])

            except:
                pass
        
        return athlete_info
        
    def find_by_total_medals(self, quantity: int) -> None:
        self.chrome.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')
        self.chrome.driver.execute_script("window.scrollTo(0, 100);")
        self.chrome.click_element(By.XPATH, '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]')
        sleep(5)  
        self.chrome.click_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]')
        countries_info = []

        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/'
        self.chrome.driver.execute_script("window.scrollTo(0, 400);")

        for index in range(1, quantity+1):
            country_info = []
            sleep(5)
            country = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/div/span[3]')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[2]')
            bronze = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[4]')
            country_info.append(country.text)
            country_info.append(gold.text)
            country_info.append(silver.text)
            country_info.append(bronze.text)
            country_info.append(total.text)
            countries_info.append(country_info)
        
        self.write_countries_csv(countries_info, "test/csv_student/total_medals.csv")

    def find_by_alphabetical_order(self, quantity: int) -> None:
        self.chrome.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')
        self.chrome.driver.execute_script("window.scrollTo(0, 100);")
        self.chrome.click_element(By.XPATH, '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]')
        sleep(5)  
        self.chrome.click_element(By.XPATH, '/html/body/div[4]/div[1]/div[3]')
        countries_info = []

        xpath_father = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/div/div[2]/'
        self.chrome.driver.execute_script("window.scrollTo(0, 400);")

        for index in range(1, quantity+1):
            country_info = []
            sleep(5)
            country = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/div/span[3]')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[2]')
            bronze = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_father}div[{index}]/div/div/div/span[4]')
            country_info.append(country.text)
            country_info.append(gold.text)
            country_info.append(silver.text)
            country_info.append(bronze.text)
            country_info.append(total.text)
            countries_info.append(country_info)
        
        self.write_countries_csv(countries_info, "test/csv_student/alphabetical_order.csv")

    def find_top_medallists(self, country: str, sport: str, quantity: int) -> list:
        self.chrome.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')
        self.chrome.click_element(By.XPATH, '//*[@id="paris2024-header"]/div/div[3]/a[2]')
        self.chrome.click_element(By.XPATH, '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/button')
        self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/button')
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{country}')]")
        self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[3]/button')
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{sport}')]")

        sleep(2)

        medallists_info = []

        for i in range(1, quantity + 1):
            medallist = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/div[2]/span')
            gold = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[2]')
            bronze =  self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[3]')
            total = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[4]')
            medallists_info.append([medallist.text, gold.text, silver.text, bronze.text, total.text])

        return medallists_info
    
    def find_top_medallists_gender(self, gender: str, quantity: int) -> list:

        self.chrome.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        self.chrome.click_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')
        self.chrome.click_element(By.XPATH, '//*[@id="paris2024-header"]/div/div[3]/a[2]')
        self.chrome.click_element(By.XPATH, '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/button')
        self.chrome.click_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[1]/div/div[2]/div/div[7]/button')

        self.chrome.click_element(By.XPATH, f"//div[@role='option' and text()='{gender}']")

        sleep(2)

        medallists_info = []

        for i in range(1, quantity + 1):
            medallist = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/div[2]/span')
            gold = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[2]')
            bronze =  self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[3]')
            total = self.chrome.find_element(By.XPATH, f'/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[1]/span[4]')
            medallists_info.append([medallist.text, gold.text, silver.text, bronze.text, total.text])


        return medallists_info

    # Función genérica para escribir en un archivo CSV
    def write_csv(self, filename: str, header: str, info: list) -> None:
        with open(f'test/csv_student/{filename}', mode='w', newline='', encoding='utf-8') as file:
            # Escribir el encabezado
            file.write(header + "\n")

            # Contar cuántas columnas hay en el encabezado
            num_columns = len(header.split(";"))

            # Escribir cada fila de datos
            for data in info:
                # Asegurarse de que el número de elementos en la fila coincide con el número de columnas
                row_data = ";".join(str(data[i]) if i < len(data) else "" for i in range(num_columns))
                file.write(row_data + "\n")

        print(f"Se ha creado el archivo {filename}\n")