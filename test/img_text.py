# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     img_text
   Description :
   Author :       7326
   date：          2017/12/4
-------------------------------------------------
   Change Activity: 2017/12/4
-------------------------------------------------
"""
import json
import uuid

__author__ = '7326'
import requests

headers = {
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Referer":"http://www.ssyer.com/",
    "Cookie":"UM_distinctid=1601c0ca7ae239-0307c9e133e209-5b452a1d-1fa400-1601c0ca7af949; goeasyNode=6; CNZZDATA1262807909=1494077160-1512294453-%7C1512386212"

}

def main(url):
    data = {
        "start": 0,
        "limit": 20,
    }
    num = 1
    while True:
        r = requests.post(url=url,data=data,headers=headers)
        r = json.loads(r.content)
        pageCount = r['data']['pageCount']
        pageIndex = r['data']['pageIndex']
        if pageIndex == pageCount:
            break
        img_data = r['data']['datas']
        for img in img_data:
            img_url = img['pictureUrl']
            id = getUUID()
            save_img(url=img_url,id=id)
        data['start'] += 20


def save_img(url,id):
    print(url)
    r = requests.get(url=url,headers=headers)
    with open('F:\img\%s.jpg'%id,"wb") as f:
        f.write(r.content)




def getUUID():
    s_uuid = str(uuid.uuid5(uuid.uuid4(),''))
    l_uuid = s_uuid.split('-')
    return ''.join(l_uuid)


if __name__ == '__main__':
    url = 'http://www.ssyer.com/pc/order/newsOrderList'
    main(url=url)