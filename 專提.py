# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:06:45 2020

@author: cis-user
"""

import csv
import requests
import pandas as pf
from io import StringIO
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import sys
import time,datetime


print('\n\n\n需有Chrome瀏覽器才能執行此程式!!!')

url = "https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2F%25E9%259D%25A0%25E5%258C%2597%25E9%2595%25B7%25E5%25AE%25982020-110310737083261%2F"
key_word="官校生 "


options = webdriver.ChromeOptions()                                     
options.add_argument('--ignore-certificate-errors')                                 
driver = webdriver.Chrome(chrome_options=options)                       
driver.get(url)


username="jeffrey5548@yahoo.com.tw"
password="as841118"

driver.find_element_by_id("email").click()
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").click()
driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()

driver.find_element_by_search("//div[@id='mount_0_0']/div/div/div/div[3]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div").click()
driver.find_element_by_search("(//input[@value=''])[3]").click()
driver.find_element_by_search(u"//input[@value='官校生']").clear()
driver.find_element_by_search(u"//input[@value='官校生']").send_keys(u"官校生")
driver.find_element_by_xpath("//li[@id='jsc_c_5s']/div/div/div/div[2]/span/span").click()








# page=0
# with open('666.csv','w+',newline='', encoding="utf-8-sig") as csvfile: 
#     writer = csv.writer(csvfile)
#     writer.writerow(('時間','標題','內文','連結'))

# page+=1
# html =driver.page_source
# sp=BeautifulSoup(html,"html.parser")
# search_a=sp.select("div.part_list_2 > h3 > a")
# search_class=sp.select("div.part_list_2 > h3 > em")
# search_span=sp.select("div.part_list_2 > h3 >span ")
        
# for i in range(2):
#     print(page)
#     print(search_span[i].text)
#     print(search_class[i].text,end=' ')
#     print(search_a[i].get('href'))
#     print(search_a[i].text,end=' ')

#             # writer.writerow([search_span[i].text,search_class[i].text,search_a[i].text,search_a[i].get('href')])

#     sleep(1)    


# driver.close()               #關閉瀏覽器


sys.exit