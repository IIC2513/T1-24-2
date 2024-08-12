import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import unittest
import pandas as pd
from scrapper import Scrapper
from driver import Driver


class ScraperTest(unittest.TestCase):

    def setUp(self):
        chrome = Driver()
        chrome.initialize_driver()
        chrome.load_page('https://olympics.com/')
        self.scrapper = Scrapper(chrome)

    def test_top_10_countries(self):

        countries = self.scrapper.find_top_10_countries()
        header = 'COUNTRY;GOLD;SILVER;BRONZE;TOTAL'
        self.scrapper.write_csv('top_10_countries.csv', header, countries)

        base_content = pd.read_csv("test/csv_base/top_10_countries.csv")
        
        try:
            student_content = pd.read_csv("test/csv_student/top_10_countries.csv")
        except:
            self.fail("No se creó el archivo top_10_countries.csv")

        self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
        self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")   


    def test_top_n_sports_from(self):
            
            country = 'Chile'
            sports = self.scrapper.find_top_n_sports_from(country, 3)
            header = 'SPORT;GOLD;SILVER;BRONZE;TOTAL'
            self.scrapper.write_csv('top_n_sports_from_country.csv', header, sports)
    
            base_content = pd.read_csv("test/csv_base/top_n_sports_from_country.csv")
            
            try:
                student_content = pd.read_csv("test/csv_student/top_n_sports_from_country.csv")
            except:
                self.fail("No se creó el archivo top_n_sports_from_country.csv")
    
            self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
            self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")


    def test_first_athlete_from_countries(self):
            
            countries = ['United States of America', 'Chile', 'Japan']
            sport = 'Athletics'
            header = 'NAME;CATEGORY;MEDAL;COUNTRY;SPORT'
            results = self.scrapper.find_first_athlete_from(countries, sport)
            self.scrapper.write_csv('first_athlete_from_countries.csv', header, results) 
    
            base_content = pd.read_csv("test/csv_base/first_athlete_from_countries.csv")
            
            try:
                student_content = pd.read_csv("test/csv_student/first_athlete_from_countries.csv")
            except:
                self.fail("No se creó el archivo first_athlete_from_countries.csv")
    
            self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
            self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")
if __name__ == '__main__':
    unittest.main()

