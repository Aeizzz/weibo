# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     weibo_keyword
   Description :
   Author :       7326
   date：          2017/12/5
-------------------------------------------------
   Change Activity: 2017/12/5
-------------------------------------------------
"""
from urllib import parse

__author__ = '7326'

'''
404
搜索问题
'''
from weibo.weibo_keyword import keywords
from scrapy.spider import CrawlSpider, logging
from scrapy.http import Request
import json
from weibo.items import KeyTweetsItem
from weibo.utils import getTime
import requests

class Weibo_keyword(CrawlSpider):
    name = 'weibo_keyword'
    allowed_domains = ['https://m.weibo.cn']
    start_urls = list(set(keywords))
    logging.getLogger("requests").setLevel(logging.WARNING)


    def start_requests(self):
        for key in self.start_urls:
            url = 'https://m.weibo.cn/api/container/getIndex?'
            data = {
                "type": "all",
                "queryVal": key,
                "featurecode": "20000320",
                "luicode": "10000011",
                "lfid": "106003type=1",
                "title": key,
                "containerid": "100103type=1&q=" + key,
            }
            data = str(parse.urlencode(data).encode('utf-8'))
            url = url+data
            yield Request(url=url,meta={"keyword":key},callback=self.parse_Tweets,dont_filter=True)



    # 获取一个关键词的内容
    def parse_Tweets(self, response):
        tweets = json.loads(response.body)
        keyword = response.meta['keyword']
        page = ''
        containerid = ''
        tweets = tweets['data']

        if tweets.get('cards',''):
            cards = tweets['cards']
            if tweets['cardlistInfo'].get('page',''):
                page = tweets['cardlistInfo']['page']
                page = str(page)
            else:
                return
            if tweets['cardlistInfo'].get('containerid',''):
                containerid = tweets['cardlistInfo']['containerid']
                containerid = str(containerid)
            else:
                return
            for card in cards:
                if card['show_type'] == 1:
                    card_group = card['card_group']
                    for group in card_group:
                        mblog = group.get('mblog', '')
                        if mblog:
                            keyTweetsItem = KeyTweetsItem()
                            keyTweetsItem['_id'] = group['mblog']['mid']
                            keyTweetsItem['ID'] = group['mblog']['user']['id']
                            keyTweetsItem['keyword'] = keyword
                            text = self.get_text_byid(group['mblog']['mid'])
                            if text == None:
                                text = group['mblog']['text']
                            keyTweetsItem['text'] = text
                            keyTweetsItem['PubTime'] = group['mblog']['created_at']
                            keyTweetsItem['createtime'] = getTime()
                        yield keyTweetsItem
            url = 'https://m.weibo.cn/api/container/getIndex?'
            data = {
                "type": "all",
                "queryVal": keyword,
                "featurecode": "20000320",
                "luicode": "10000011",
                "lfid": "106003type=1",
                "title": keyword,
                "containerid": "100103type=1&q=" + keyword,
                "page":page,
            }
            data = str(parse.urlencode(data).encode('utf-8'))
            url = url + data
            yield Request(url=url,meta={"keyword":keyword},callback=self.parse_Tweets,dont_filter=True)



    def get_text_byid(self,id):
        try:
            url = 'https://m.weibo.cn/statuses/extend?id=%s'%(str(id))
            r = requests.get(url=url)
            return json.loads(r.content)['longTextContent']
        except Exception as e:
            return None