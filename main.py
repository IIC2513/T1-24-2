from driver import Driver 
from scrapper import Scrapper

def execute_scrapping():
    chrome_ = Driver()
    chrome_.initialize_driver()
    chrome_.load_page('https://olympics.com/')

    #chrome_.click_element('//*[@id="onetrust-accept-btn-handler"]')

    chrome_.click_element('//*[@id="__next"]/div/header/div/div[1]/nav[1]/nav[2]/a[3]')



    # scrapper = Scrapper(chrome_)
    # info_pokemons = scrapper.extract_pokemon_info(list_pokemons)
    # sorted_info = scrapper.sort_by_weight(info_pokemons)

    # scrapper.write_csv(sorted_info)

    chrome_.quit_driver()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()