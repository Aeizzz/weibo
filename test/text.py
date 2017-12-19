# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     text
   Description :
   Author :       7326
   date：          2017/12/4
-------------------------------------------------
   Change Activity: 2017/12/4
-------------------------------------------------
"""
__author__ = '7326'
import requests

headers = {
    "accept":"application/json, text/plain, */*",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
    "content-type":"application/json;charset=utf-8",
    "cookie":"csrftoken=2LrRZcl201tb925VXAmrJcdwN88HgUPAhxcaC5DcXhI28YQyyxbHqWtxZ8E7cWHX; sessionid=x7vjpd265f0505rotyjqojd1iw9o2j5p",
    "referer":"https://www.7326it.club/admin/problem/edit/21",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "x-csrftoken":"2LrRZcl201tb925VXAmrJcdwN88HgUPAhxcaC5DcXhI28YQyyxbHqWtxZ8E7cWHX"
}

import json
import time
def main(url):
    try:
        r =  requests.get(url=url,headers=headers)
        r = json.loads(r.content)
        description = r['data']['description']
        input_description = r['data']['input_description']
        output_description = r['data']['output_description']
        test_case_id = r['data']['test_case_id']
        id = r['data']['id']
        samples = r['data']['samples'][0]
        input = samples['input']
        output = samples['output']
        save_test_case(id,id)
        save_text(id,description,input_description,output_description,input,output)
        print(id)
    except Exception as e:
        print(e)



def save_text(id,description,input_description,output_description,input,output):
    with open("problem/%d.txt" %(id),"w") as f:
        f.writelines("description\n")
        f.writelines(description+'\n')
        f.writelines("input_description\n")
        f.writelines(input_description+'\n')
        f.writelines("output_description\n")
        f.writelines(output_description+'\n')
        f.writelines("input\n")
        f.writelines(input + '\n')
        f.writelines("output\n")
        f.writelines(output + '\n')



def save_test_case(id,problem):
    url = 'https://www.7326it.club/api/admin/test_case?problem_id=%d'% (id)
    r = requests.get(url=url,headers=headers)
    with open("problem/%s.zip"%(str(problem)),"wb") as f:
        f.write(r.content)


if __name__ == '__main__':
    num = 1
    while num <= 45:
        url = 'https://www.7326it.club/api/admin/problem?id=%d' % (num)
        time.sleep(2)
        main(url=url)
        num +=1