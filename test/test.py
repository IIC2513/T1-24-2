import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import unittest
import pandas as pd
from scrapper import Scrapper
from driver import Driver

def test_id(id):
    def decorator(func):
        func._test_id = id
        return func
    return decorator


class ScraperTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Este método se ejecuta una sola vez antes de todos los tests
        cls.chrome = Driver()
        cls.chrome.initialize_driver()
        cls.scrapper = Scrapper(cls.chrome)

    def setUp(self):
        # Este método se ejecuta antes de cada test
        self.chrome.load_page('https://olympics.com/en/paris-2024/medals')

    @test_id('test_top_10_countries')
    def test_top_10_countries(self):
        self._test_id = 'test_top_10_countries'
        countries = self.scrapper.extract_top_10_countries()
        header = 'COUNTRY;GOLD;SILVER;BRONZE;TOTAL'
        self.scrapper.write_csv('top_10_countries.csv', header, countries)
        base_content = pd.read_csv('test/csv_base/top_10_countries.csv')
        
        try:
            student_content = pd.read_csv('test/csv_student/top_10_countries.csv')
        except:
            self.fail('No se creó el archivo top_10_countries.csv')

        self.assertTrue(base_content.equals(student_content), 'Los archivos no son iguales')   

    @test_id('test_top_n_spots_from')
    def test_top_n_sports_from(self):
        self._test_id = 'test_top_n_sports_from'
        country = 'Ukraine'
        sports = self.scrapper.extract_top_n_sports_from(country, 5)
        header = 'SPORT;GOLD;SILVER;BRONZE;TOTAL'
        self.scrapper.write_csv('top_n_sports_from_country.csv', header, sports)
        base_content = pd.read_csv('test/csv_base/top_n_sports_from_country.csv')
        
        try:
            student_content = pd.read_csv('test/csv_student/top_n_sports_from_country.csv')
        except:
            self.fail('No se creó el archivo top_n_sports_from_country.csv')

        self.assertTrue(base_content.equals(student_content), 'Los archivos no son iguales')

    @test_id('test_first_athlete_from_countries')
    def test_first_athlete_from_countries(self):
        self._test_id = 'test_first_athlete_from_countries'
        countries = ['Spain', 'Kazakhstan', 'Mexico', 'Dominican Republic', 'Chile', 'Puerto Rico']
        sport = 'Boxing'
        header = 'NAME;CATEGORY;MEDAL;COUNTRY;SPORT'
        results = self.scrapper.extract_first_athlete_from(countries, sport)
        self.scrapper.write_csv('first_athlete_from_countries.csv', header, results) 
        base_content = pd.read_csv('test/csv_base/first_athlete_from_countries.csv')
        
        try:
            student_content = pd.read_csv('test/csv_student/first_athlete_from_countries.csv')
        except:
            self.fail('No se creó el archivo first_athlete_from_countries.csv')

        self.assertTrue(base_content.equals(student_content), 'Los archivos no son iguales')
    
    @test_id('test_find_top_medallists')
    def test_find_top_medallists(self):
        self._test_id = 'test_find_top_medallists'
        header = 'NAME;GOLD;SILVER;BRONZE;TOTAL'
        country = 'Italy'
        sport = 'Shooting'
        results = self.scrapper.extract_top_medallists(country, sport, 5)
        self.scrapper.write_csv('top_medallists_sport_country.csv', header, results)
        base_content = pd.read_csv('test/csv_base/top_medallists_sport_country.csv')
        
        try:
            student_content = pd.read_csv('test/csv_student/top_medallists_sport_country.csv')
        except:
            self.fail('No se creó el archivo top_medallists_sport_country.csv')

        self.assertTrue(base_content.equals(student_content), 'Los archivos no son iguales')   

    @test_id('test_find_top_medallists_gender')
    def test_find_top_medallists_gender(self):
        self._test_id = 'test_find_top_medallists_gender'
        header = 'NAME;GOLD;SILVER;BRONZE;TOTAL'
        gender = 'Female'
        results = self.scrapper.extract_top_medallists_gender(gender, 5)
        self.scrapper.write_csv('top_medallists_female.csv', header, results)
        base_content = pd.read_csv('test/csv_base/top_medallists_female.csv') 

        try:
            student_content = pd.read_csv('test/csv_student/top_medallists_female.csv') 
        except:
            self.fail('No se creó el archivo top_medallists_female.csv')

        self.assertTrue(base_content.equals(student_content), 'Los archivos no son iguales')

    @test_id('test_extract_countries_by_total_medals')
    def test_extract_countries_by_total_medals(self):
        self._test_id = 'test_extract_countries_by_total_medals'
        countries = self.scrapper.extract_by_total_medals(3)
        header = 'COUNTRY;GOLDS;SILVERS;BRONZES;TOTAL'
        self.scrapper.write_csv('total_medals.csv', header, countries)
        base_content = pd.read_csv("test/csv_base/total_medals.csv")

        try:
            student_content = pd.read_csv('test/csv_student/total_medals.csv')
        except:
            self.fail('No se creó el archivo total_medals.csv')
        
        self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")
    
    @test_id('test_extract_countries_by_alphabetical_order')
    def test_extract_countries_by_alphabetical_order(self):
        self._test_id = 'test_extract_countries_by_alphabetical_order'
        countries = self.scrapper.extract_by_alphabetical_order(3)
        header = 'COUNTRY;GOLDS;SILVERS;BRONZES;TOTAL'
        self.scrapper.write_csv('alphabetical_order.csv', header, countries)
        base_content = pd.read_csv("test/csv_base/alphabetical_order.csv")

        try:
            student_content = pd.read_csv('test/csv_student/alphabetical_order.csv')
        except:
            self.fail('No se creó el archivo alphabetical_order.csv')
        
        self.assertTrue(base_content.equals(student_content), 'Los archivos no son iguales')

    def id(self):
        """Devuelve el ID personalizado si existe, o el ID por defecto."""
        return getattr(self, '_test_id', super().id())
        

if __name__ == '__main__':
    unittest.main()
