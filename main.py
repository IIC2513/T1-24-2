from driver import Driver 
from scrapper import Scrapper

def execute_scrapping():
    chrome_ = Driver()
    chrome_.initialize_driver()
    

    scrapper = Scrapper(chrome_)

    countries = scrapper.find_top_10_countries()
    
    print(countries)


    chrome_.close()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()