from driver import Driver 
from scrapper import Scrapper

def execute_scrapping():
    chrome = Driver()
    chrome.initialize_driver()
    scrapper = Scrapper(chrome)

    # Opciones para probar
    print("\nFUNCIONES DISPONIBLES:\n")
    print("     1. find_top_10_countries")
    print("     2. find_top_n_sports_from")
    print("     3. find_first_athlete_from")
    print("     4. find_top_medallists")
    print("     5. find_top_medallists_by_sport")
    print("     6. find_top_medallists_by_country")
    print("     7. find_top_medallists_by_sport_and_country")
    print("     0. Salir\n")
    
    n = int(input("Ingresa el número de la función que quieres probar: "))
    
    print("\nEjecutando la función", n)

    # TEST 1
    if n == 1:
        countries = scrapper.find_top_10_countries()
        header = 'COUNTRY;GOLD;SILVER;BRONZE;TOTAL'
        scrapper.write_csv('top_10_countries.csv', header, countries)
        print(countries)
    
    # TEST 2
    elif n == 2:

        country = 'Chile'
        sports = scrapper.find_top_n_sports_from(country, 3)
        header = 'SPORT;GOLD;SILVER;BRONZE;TOTAL'
        scrapper.write_csv('top_n_sports_from_country.csv', header, sports)
        print(sports)

    # TEST 3
    elif n == 3:
        countries = ['United States of America', 'Chile', 'Japan']
        sport = 'Athletics'
        header = 'NAME;CATEGORY;MEDAL;COUNTRY;SPORT'
        results = scrapper.find_first_athlete_from(countries, sport)
        scrapper.write_csv('first_athlete_from_countries.csv', header, results) 
        print(results)
    
    # TEST 4
    elif n in [4, 5, 6, 7]:
        print("Puedes poner aquí tu código para probar las funciones adicionales")
    
    elif n == 0:
        print("Saliendo del programa")

    else: 
        print("Número incorrecto")

    chrome.close()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()