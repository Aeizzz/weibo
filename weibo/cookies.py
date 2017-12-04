# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cookies
   Description :
   Author :       7326
   date：          2017/12/2
-------------------------------------------------
   Change Activity: 2017/12/2
-------------------------------------------------
"""
__author__ = '7326'

from selenium import webdriver
import time

# chromedriver
chromepath = 'F:\weibo\weibo\chromedriver.exe'
myWeiBo = [
    {'account':'15610593295','password':'liuhonglei199634'},
]


'''
登陆账号获取cookies
使用selenium，先调用chrome浏览器
最后改成PhantomJS
'''
def getCookies(weibo):
    url = 'https://passport.weibo.cn/signin/login'
    print("Start crawl cookies!!!!")
    cookies = []
    for ele in weibo:
        account = ele['account']
        password = ele['password']
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["--ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path=chromepath,chrome_options=options)
            driver.get(url=url)
            time.sleep(2)

            failure = 0
            while "登录 - 新浪微博" in driver.title and failure < 5:
                failure+=1
                # #loginName
                username =  driver.find_element_by_id("loginName")
                username.clear()
                username.send_keys(account)
                # loginPassword
                psd = driver.find_element_by_id("loginPassword")
                psd.clear()
                psd.send_keys(password)

                commit = driver.find_element_by_id('loginAction')
                commit.click()
                time.sleep(2)
                cookie = {}
                if "微博 - 随时随地发现新鲜事" in driver.title:
                    for elem in driver.get_cookies():
                        cookie[elem['name']] = elem['value']
                        if len(cookie)>0:
                            cookies.append(cookie)
                            print("Get Cookie Successful: %s!!!!!!"%account)
        except Exception as e:
            print("%s Failure!!!!!" % account)
            print(e)
            pass
        finally:
            try:
                driver.quit()
            except Exception as e:
                pass
    return cookies



cookies = getCookies(myWeiBo)

