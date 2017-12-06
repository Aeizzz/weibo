# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       7326
   date：          2017/12/5
-------------------------------------------------
   Change Activity: 2017/12/5
-------------------------------------------------
"""
import uuid
from datetime import datetime

from pytz import timezone

__author__ = '7326'

# 获取当前时间
def getTime():
    ZH = timezone('Asia/Shanghai')
    return datetime.now(ZH)

def getUUID(self):
    s_uuid = str(uuid.uuid5(uuid.uuid4(),''))
    l_uuid = s_uuid.split('-')
    return ''.join(l_uuid)