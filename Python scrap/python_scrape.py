from requests_html import HTML , HTMLSession
from time import sleep as delay
#This code is for scraping a particular part of the website and monitor it for particular changes
session = HTMLSession()

#for data in datas:
#v = data.find('span', first = True).text
while True:
    r = session.get('https://play.google.com/store/apps/details?id=zedTarc.zig.zig')
    datas = r.html.find('span.htlgb')
    print (datas[6].text)
    delay(10)
