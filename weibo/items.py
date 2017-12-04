# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class InformationItem(Item):
    _id = Field()  # 用户ID
    NickName = Field()  # 昵称
    Signature = Field()  # 个性签名
    Num_Tweets = Field()  # 微博数
    Num_Follows = Field()  # 关注数
    Num_Fans = Field()  # 粉丝数

class TweetsItem(Item):
    _id=Field() #微博ID
    ID=Field() #用户ID
    Content=Field() #微博内容
    PubTime=Field() #发表时间
    Like=Field() #点赞数
    Comment=Field() #评论数
    Transfer=Field() #转载数

class FansItem(Item):
    _id=Field() #粉丝ID
    ID=Field() #用户ID
    NickName=Field() #昵称
    Signature=Field() #个性签名
    Num_Tweets=Field() #微博数
    Num_Follows=Field() #关注数
    Num_Fans=Field() #粉丝数
    profile_url=Field() #主页链接

class FollowsItem(Item):
    _id=Field() #好友ID
    ID=Field() #用户ID
    NickName=Field() #昵称
    Signature=Field() #个性签名
    Num_Tweets=Field() #微博数
    Num_Follows=Field() #关注数
    Num_Fans=Field() #粉丝数
    profile_url=Field() #主页链接

