# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import math

SE_OFFICE_URL = 'https://www.sej.co.jp/products/a/thisweek/'

SE_PRODUCT_URL = 'item_ttl'

SE_PRODUCT_IMAGE = 'list_inner'

SE_DETAIL_NAME = 'item_ttl'

SE_DETAIL_PRICE = 'item_price'

SE_DETAIL_DATE = 'item_launch'

SE_PREFECTURE_URL = 'list_btn'

SE_PREFECTURE_NAME = 'ttl_02'

SE_PREFECTURE_INDEX = 6

SE_PROEFECTURE_LIST = []

def get_product_information():
    get_prefecture()
    se_product_list = []
    get_requests = requests.get(SE_OFFICE_URL)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    product_url = beasutiful_soup.find_all("div", attrs={'class': SE_PRODUCT_URL})
    product_name = beasutiful_soup.find_all("div", attrs={'class': SE_DETAIL_NAME})
    product_price = beasutiful_soup.find_all("div", attrs={'class': SE_DETAIL_PRICE})
    product_image = beasutiful_soup.find_all("div", attrs={'class': SE_PRODUCT_IMAGE})
    product_date = beasutiful_soup.find_all("div", attrs={'class': SE_DETAIL_DATE})
    product_index = 0
    proefecture_index = 0
    for index,url in enumerate(product_url):
        product_price_findall = re.findall(r'税込(.*?)円', product_price[index].p.text)
        product_date_parse = product_date[index].p.text
        product_date_yyyy = re.findall(r'(.*?)年', product_date_parse)
        product_date_mm = re.findall(r'年(.*?)月', product_date_parse)
        product_date_dd = re.findall(r'月(.*?)日', product_date_parse)
        product_date_ymd = product_date_yyyy[0] + "." + product_date_mm[0] + "." + product_date_dd[0]
        se_product_list.append({
            "product_url":"https://www.sej.co.jp" + url.a.get("href"),
            "product_name":product_name[index].text,
            "product_price":math.floor(float(product_price_findall[0])),
            "product_image":product_image[index].img.get("data-original"),
            "product_date":product_date_ymd
            })
        product_index += 1
        if product_index == SE_PREFECTURE_INDEX:
            SE_PROEFECTURE_LIST[proefecture_index]["product_list"] = se_product_list
            se_product_list = []
            product_index = 0
            proefecture_index += 1
    return SE_PROEFECTURE_LIST

def get_prefecture():
    get_requests = requests.get(SE_OFFICE_URL)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    prefecture_url = beasutiful_soup.find_all("div", attrs={'class': SE_PREFECTURE_URL})
    prefecture_name = beasutiful_soup.find_all("div", attrs={'class': SE_PREFECTURE_NAME})
    for index,url in enumerate(prefecture_url):
        SE_PROEFECTURE_LIST.append({
            "prefecture_url":"https://www.sej.co.jp" + url.a.get("href"),
            "product_list":None,
            "prefecture_name":prefecture_name[index].h2.text.replace('\n', '').replace('\t', '').replace(' ', '')
            })
    return SE_PROEFECTURE_LIST