# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


DY_OFFICE_URL = 'https://www.daily-yamazaki.jp/new/'

DY_PRODUCT_IMAGE = 'pic'

DY_DETAIL_LIST = 'c-top-products__inner-list'

DY_DETAIL_NAME = 'ttl'

DY_DETAIL_PRICE = 'tax'

DY_DETAIL_DATE = 'c-title03'

DY_DETAIL_DATE_LIST = []

DY_PRODUCT_LIST = []

def get_product_information():
    get_requests = requests.get(DY_OFFICE_URL)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    product_detailList = beasutiful_soup.find_all("div", attrs={'class': DY_DETAIL_LIST})
    for detailIndex ,detail in enumerate(product_detailList):
        product_dateList = detail.find_all("h3",attrs={'class': DY_DETAIL_DATE})
        product_name = detail.find_all("h3", attrs={'class': DY_DETAIL_NAME})
        product_price = detail.find_all("span", attrs={'class': DY_DETAIL_PRICE})
        product_image = detail.find_all("figure", attrs={'class': DY_PRODUCT_IMAGE})
        product_date = product_dateList[0].text
        for nameIndex ,name in enumerate(product_name):
            product_price_findall = re.findall(r'(\d*?)円', product_price[nameIndex].text)
            DY_DETAIL_DATE_LIST.append({
            "product_name":name.text.replace('\n', '').replace('\t', ''),
            "product_price":int(product_price_findall[0]),
            "product_date":get_product_ymd(product_date),
            "product_image":product_image[nameIndex].img.get("src")
            })
    return DY_DETAIL_DATE_LIST

def get_product_ymd(product_date):
    current_year = datetime.now().year
    product_date = re.findall(r'(\d{1,2})月(\d{1,2})日', product_date)
    return str(current_year) + "." + product_date[0][0] + "." + product_date[0][1]