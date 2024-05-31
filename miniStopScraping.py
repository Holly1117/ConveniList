# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

MS_OFFICE_URL = 'https://www.ministop.co.jp/syohin/'

MS_PRODUCT_IMAGE = 'productListPhoto'

MS_DETAIL_NAME = 'name'

MS_DETAIL_PRICE = 'price'

MS_PRODUCT_LIST = []

def get_product_information():
    get_requests = requests.get(MS_OFFICE_URL)
    beasutiful_soup = BeautifulSoup(get_requests.text, "html.parser")
    print(beasutiful_soup)
     
get_product_information()