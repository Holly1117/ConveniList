# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# user-agent定義
USER_AGENT = 'Mozilla'

# URL定義
LN_REDIRECT_URL = 'https://www.lawson.co.jp/recommend/new/'
LN_OFFICE_URL = 'https://www.lawson.co.jp'

# CSSセレクタ定義
LN_PRODUCT_BOX = 'heightLineParent'
LN_PRODUCT_URL = '.img'
LN_PRODUCT_IMAGE = '.img'
LN_DETAIL_NAME = '.ttl'
LN_DETAIL_PRICE = '.price'
LN_DETAIL_DATE = '.date'
LN_DETAIL_TEXT = '.smalltxt'

# URLを取得
def get_product_site():
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(LN_REDIRECT_URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    meta = soup.find("meta", attrs={"http-equiv": "Refresh"})
    if not meta:
        return LN_REDIRECT_URL
    content = meta.get("content", "")
    redirect_path = content.split("URL=")[-1].strip()
    return urljoin(LN_REDIRECT_URL, redirect_path)

# contentsNavのaタグから各発売日のURLを取得
def get_contents_nav_links():
    headers = {"User-Agent": USER_AGENT}
    product_url = get_product_site()
    response = requests.get(product_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return [
        urljoin(product_url, a["href"])
        for a in soup.select("ul.contentsNav a[href]")
    ]

def get_product_information(page_url):
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(page_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    product_box = soup.find("ul", class_=LN_PRODUCT_BOX)
    if not product_box:
        return []
    product_list = []
    # liタグをループして商品情報を抽出
    for li in product_box.select("li"):
        a_tag = li.find("a")
        if not a_tag:
            continue
        # URL
        product_url = urljoin(LN_OFFICE_URL, a_tag.get("href"))
        # 商品名
        name_tag = li.select_one(LN_DETAIL_NAME)
        product_name = name_tag.get_text(strip=True) if name_tag else ""
        # 価格
        price_tag = li.select_one(LN_DETAIL_PRICE)
        if price_tag:
            price_text = price_tag.get_text(strip=True)
            product_price = int(
                price_text.replace("円(税込)", "")
                          .replace("円", "")
                          .replace("(税込)", "")
                          .replace(",", "")
            )
        else:
            product_price = 0
        # 画像
        img_tag = li.select_one(LN_PRODUCT_IMAGE)
        if img_tag and img_tag.find("img"):
            product_image = urljoin(
                LN_OFFICE_URL,
                img_tag.find("img").get("src")
            )
        else:
            product_image = ""
        # 発売日
        date_tag = li.select_one(LN_DETAIL_DATE)
        product_date = (
            date_tag.get_text(strip=True).replace("発売日", "")
            if date_tag else ""
        )
        product_list.append({
            "product_url": product_url,
            "product_name": product_name,
            "product_price": product_price,
            "product_image": product_image,
            "product_date": product_date
        })
    return product_list

# 全ての商品情報を取得
def get_all_products():
    all_products = []
    nav_links = get_contents_nav_links()
    for link in nav_links:
        products = get_product_information(link)
        all_products.extend(products)
    return all_products


get_all_products()
