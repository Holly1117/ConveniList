# -*- coding: utf-8 -*-
from flask import Flask ,render_template
import json
import ssl

app = Flask(__name__)

FM_FILE_PATH = 'familyMart.json'

LN_FILE_PATH = 'lawson.json'

SE_FILE_PATH = 'sevenEleven.json'

@app.route("/")
def get_index():
    return ""

@app.route('/lawson')
def get_lawson():
 info_jsons = json.load(open(LN_FILE_PATH, 'r',encoding='UTF-8'))
 return render_template("lawson.html", jsons = info_jsons)

@app.route('/familymart')
def get_familymart():
 info_jsons = json.load(open(FM_FILE_PATH, 'r',encoding='UTF-8'))
 return render_template("familyMart.html", jsons = info_jsons)

@app.route('/seveneleven')
def get_seveneleven():
 info_jsons = json.load(open(SE_FILE_PATH, 'r',encoding='UTF-8'))
 return render_template("sevenEleven.html", jsons = info_jsons)

if __name__ == "__main__":
    app.run()