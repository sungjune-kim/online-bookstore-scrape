#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install selenium


# In[29]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import json
from pymongo import MongoClient


# In[30]:


#ubuntuPATH = '/home/cvlab/chromedriver'
macPATH = '/Users/sungjunekim/Downloads/chromedriver'

driver = webdriver.Chrome(macPATH)
driver.get("https://www.aladin.co.kr/home/welcome.aspx")

search = driver.find_element_by_name("SearchWord")
search.send_keys("deep learning")
search.send_keys(Keys.RETURN)

list = []

try:
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"Search3_Result")))
    items = main.find_elements_by_class_name("ss_book_box")
    
    for item in items:
        title = item.find_element_by_class_name("bo3").text #for loop 안에 있기 때문에 elements가 아닌 element 사용!!!
        price = item.find_element_by_class_name("ss_p2").text
        #list.append({'Title':title, 'Price':price})
        print(f"{title} --------- {price}")

finally:
    driver.quit()


# In[31]:


#client = MongoClient('localhost',27017)
#db = client.aladin
#bookinfo = db.bookinfo


# In[32]:


#bookinfo.insert_many(list)


# In[33]:


#for item in bookinfo.find():
#    print(item)


# In[36]:


#bookDB = pd.DataFrame(list)


# In[37]:


#bookDB


# In[ ]:




