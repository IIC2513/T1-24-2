from selenium.webdriver.common.by import By
from driver import Driver
from time import sleep

class Scrapper:

    def __init__(self, chrome: Driver):
        self.chrome = chrome

    def __accept_cookies(self):
        try:
            sleep(1)
            self.chrome.click_element(By.ID, 'onetrust-accept-btn-handler')
        except:
            pass
        
    def extract_top_10_countries(self) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals')
        self.__accept_cookies()

        xpath_list = '//*[@data-test-id="virtuoso-item-list"]'
        xpath_data_span = 'div/div/div/span'
        self.chrome.scroll_to_element(By.XPATH, xpath_list)

        countries_info = []
        quantity = 10    
    
        for index in range(1, quantity+1):
            country = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/div/{xpath_data_span}[3]')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[2]')
            bronze = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[4]')

            countries_info.append([country.text, gold.text, silver.text, bronze.text, total.text])
        return countries_info
        
    def extract_top_n_sports_from(self, country: str, n:int) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals')
        self.__accept_cookies()

        xpath_filter_button = '//*[@data-testid="extraSettings"]'
        relative_xpath_filter_country =  '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[2]/div/div[1]/button'
        xpath_button_plus = '//*[@data-testid="expand-discipline-icon"]'
        xpath_body_table = '//*[@data-testid="noc-row"]/div[2]'

        self.chrome.click_element(By.XPATH, xpath_filter_button)
        self.chrome.click_element(By.XPATH, relative_xpath_filter_country)
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{country}')]")
        self.chrome.click_element(By.XPATH, xpath_button_plus)
        
        sports_info = []
        quantity = n

        for i in range(1, quantity+1):
            try:
                sport = self.chrome.find_element(By.XPATH, f'{xpath_body_table}/div[{i}]/span[1]')
                gold = self.chrome.find_element(By.XPATH, f'{xpath_body_table}/div[{i}]/span[2]')
                silver = self.chrome.find_element(By.XPATH, f'{xpath_body_table}/div[{i}]/span[3]')
                bronze = self.chrome.find_element(By.XPATH, f'{xpath_body_table}/div[{i}]/span[4]')
                total = self.chrome.find_element(By.XPATH, f'{xpath_body_table}/div[{i}]/span[5]')
                
                sports_info.append([sport.text, gold.text, silver.text, bronze.text, total.text])
            except:
                break

        return sports_info

    def extract_first_athlete_from(self, countries: list, sport: str) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals')
        self.__accept_cookies()

        xpath_filter_button = '//*[@data-testid="extraSettings"]'
        relative_xpath_filter_country =  '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[2]/div/div[1]/button'
        relative_xpath_filter_sport = '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[2]/div/div[3]'
        xpath_button_plus = '//*[@data-testid="expand-discipline-icon"]'
        xpath_button_plus_2 = '//*[@data-testid="expand-medal-winners-icon"]'
        xpath_sport_info = '//*[@id="p2024-main-content"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]'

        self.chrome.click_element(By.XPATH, xpath_filter_button)
        
        athlete_info = []
        
        for country in countries:
            self.chrome.click_element(By.XPATH, relative_xpath_filter_country)
            self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{country}')]")
            self.chrome.click_element(By.XPATH, relative_xpath_filter_sport)
            self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{sport}')]")

            try:
                self.chrome.click_element(By.XPATH, xpath_button_plus)
                self.chrome.click_element(By.XPATH, xpath_button_plus_2)
            except:
                continue

            try:
                name = self.chrome.find_element(By.XPATH,     f'{xpath_sport_info}/div[1]/div/a')
                category = self.chrome.find_element(By.XPATH, f'{xpath_sport_info}/div[1]/a')
                medal = self.chrome.find_element(By.XPATH,    f'{xpath_sport_info}/div[2]/div/span')
                athlete_info.append([name.text, category.text, medal.text, country, sport])

            except:
                pass
        
        return athlete_info
        
    def extract_by_total_medals(self, quantity: int) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals')
        self.__accept_cookies()

        xpath_filter_by_button = '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/button'
        xpath_key_total_medals = '//*[@data-key="Total Medals"]'
        xpath_list = '//*[@data-test-id="virtuoso-item-list"]'
        xpath_data_span = 'div/div/div/span'

        self.chrome.click_element(By.XPATH, xpath_filter_by_button)
        self.chrome.click_element(By.XPATH, xpath_key_total_medals)
        self.chrome.scroll_to_element(By.XPATH, xpath_list)
        countries_info = []

        for index in range(1, quantity+1):
            country = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/div/{xpath_data_span}[3]')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[2]')
            bronze = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[4]')

            countries_info.append([country.text, gold.text, silver.text, bronze.text, total.text])
        
        return countries_info

    def extract_by_alphabetical_order(self, quantity: int) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals')
        self.__accept_cookies()

        xpath_filter_by_button = '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/button'
        xpath_key_total_medals = '//*[@data-key="Alphabetical"]'
        xpath_list = '//*[@data-test-id="virtuoso-item-list"]'
        xpath_data_span = 'div/div/div/span'

        self.chrome.click_element(By.XPATH, xpath_filter_by_button)
        self.chrome.click_element(By.XPATH, xpath_key_total_medals)
        self.chrome.scroll_to_element(By.XPATH, xpath_list)
        countries_info = []

        for index in range(1, quantity+1):
            country = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/div/{xpath_data_span}[3]')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[2]')
            bronze = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{index}]/{xpath_data_span}[4]')

            countries_info.append([country.text, gold.text, silver.text, bronze.text, total.text])
        
        return countries_info

    def extract_top_medallists(self, country: str, sport: str, quantity: int) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals/medallists')
        self.__accept_cookies()

        xpath_filter_button = '//*[@data-testid="extraSettings"]'
        relative_xpath_filter_country =  '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[2]/div/div[1]/button'
        relative_xpath_filter_sport = '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[2]/div/div[3]'
        xpath_list = '//*[@data-test-id="virtuoso-item-list"]'
        xpath_data_text = 'div/div/div[1]'

        self.chrome.click_element(By.XPATH, xpath_filter_button)
        self.chrome.click_element(By.XPATH, relative_xpath_filter_country)
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{country}')]")
        self.chrome.click_element(By.XPATH, relative_xpath_filter_sport)
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and contains(text(), '{sport}')]")
        self.chrome.scroll_to_element(By.XPATH, xpath_list)

        medallists_info = []
        for i in range(1, quantity + 1):
            medallist = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/div[2]/span')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[2]')
            bronze =  self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[4]')
            medallists_info.append([medallist.text, gold.text, silver.text, bronze.text, total.text])

        return medallists_info
    
    def extract_top_medallists_gender(self, gender: str, quantity: int) -> list:
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals/medallists')
        self.__accept_cookies()

        xpath_filter_button = '//*[@data-testid="extraSettings"]'
        relative_xpath_filter_gender =  '//*[@id="p2024-main-content"]/div[1]/div[1]/div/div[2]/div/div[7]/button'
        xpath_list = '//*[@data-test-id="virtuoso-item-list"]'
        xpath_data_text = 'div/div/div[1]'

        self.chrome.click_element(By.XPATH, xpath_filter_button)
        self.chrome.click_element(By.XPATH, relative_xpath_filter_gender)
        self.chrome.click_element(By.XPATH, f"//div[@role='option' and text()='{gender}']")
        self.chrome.scroll_to_element(By.XPATH, xpath_list)

        medallists_info = []
        for i in range(1, quantity + 1):
            medallist = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/div[2]/span')
            gold = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[1]')
            silver = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[2]')
            bronze =  self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[3]')
            total = self.chrome.find_element(By.XPATH, f'{xpath_list}/div[{i}]/{xpath_data_text}/span[4]')
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

if __name__ == '__main__':
    chrome = Driver()
    chrome.initialize_driver()
    scrapper = Scrapper(chrome)
    header = 'NAME;GOLD;SILVER;BRONZE;TOTAL'
    gender = 'Female'
    results = scrapper.extract_top_medallists_gender(gender, 5)
    scrapper.write_csv('top_medallists_female.csv', header, results)