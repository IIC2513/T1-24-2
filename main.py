from driver import Driver 
from scrapper import Scrapper

def execute_scrapping():
    chrome_ = Driver()
    chrome_.initialize_driver()
    

    scrapper = Scrapper(chrome_)

    # Test 1
    countries = scrapper.find_top_10_countries()
    header = 'COUNTRY;GOLD;SILVER;BRONZE;TOTAL'
    scrapper.write_csv('top_10_countries.csv', header, countries)
    print(countries)
    
    # Test 2
    country = 'Chile'
    sports = scrapper.find_top_n_sports_from(country, 3)
    header = 'SPORT;GOLD;SILVER;BRONZE;TOTAL'
    scrapper.write_csv('top_n_sports_from_country.csv', header, sports)
    print(sports)

    # Test 3
    countries = ['United States of America', 'Chile', 'Japan']
    sport = 'Athletics'
    header = 'NAME;CATEGORY;MEDAL;COUNTRY;SPORT'
    results = scrapper.find_first_athlete_from(countries, sport)
    scrapper.write_csv('first_athlete_from_countries.csv', header, results) 
    print(results)

    # Test 4
    scrapper.find_by_total_medals(12)
    #scrapper.find_by_alphabetical_order(25)


    # scrapper.write_csv(sorted_info)
    
    chrome_.close()
    print("Fin del programa")

if __name__ == '__main__':
    execute_scrapping()






