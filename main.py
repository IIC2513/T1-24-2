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
    # country = 'Chile'
    # sports = scrapper.find_top_n_sports_from(country, 3)
    # print(sports)

    # Test 3
    country = 'Chile'
    sport = 'Athletics'
    results = scrapper.find_first_athlete_from(country, sport)
    print(results)


    chrome_.close()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()