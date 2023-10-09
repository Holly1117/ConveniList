# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

FM_OFFICE_URL = 'https://www.family.co.jp/goods/newgoods.html'

FM_PRODUCT_URL = 'ly-mod-infoset3-link'

FM_PRODUCT_IMAGE = 'ly-mod-infoset3-img'

FM_DETAIL_NAME = 'ly-mod-infoset3-ttl'

FM_DETAIL_PRICE = 'ly-mod-infoset3-txt'

FM_DETAIL_DATE = 'ly-goods-spec'

FM_PRODUCT_LIST = []

def get_product_information():
    get_requests = requests.get(FM_OFFICE_URL)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    product_url = beasutiful_soup.find_all("a", attrs={'class': FM_PRODUCT_URL})
    product_name = beasutiful_soup.find_all("h3", attrs={'class': FM_DETAIL_NAME})
    product_price = beasutiful_soup.find_all("p", attrs={'class': FM_DETAIL_PRICE})
    product_image = beasutiful_soup.find_all("p", attrs={'class': FM_PRODUCT_IMAGE})
    for index,url in enumerate(product_url):
        product_price_findall = re.findall(r'(\d*?)円', product_price[index].text)
        product_date = get_product_dates(url.get("href"))
        product_date_ymd = get_product_ymd(product_date)
        FM_PRODUCT_LIST.append({
            "product_url":url.get("href"),
            "product_name":product_name[index].text.replace('\n', '').replace('\t', ''),
            "product_price":int(product_price_findall[1]),
            "product_date":product_date_ymd,
            "product_image":'https://www.family.co.jp' + product_image[index].img.get("src")
            })
    return FM_PRODUCT_LIST

def get_product_dates(product_url):
    get_requests = requests.get(product_url)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    product_date = beasutiful_soup.find("ul", attrs={'class': FM_DETAIL_DATE})
    return product_date.li.text.replace('発売日：', '')

def get_product_ymd(product_date):
     if '年' in product_date:
         product_date_yyyy = re.findall(r'(.*?)年', product_date)
         product_date_mm = re.findall(r'年(.*?)月', product_date)
         product_date_dd = re.findall(r'月(.*?)日', product_date)
         return product_date_yyyy[0] + "." + product_date_mm[0] + "." + product_date_dd[0]
     else :
         product_date_yyyy = re.findall(r'(.*?)\/', product_date)
         product_date_mm = re.findall(r'\/(.*?)\/', product_date)
         product_date_dd = re.findall(product_date_yyyy[0] +'\/'+product_date_mm[0]+'\/(\d*)', product_date)
         return product_date_yyyy[0] + "." + product_date_mm[0] + "." + product_date_dd[0]