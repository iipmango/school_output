from urllib.request import urlopen
from bs4 import BeautifulSoup
from .dbcon import dbInsert
import ssl
import json
import time

menu_date = []
menu = []
crawl_time = time.time

def crawl():
    context = ssl._create_unverified_context()

    html = urlopen("https://www.kumoh.ac.kr/ko/restaurant01.do", context = context)

    bsObject = BeautifulSoup(html, "html.parser")
    
    link = []
    
    link = bsObject.find_all('tr')
    for text in link[0]:
        menu_date.append(text.text.strip())
    for text in link[1]:
        menu.append(text.text.strip())
    if link[2]:
        for text in link[2]:
            menu.append(text.text.strip())

    dbInsert(json.dumps(menu_date, ensure_ascii = False), json.dumps(menu, ensure_ascii = False))
            
crawl()