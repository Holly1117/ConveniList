import requests
import json
import config

WEBHOOK_URL = config.WEBHOOK_URL

LAWSON_CONTENT = [ "Lawson", "https://i.kobe-np.co.jp/rentoku/omoshiro/202201/img/d_14961479.jpg"]

FAMILY_CONTENT = ["FamilyMart","https://joinus-terrace.com/img/joinusfmg/store/storage/w670xh670/cname_20181029135326.jpg"]

SEVEN_CONTENT = ["SevenEleven","https://play-lh.googleusercontent.com/EEX7U_o2Q9o4kjuo1j1IR4JCm6LO29BifTdi404TFFQxnQsB8sGFXONbTDC6Yko3iik"]

HEADRES = {'Content-Type': 'application/json'}

CONTENT_LIST = [LAWSON_CONTENT,FAMILY_CONTENT,SEVEN_CONTENT]

def get_embeds(result):
    if (result):
     return [{'title': "Notice from the server",'description': 'List has been updated...','color': 1939322}]
    else:
     return [{'title': "Notice from the server",'description': 'Update failed!\nPlease maintain immediately!','color': 15146762}]

def get_content(index,result):
        return {'username': CONTENT_LIST[index][0],'avatar_url':  CONTENT_LIST[index][1],'embeds': get_embeds(result)}

def post_requests(index,result):
    requests.post(WEBHOOK_URL, json.dumps(get_content(index,result)), headers=HEADRES)