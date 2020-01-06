#This code is for scraping a particular part of the website and monitor it for particular changes and update in googlesheets

from requests_html import HTML , HTMLSession
from time import sleep as delay
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('tarc-ca917-6c61edc32594.json',scope)
gc = gspread.authorize(credentials)

wks = gc.open('test').sheet1

cellvalue = wks.acell('A2').value


session = HTMLSession()

#for data in datas:
#v = data.find('span', first = True).text
while True:
    r = session.get('https://play.google.com/store/apps/details?id=zedTarc.zig.zig')
    datas = r.html.find('span.htlgb')
    #print (datas[6].text)
    onlinevalue = datas[6].text
    print("cellvalue is",cellvalue)
    print("onlinevalue is",onlinevalue)

    if (onlinevalue != cellvalue):
        wks.update_acell('A2',onlinevalue)
        print("cell updated successfully")

    delay(10)
