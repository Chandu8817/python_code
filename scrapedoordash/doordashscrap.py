# requirements python packages
# pip install BeautifulSoup4
# pip install pandas
# pip install selenium

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

category = []
item_name = []
description = []
prices = []
option_name = []
choice = []
choice_price = []

# driver.get(https://www.flipkart.com/televisions/pr?sid=ckf,czl&p[]=facets.screen_size%255B%255D("http://127.0.0.1:5500/compltedump.html")
# driver.get('http://127.0.0.1:5500/tst.html')
# URL = 'https://www.doordash.com/store/yafo-kitchen-charlotte-63003'
# content = requests.get(URL)

driver.get("https://www.doordash.com/store/yafo-kitchen-charlotte-63003")

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

items = soup.find_all("div", {"class": "Ieerz"})

# cate=soup.find_all("div", { "class" : "cXtuDl" })
# de=soup.find_all("span", { "class" : "kmvjNe" })

# print(items)


for a in items:
    name = a.find('span', {'class': 'izBrpx'})
    # desc = a.find("span", {"class": "kmvjNe"})
    price = a.find('span', {'class': 'iSLJhq'})

    if(name != None) and (price != None):
        item_name.append(name.text or name)
        # description.append(desc.text)
        prices.append(price.text or price)


df = pd.DataFrame({'Item Name': item_name, 'Price': prices})
df.to_csv('products1.csv', index=False, encoding='utf-8')

# df.to_csv('products.json')
# a = {'Item Name': item_name, 'Description':description,'Price': prices}
# df = pd.DataFrame.from_dict(a, orient='index')
# df.transpose()
#    -------------------
