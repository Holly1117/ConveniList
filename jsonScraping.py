# -*- coding: utf-8 -*-
import familyMartScraping as FMScraping
import lawsonScraping as LNScraping
import sevenElevenScraping as SEScraping
import dailyYamazakiScraping as DYScraping
import webHook as WebHook
import json
import datetime

FM_FILE_PATH = 'familyMart.json'

LN_FILE_PATH = 'lawson.json'

SE_FILE_PATH = 'sevenEleven.json'

DY_FILE_PATH = 'dailyYamazaki.json'

STORE_UPDATE_PATH = 'storeUpdate.json'

STORE_FILE_LIST = [FM_FILE_PATH, LN_FILE_PATH, SE_FILE_PATH,DY_FILE_PATH,STORE_UPDATE_PATH]

STORE_TIME_LIST = []

def get_familymart():
    try:
        info_jsons = FMScraping.get_product_information()
        WebHook.post_requests(1, True)
        dt_now = datetime.datetime.now()
        STORE_TIME_LIST.append({"familyMart":dt_now.strftime('%Y年%m月%d日 %H:%M:%S')})
        return info_jsons
    except:
        WebHook.post_requests(1, False)


def get_lawson():
    try:
        info_jsons = LNScraping.get_all_products()
        WebHook.post_requests(0, True)
        dt_now = datetime.datetime.now()
        STORE_TIME_LIST.append({"lawson":dt_now.strftime('%Y年%m月%d日 %H:%M:%S')})
        return info_jsons
    except:
        WebHook.post_requests(0, False)


def get_seveneleven():
    try:
        info_jsons = SEScraping.get_product_information()
        WebHook.post_requests(2, True)
        dt_now = datetime.datetime.now()
        STORE_TIME_LIST.append({"sevenEleven":dt_now.strftime('%Y年%m月%d日 %H:%M:%S')})
        return info_jsons
    except:
        WebHook.post_requests(2, False)

def get_dailyYamazaki():
    try:
        info_jsons = DYScraping.get_product_information()
        WebHook.post_requests(3, True)
        dt_now = datetime.datetime.now()
        STORE_TIME_LIST.append({"dailyYamazaki":dt_now.strftime('%Y年%m月%d日 %H:%M:%S')})
        return info_jsons
    except:
        WebHook.post_requests(3, False)


def git_deploy():
    store_def_list = [get_familymart(), get_lawson(), get_seveneleven(),get_dailyYamazaki(),STORE_TIME_LIST]

    for index, file_path in enumerate(STORE_FILE_LIST):
        codecs_open = open(file_path, 'w', encoding='UTF-8')
        get_dict = store_def_list[index]
        json.dump(get_dict, codecs_open, ensure_ascii=False, indent=2)
        codecs_open.close()


git_deploy()
