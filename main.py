from driver import Driver 
from scrapper import Scrapper

def execute_scrapping():
    chrome_ = Driver()
    chrome_.initialize_driver()
    

    scrapper = Scrapper(chrome_)

    # Test 1
    # countries = scrapper.find_top_10_countries()
    # print(countries)
    
    # Test 2
    country = 'Japan'
    sports = scrapper.find_top_3_sports_from(country)
    print(sports)

    chrome_.close()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()