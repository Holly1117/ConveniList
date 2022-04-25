# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import requests

USER_AGENT = 'Mozilla'

LN_REDIRECT_URL = 'https://www.lawson.co.jp/recommend/new/'

LN_OFFICE_URL ='https://www.lawson.co.jp'

LN_PRODUCT_BOX = 'heightLineParent'

LN_PRODUCT_URL = '.img'

LN_PRODUCT_IMAGE = '.img'

LN_DETAIL_NAME = '.ttl'

LN_DETAIL_PRICE = '.price'

LN_DETAIL_DATE = '.date'

LN_DETAIL_TEXT = '.smalltxt'

LN_PRODUCT_LIST = []

def get_product_site():
    header = {
    'User-Agent': USER_AGENT
    }
    get_requests = requests.get(LN_REDIRECT_URL, headers=header)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    product_url = beasutiful_soup.find_all("meta",attrs={'http-equiv': 'Refresh', 'content': True})
    product_content = product_url[0].get('content')
    office_url = product_content[7:]
    return office_url

def get_product_information():
    ln_office_url = LN_OFFICE_URL + get_product_site()
    header = {
    'User-Agent': USER_AGENT
    }
    get_requests = requests.get(ln_office_url, headers=header)
    beasutiful_soup = BeautifulSoup(get_requests.content, "html.parser")
    product_box = beasutiful_soup.find("ul", attrs={'class': LN_PRODUCT_BOX})
    product_url = product_box.select(LN_PRODUCT_URL)
    product_name = product_box.select(LN_DETAIL_NAME)
    product_price = product_box.select(LN_DETAIL_PRICE)
    product_image = product_box.select(LN_PRODUCT_IMAGE)
    product_date = product_box.select(LN_DETAIL_DATE)
    product_text = product_box.select("li")
    for index,url in enumerate(product_url):
        product_text_select = product_text[index].select_one(LN_DETAIL_TEXT)
        if product_text_select is None :
            product_text_select = ""
        else :
            product_text_select = product_text_select.text

        LN_PRODUCT_LIST.append({
        "product_url":LN_OFFICE_URL + url.a.get("href"),
        "product_name":product_name[index].text,
        "product_price":int(product_price[index].text.replace('円(税込)', '')), 
        "product_image":LN_OFFICE_URL + product_image[index].img.get("src"),
        "product_date":product_date[index].text.replace('発売日', ''),
        "product_text":product_text_select
        })
    return LN_PRODUCT_LIST
