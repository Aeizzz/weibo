# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     weibo_keyword_test
   Description :
   Author :       7326
   date：          2017/12/5
-------------------------------------------------
   Change Activity: 2017/12/5
-------------------------------------------------
"""
__author__ = '7326'

from weibo.weibo_keyword import keywords
from urllib import parse
def main():
    for key in keywords:
        print(key)
        url = b'https://m.weibo.cn/api/container/getIndex?'
        data = {
            "type":"all",
            "queryVal":key,
            "featurecode":"20000320",
            "luicode":"10000011",
            "lfid":"106003type=1",
            "title":key,
            "containerid":"100103type=1&q="+key,
        }
        data = parse.urlencode(data).encode('utf-8')
        print(url+data)
if __name__ == '__main__':
    main()