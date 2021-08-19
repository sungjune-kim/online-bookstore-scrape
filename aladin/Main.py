#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from scraper import Scraper

if __name__ == '__main__':
    scraper = Scraper()
    dblist = scraper.activate()
    
    bookdb = pd.DataFrame(dblist)