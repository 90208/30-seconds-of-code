# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:50:56 2020

@author: chenlw
"""
import csv
import requests
import pandas as pf
from io import StringIO
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import sys
import time,datetime


print('\n\n\n需有Chrome瀏覽器才能執行此程式!!!')

url = "https://www.ettoday.net/news/news-list-2020-12-12-0.htm"
key_word="陸軍官校 "


options = webdriver.ChromeOptions()                                     
options.add_argument('--ignore-certificate-errors')                                 
driver = webdriver.Chrome(chrome_options=options)                       
driver.get(url)
page=0
with open('666.csv','w+',newline='', encoding="utf-8-sig") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(('時間','標題','內文','連結'))
    now_date = time.strftime("%Y%m%d")
    day=int(now_date[-2:])


    n_days1=2  #要幾天

    for i in range(0,n_days1+1):
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=i)
        n_days = now-delta
        now1=now.strftime('%Y%m%d')
    
    
        n_days1=n_days.strftime('%Y%m%d')
        
   

        # driver.get("https://www.ettoday.net/news/news-list-2020-12-12-0.htm")
        driver.find_element_by_id("selY").click()
        Select(driver.find_element_by_id("selY")).select_by_visible_text("2020")
        driver.find_element_by_id("selY").click()
        driver.find_element_by_id("selM").click()
        Select(driver.find_element_by_id("selM")).select_by_visible_text("12")
        driver.find_element_by_id("selM").click()
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text(n_days1[-2:])
        driver.find_element_by_id("selD").click()
        driver.find_element_by_id("button").click()
    
        page+=1
        html =driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_a=sp.select("div.part_list_2 > h3 > a")
        search_class=sp.select("div.part_list_2 > h3 > em")
        search_span=sp.select("div.part_list_2 > h3 >span ")
        
        for i in range(2):
            print(page)
            print(search_span[i].text)
            print(search_class[i].text,end=' ')
            print(search_a[i].get('href'))
            print(search_a[i].text,end=' ')

            writer.writerow([search_span[i].text,search_class[i].text,search_a[i].text,search_a[i].get('href')])

        sleep(1)    


# driver.close()               #關閉瀏覽器


sys.exit

