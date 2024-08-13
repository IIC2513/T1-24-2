from selenium.webdriver.common.by import By
from driver import Driver
from time import sleep

class Scrapper:

    def __init__(self, chrome: Driver):
        self.chrome = chrome

    def extract_top_10_countries(self) -> list:
        pass

    def extract_top_n_sports_from(self, country: str, n:int) -> list:
        pass

    def extract_first_athlete_from(self, countries: list, sport: str) -> list:
        pass

    def extract_by_total_medals(self, quantity: int) -> list:
        pass

    def extract_by_alphabetical_order(self, quantity: int) -> list:
        pass

    def extract_top_medallists(self, country: str, sport: str, quantity: int) -> list:
        pass
    
    def extract_top_medallists_gender(self, gender: str, quantity: int) -> list:
        pass
    
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