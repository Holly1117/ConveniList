import requests
import json
import config

WEBHOOK_URL = config.WEBHOOK_URL

LAWSON_CONTENT = [ "ローソン", "https://i.kobe-np.co.jp/rentoku/omoshiro/202201/img/d_14961479.jpg"]

FAMILY_CONTENT = ["ファミリーマート","https://greensprings.jp/wp/wp-content/uploads/2020/03/img-logo_Familymart.png"]

SEVEN_CONTENT = ["セブンイレブン","https://play-lh.googleusercontent.com/EEX7U_o2Q9o4kjuo1j1IR4JCm6LO29BifTdi404TFFQxnQsB8sGFXONbTDC6Yko3iik"]

DAILY_CONTENT = ["デイリーヤマザキ","https://pbs.twimg.com/profile_images/1113599389249839104/eD2onJy9_400x400.jpg"]

HEADRES = {'Content-Type': 'application/json'}

CONTENT_LIST = [LAWSON_CONTENT,FAMILY_CONTENT,SEVEN_CONTENT,DAILY_CONTENT]

def get_embeds(result):
    if (result):
     return [{'title': "Notice from the server",'description': 'List has been updated...','color': 1939322}]
    else:
     return [{'title': "Notice from the server",'description': 'Update failed!\nPlease maintain immediately!','color': 15146762}]

def get_content(index,result):
        return {'username': CONTENT_LIST[index][0],'avatar_url':  CONTENT_LIST[index][1],'embeds': get_embeds(result)}

def post_requests(index,result):
    requests.post(WEBHOOK_URL, json.dumps(get_content(index,result)), headers=HEADRES)