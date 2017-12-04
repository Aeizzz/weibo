# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     launch
   Description :
   Author :       7326
   date：          2017/12/3
-------------------------------------------------
   Change Activity: 2017/12/3
-------------------------------------------------
"""
__author__ = '7326'

from scrapy import cmdline

cmdline.execute("scrapy crawl weibo".split())