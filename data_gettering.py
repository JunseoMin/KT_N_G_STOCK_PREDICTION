#web scrapping
import pandas as pd
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

url="https://finance.naver.com/item/sise.naver?code=033780"

#requests로 html다운로드
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
price_type_tag=soup.find_all("th",attrs={"class":"title"})
price_tag=soup.find_all("td",attrs={"class":"num"})
#find method이용해서 html원하는 값 추출
#find_all("tag",attrs={"classtype":"class"})
#find method는 맨 처음나온 하나의 값만 반환
#finde_all method는 모든 값 반환

for priceTTag in price_type_tag:
    print(priceTTag.get_text())
#dictionary name

for priceTag in price_tag:
    print(priceTag.get_text())
#dictionary parameter

#bs객체로 받아서 numpy배열로 만든 후 csv로 손질할것.
