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


def get_product_information():

    product_list = []

    response = requests.get(DY_OFFICE_URL)

    if response.status_code != 200:
        return product_list

    soup = BeautifulSoup(response.text, "html.parser")

    product_detail_list = soup.find_all(
        "div",
        attrs={'class': DY_DETAIL_LIST}
    )

    for detail in product_detail_list:

        # 発売日
        date_element = detail.find(
            "h3",
            attrs={'class': DY_DETAIL_DATE}
        )

        if date_element:
            product_date = get_product_ymd(date_element.text)
        else:
            product_date = None


        # 商品情報
        product_names = detail.find_all(
            "h3",
            attrs={'class': DY_DETAIL_NAME}
        )

        product_prices = detail.find_all(
            "span",
            attrs={'class': DY_DETAIL_PRICE}
        )

        product_images = detail.find_all(
            "figure",
            attrs={'class': DY_PRODUCT_IMAGE}
        )


        for index, name in enumerate(product_names):

            # 価格
            price = None

            if index < len(product_prices):
                price_text = product_prices[index].text

                price_match = re.search(
                    r'税込(\d+)\s*円',
                    price_text
                )

                if price_match:
                    price = int(price_match.group(1))


            # 画像
            image_url = None

            if index < len(product_images):
                img = product_images[index].find("img")

                if img:
                    image_url = img.get("src")


            product_list.append({
                "product_name": name.text.strip(),
                "product_price": price,
                "product_date": product_date,
                "product_image": image_url
            })


    return product_list



def get_product_ymd(product_date):

    current_year = datetime.now().year

    result = re.search(
        r'(\d{1,2})月(\d{1,2})日',
        product_date
    )

    if result:
        month = result.group(1)
        day = result.group(2)

        return f"{current_year}.{month}.{day}"

    return None

print(get_product_information())