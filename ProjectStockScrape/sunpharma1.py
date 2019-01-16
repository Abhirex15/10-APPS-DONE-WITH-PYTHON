import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/O

import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
from fastnumbers import isfloat
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool
import bs4

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylib import tidy_document # for tidying incorrect html

sns.set_style('whitegrid')
#%matplotlib inline
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def ffloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ")[0].replace(',','').replace('%',''),
                      default=np.nan)

def ffloat_list(string_list):
    return list(map(ffloat,string_list))

def remove_multiple_spaces(string):
    if type(string)==str:
        return ' '.join(string.split())
    return string

response = requests.get("https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI", timeout=240)
response.status_code
response.content

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url, timeout=240)
response.status_code
response.json()

content = response.json()
content.keys()


def request_with_check(url):
    page_response = requests.get(url, timeout=240)
    status = page_response.status_code
    if status>299:
        raise AssertionError("page content not found, status: %s"%status)
    return page_response

request_with_check("https://www.google.co.in/")

from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")

page_response = requests.get("https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI", timeout=240)
page_content = BeautifulSoup(page_response.content, "html.parser")
HTML(str(page_content.find("h1")))

print(HTML(str(page_content.find("div",attrs={'id':"content_full"}))))


page_response = requests.get("https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI", timeout=240)
page_content = BeautifulSoup(page_response.content, "html.parser")
price_div = page_content.find("div",attrs={"id":'b_changetext'})
HTML(str(price_div))

list(price_div.children)

def get_children(html_content):
    children = list()
    for item in html_content.children:
        if type(item)==bs4.element.Comment:
            continue
        if type(item)==bs4.element.Tag or len(str(item).replace("\n","").strip())>0:
            children.append(item)

    return children

get_children(price_div)


    
