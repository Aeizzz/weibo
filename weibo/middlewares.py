# -*- coding: utf-8 -*-

import random
from .user_agent import agents
from .cookies import cookies

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware



class UserAgentMiddleware(UserAgentMiddleware):
    def process_request(self,request,spider):
        agent = random.choice(agents)
        request.headers.setdefault("User-Agent",agent)


class CookiesMiddleware(object):
    def process_request(self,requset,spider):
        cookie = random.choice(cookies)
        requset.cookies = cookie


