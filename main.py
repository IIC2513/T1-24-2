from driver import Driver 
from scrapper import Scrapper

def execute_scrapping():
    chrome_ = Driver()
    chrome_.initialize_driver()
    chrome_.load_page('https://olympics.com/')

    scrapper = Scrapper(chrome_)
    scrapper.find_by_total_medals(12)
    #scrapper.find_by_alphabetical_order(25)
    # info_pokemons = scrapper.extract_pokemon_info(list_pokemons)
    # sorted_info = scrapper.sort_by_weight(info_pokemons)

    # scrapper.write_csv(sorted_info)

    chrome_.close()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()