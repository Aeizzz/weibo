# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     loj
   Description :
   Author :       7326
   date：          2017/12/5
-------------------------------------------------
   Change Activity: 2017/12/5
-------------------------------------------------
"""
__author__ = '7326'

import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()

def getproblemid(page):
    reg = '<a style="vertical-align: middle; " href="/problem/([0-9]+)">'
    com = re.compile(reg)
    return re.findall(com, page)

page = 1
problemlist = []

while page<=12:
    r = session.get("https://loj.ac/problems?page=" + str(page))
    if r.status_code == 200:
        problemlist += getproblemid(r.text)
        page +=1
    else:
        break

for each in problemlist:
    page = session.get("https://loj.ac/problem/" + str(each))
    data = session.get("https://loj.ac/problem/" + str(each) + "/testdata/download")
    with open(str(each) + ".zip", "wb") as code:
        code.write(data.content)
    soup = BeautifulSoup(page.text, "lxml")
    ti = soup.find_all("h4", class_="ui top attached block header")
    an = soup.find_all("div", class_="ui bottom attached segment font-content")
    with open(str(each) + "pro.txt", "w", encoding="utf-8") as text:
        for i in range(len(ti)):
            text.write(ti[i].text + " : " + an[i].text)
