#!/usr/bin/env python
# coding: utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ConfigLoader import config_driver, config_searchbox


class Scraper:
    def __init__(self):
        self.PATH = config_driver['PATH']
        self.URL = config_driver['URL']
        self.searchword = config_searchbox['searchword']
        
    def activate(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        
        search = driver.find_element_by_name("Searchword")
        search.send_keys(self.searchword)
        search.send_keys(Keys.RETURN)
        
        self.list = []
        try:
            main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"Search3_Result")))
            items = main.find_elements_by_class_name("ss_book_box")
            for item in items:
                title = item.find_element_by_class_name("bo3").text
                price = item.find_element_by_class_name("ss_p2").text
                self.list.append({'Title':title, 'Price':price})
        finally:
            driver.quit()
            
        return self.list