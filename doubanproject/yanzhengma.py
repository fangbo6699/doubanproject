#encoding:utf-8

"""
@project =doubanproject
@file=yanzhengma
@user=Administrator
@create_time=2018/12/16_0:36
"""
import urllib, urllib3, sys
import ssl
from urllib import parse
import requests
from base64 import b64decode
from requests.models import Response

# appcode = 'a1fc3a1115dc48608050daaeb0801f5b'
# # reg_url= "http(s)://imgurlocr.market.alicloudapi.com/urlimages/"
# host = 'https://imgurlocr.market.alicloudapi.com'
# path = '/urlimages'
# url = host + path
# formdata = {}
# with open("../captcha_image_url.png", "rb") as fp:
#     data = fp.read()
#     pic = b64decode(data)
#     formdata["pic"] = pic
#     print(pic)
# headers = {
#     "Authorization": 'APPCODE ' + appcode,
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
# }
# response = requests.post(url, data=formdata, headers=headers)
# print(type(response))
# print(response.content)

appcode = 'a1fc3a1115dc48608050daaeb0801f5b'
# reg_url= "http(s)://imgurlocr.market.alicloudapi.com/urlimages/"
host = 'https://imgurlocr.market.alicloudapi.com'
path = '/urlimages'
url = host + path
bodys = {}
bodys['image'] = "https://oimageb3.ydstatic.com/image?id=-1405961428748346345&product=adpublish&w=300&h=250&sc=0&rm=0"
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