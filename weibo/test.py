# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       7326
   date：          2017/12/3
-------------------------------------------------
   Change Activity: 2017/12/3
-------------------------------------------------
"""
__author__ = '7326'

import requests
from cookies import cookies
import random

if __name__ == '__main__':
    url = 'https://m.weibo.cn/feed/friends?version=v4&next_cursor=4180778692342438&page=1'
    cookie = random.choice(cookies)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    r = requests.get(url=url, cookies=cookie, headers=headers)
    print(r.json())