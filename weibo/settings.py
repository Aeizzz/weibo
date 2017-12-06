# -*- coding: utf-8 -*-

# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False



DOWNLOADER_MIDDLEWARES = {
   'weibo.middlewares.UserAgentMiddleware': 401,
    'weibo.middlewares.CookiesMiddleware':402,
    'weibo.middlewares.ProxyMiddleware':400,
}

# ITEM_PIPELINES = {
#     'weibo.pipelines.WeiboPipeline': 300,
# }




#------------scrapy-redis 分布式爬虫相关设置-----------------
# 修改scrapy默认的调度器为scrapy重写的调度器 启动从reids缓存读取队列调度爬虫
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True

# 请求调度使用优先队列（默认)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# 请求调度使用FIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# 请求调度使用LIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# 最大的空闲时间，避免分布式爬取得情况下爬虫被关闭
# 此设置只适用于SpiderQueue和SpiderStack
# 也是爬虫第一次启动时的等待时间（应为队列是空的）
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 存储爬取到的item，一定要在所有的pipeline最后，即设定对应的数字大于其他pipeline
ITEM_PIPELINES = {
    'weibo.pipelines.WeiboPipeline': 256,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 指定redis的地址和端口(可选，程序将使用默认的地址localhost:6379)
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 声明redis的url地址（可选）
# 如果设置了这一项，则程序会有限采用此项设置，忽略REDIS_HOST 和 REDIS_PORT的设置
# REDIS_URL = 'redis://user:pass@hostname:9001'
#------------end scrapy-redis----------------------------