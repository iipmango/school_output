import requests
import urllib
import json
from .dbcon import dbGet
import datetime

token = 'R0F5lpR51XrvM0gDRxvHT8abopYd04vE6oPYMIqghau'

def send():
    url = 'https://notify-api.line.me/api/notify'
    
    today = datetime.datetime.today().weekday()
    
    Date = []
    Lunch = []
    Date, Lunch = dbGet()
    if Lunch[today + 7]:
        payload = 'message="' + Date[today] + Lunch[today] + Lunch[today + 7] + '"'
    else:
        payload = 'message="' + Date[today] + Lunch[today] + '"'
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Authorization' : 'Bearer ' + token,
    }
    response = requests.request("POST", url, data = payload.encode('utf-8'), headers = headers)
    responseJson = json.loads(((response.text).encode('utf-8')))
    return responseJson
