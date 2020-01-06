#this code is for updating cells in  google sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('tarc-ca917-6c61edc32594.json',scope)

gc = gspread.authorize(credentials)

wks = gc.open('test').sheet1

print(wks.acell('A2').value)
wks.update_acell('A2',"data")
print(wks.acell('A2').value)
