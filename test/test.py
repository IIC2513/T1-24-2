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

    
    def test_find_top_medallists(self):

        info = self.scrapper.find_top_medallists("United States of America",'Artistic Gymnastics', 3)
        self.scrapper.write_medallists_csv(info, "top_medallists_country.csv")

        base_content = pd.read_csv("test/csv_base/top_medallists_country.csv")
        
        try:
            student_content = pd.read_csv("test/csv_student/top_medallists_country.csv")
        except:
            self.fail("No se creó el archivo top_medallists_country.csv")

        self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
        self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")   

    def test_find_top_medallists_gender(self):
        info = self.scrapper.find_top_medallists_gender("Female", 3)
        self.scrapper.write_medallists_csv(info, "top_medallists_female.csv")

        base_content = pd.read_csv("test/csv_base/top_medallists_female.csv") # ruta de los archivos solucion

        try:
            student_content = pd.read_csv("test/csv_student/top_medallists_female.csv") # ruta de los archivos estudiante
        except:
            self.fail("No se creó el archivo top_medallist_female.csv")

        self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
        self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")

    def test_find_countries_by_total_medals(self):
        self.scrapper.find_by_total_medals(3)

        base_content = pd.read_csv("test/csv_base/total_medals.csv")

        try:
            student_content = pd.read_csv("test/csv_student/total_medals.csv")
        except:
            self.fail("No se creó el archivo total_medals.csv")
        
        self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
        self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")
    
    def test_find_countries_by_alphabetical_order(self):
        self.scrapper.find_by_alphabetical_order(3)

        base_content = pd.read_csv("test/csv_base/alphabetical_order.csv")

        try:
            student_content = pd.read_csv("test/csv_student/alphabetical_order.csv")
        except:
            self.fail("No se creó el archivo alphabetical_order.csv")
        
        self.assertTrue(base_content.columns.equals(student_content.columns), "Header incorrecto")
        self.assertTrue(base_content.equals(student_content), "Los archivos no son iguales")
        

if __name__ == '__main__':
    unittest.main()
