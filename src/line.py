import requests
import urllib
import json
import dbcon

token = 'alBi5OAo3eYx95nfmxRhoHr4FycAQPWjKa3EmRk4JIB'

def send():
    url = 'https://notify-api.line.me/api/notify'
    
    
    payload = {
        
    }
    headers= {
        'Content-type' : "application/x-www-form-urlencoded",
        'Cache-Control' : 'no-cache',
        'Autorization' : "Bearer" + token,
    }
    response = requests.request("POST", url, data = payload, headers=headers)
    reesponseJson = json.loads(((response.json).encode('utf-8')))
    return reesponseJson
