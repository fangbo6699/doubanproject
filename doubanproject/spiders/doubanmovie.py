# -*- coding: utf-8 -*-
import scrapy
import requests
from urllib import request
import urllib, urllib3, sys
import ssl
from urllib import parse
from base64 import b64decode
class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/accounts/login/']
    login_url="https://www.douban.com/accounts/login/"
    my_url="https://www.douban.com/people/188757371/"
    hobby_url="https://www.douban.com/j/people/188757371/edit_signature/"
    def parse(self, response):
        formdata={
            "source":"None",
            "redir": "https://www.douban.com/people/188757371/",
            "form_email": "3292999096@qq.com",
            "form_password": "A1G6K8MN",
            "remember": "on",
            "login": "登录"
        }
        captcha_image_url=response.xpath("//img[@id='captcha_image']/@src").get()
        print(captcha_image_url)
        if captcha_image_url:
            request.urlretrieve(captcha_image_url,"captcha_image_url.png")
            formdata["captcha-id"]=response.xpath("//input[@name='captcha-id']/@value").get()
            formdata["captcha-solution"] = self.get_captcha(captcha_image_url)
        yield scrapy.FormRequest(self.login_url,formdata=formdata,callback=self.login_after_parse)
    def login_after_parse(self,response):
        if response.url == self.my_url:
            print("#"*80)
            print("login successful")
            ckvalue=response.xpath("//input[@name='ck']/@value").get()
            formdata={
                "ck": ckvalue,
                "signature":"mygirl"
            }
            scrapy.FormRequest(self.hobby_url,formdata=formdata,callback=self.parse_none)
        else:
            print("#" * 80)
            print("login failed")
    def parse_none(self):
        pass
    def get_captcha(self,captcha_image_url):


        # host = 'https://imgurlocr.market.alicloudapi.com'
        # path = '/urlimages'
        # method = 'POST'
        # appcode = 'a1fc3a1115dc48608050daaeb0801f5b'
        # querys = ''
        # bodys = {}
        # url = host + path
        # headers={
        #     "Authorization":'APPCODE ' + appcode,
        #     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
        # }
        # bodys['image'] = captcha_image_url
        # post_data = urllib.parse.urlencode(bodys)
        # response = requests.post(url, post_data,headers =headers)
        # # ctx = ssl.create_default_context()
        # # ctx.check_hostname = False
        # # # ctx.verify_mode = ssl.CERT_NONE
        # # response = urllib.request.urlopen(request, context=ctx)
        # content =response._content
        # if (content):
        #     print("@"*50)
        #     print(content)
        #     print(content.json())
        # return["result"]["words"]
        appcode = 'a1fc3a1115dc48608050daaeb0801f5b'
        # reg_url= "http(s)://imgurlocr.market.alicloudapi.com/urlimages/"
        host = 'https://imgurlocr.market.alicloudapi.com'
        path = '/urlimages'
        url = host + path
        bodys = {}
        bodys['image'] = captcha_image_url
        # with open("captcha_image_url.png", "rb") as fp:
        #     data = fp.read()
        #     pic = b64decode(data)
        #     bodys["pic"] = pic
        #     print(pic)
        headers = {
            "Authorization": 'APPCODE ' + appcode,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        response = requests.post(url, data=bodys, headers=headers)
        print(type(response))
        print(response.content.decode("utf-8"))
        yield response.content.decode("utf-8")["result"]["words"]





