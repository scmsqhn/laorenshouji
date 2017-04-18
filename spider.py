# -*- coding: utf-8 -*-

from lxml import etree
import json
import urllib.request
import sys
import urllib.request,time,socket,random
import re,collections
import decimal
import matplotlib.pyplot as plt
import xlsxwriter
import sys
#from lxml import etree
import codecs
import json
import time
import random
import subprocess
import codecs
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
import re
import chardet
import xlwt
from datetime import datetime
import os
import os.path
import numpy as np
import data_helpers
import numpy as np
import os
import time
import datetime
import data_helpers
import csv
import data_helpers
import http.cookiejar
#import xlsxwriter



baseurl=u'https://detail.tmall.com/item.htm?id=542064021808&ns=1&abbucket=1&sku_properties=5919063:6536025;12304035:21508;122216431:27772'

ajax_req=[{'X-Requested-With':'XMLHttpRequest'},]

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]


def request_ajax_url(url,body,referer=None,cookie=None,**headers):
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Requested-With','XMLHttpRequest')
    if cookie:
        req.add_header('Cookie',cookie)

    if referer:
        req.add_header('Referer',referer)

    if headers:
        for k in list(headers.keys()):
            req.add_header(k,headers[k])

    postBody = json.dumps(body)

    response = urllib.request.urlopen(req, postBody)

    if response:
        return response

def run():
    import time
    "use username:xfkxfk; use password:123456"

    login_url = 'http://www.xx.com/member/Login.aspx'
    login_body = {"action":"login","UserName":"xfkxfk","Password":"123456","AutomaticLogin":False}
    login_referer = "http://www.xx.com/member/Login.aspx?ReturnUrl=aHR0cDovL3d3dy5sdXNlbi5jb20vRGVmYXVsdC5hc3B4"

    url = 'http://www.xx.com/Member/MobileValidate.aspx'
    referer = "http://www.xx.com/Member/ModifyMobileValidate.aspx"

    headers = {}

    response = request_ajax_url(login_url,login_body,login_referer)

    if response.read() == "1":
        print(" Login Success !!!")

    if 'set-cookie' in response.headers:
        set_cookie = response.headers['set-cookie']
    else :
        print(" Get set-cookie Failed !!! May Send Messages Failed ~~~")

    if len(sys.argv) < 3:
        print(("\nUsage: python " + sys.argv[0] + "mobile_number" + "count\n"))
        sys.exit()

    mobile_number = sys.argv[1]
    count = sys.argv[2]
    body = {"action":"GetValidateCode","Mobile":mobile_number}

    i=0
    while i < int(count):
        response = request_ajax_url(url,body,referer,set_cookie)
        i=i+1

    if response.read() == "发送成功":
        print((" Send " + count + " Messages To " + mobile_number + " !!!"))

# get the goods msg with phantomjs
def get58city(url):
    print("=== GET 58 CITY")
    driver = webdriver.PhantomJS()
    f=open(input_urls_file,'r')
    for line in f.readlines():
        response=driver.get(line)
#        response=driver.get(u'https://www.amazon.com/')
#        response=driver.get(goodsitem)
        print('=== response')
        print(response)
        slp(1,5)
        data = driver.page_source
        print('=== type(data)')
        print((type(data)))
        pagecount=0
        while(True):
            f = codecs.open('./58city%d_%d.html'%(urlcount, pagecount), 'w+', 'utf8')
            f.write(data)
            slp(1,3)
            f.flush()
            f.close()
            list=driver.find_elements_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[8]/a')
            if(list==[]):
                print('list is none,this goods msg is over')
                break;
            for a in list:
                print('item obtained href')
                print((a.xpath('@href')))
                a.click()
                pagecount=pagecount+1
                print(('pages %d'%pagecount))
                slp(3,4)
                data = driver.page_source
                slp(3,4)
            print('one page getted, turn to the next')
            slp(5,9)
        urlcount=urlcount+1
    driver.quit()
    driver.close()

def get_taobao_pinglun(url):
    print("=== GET TAOBAO PINGLUN AJAX")
    driver = webdriver.PhantomJS()
    response=driver.get(url)
    print(response)
    data = driver.page_source
    list=driver.find_elements_by_xpath('//*[@id="J_TabBar"]/li[3]')
    print(list)
    driver.quit()
    driver.close()

def get_taobao_pinglun_selephan(url):
    print("=== GET TAOBAO PINGLUN AJAX")
    driver = webdriver.PhantomJS()
    response=driver.get(url)
    print(response)
    data = driver.page_source
    list=driver.find_elements_by_xpath('//*[@id="J_TabBar"]/li[3]')
    print(list)
    driver.quit()
    driver.close()

def saveHtml(file_name,file_content):
    with open (file_name,"wb") as f:
        f.write(file_content)

def getip():
        f=open('G:\cnn-text-classification-tf-master\cnn-text-classification-tf-master\ipaddr.txt','r')
        ct=random.randint(1,20)
        for line in f.readlines():
            ct=ct-1
            if(ct<1):
                print(line)
                return line

def makeMyOpener():
    cj = http.cookiejar.CookieJar()
    proxy = urllib.request.ProxyHandler({'http': getIp()})  # 设置proxy
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),proxy)
    myheader = hds[random.randint(0,len(hds)-1)]
    myheader['X-Requested-With']='XMLHttpRequest'
    print(myheader)
    opener.addheader=myheader
    return opener

#open new urls with new opener which change the header and proxy
def openurls(opener,url):
  response=opener.open(url, timeout=10)
  data=response.read()
  return data

def handle_data_from_response(data):
# print(soup)
  print('== HANDLE THE DATA')
  if False:
      save2file_linux(data)
  if True:
      print('== PIC THE DATA')
      picTheData(data)
      time.sleep(3)

  if False:
      print('== PIC THE DATA XPATH')
      picdata_xpath(data)

def save2file_linux(data):
    f = codecs.open('./%s.html'%(re.sub(r"[^A-Za-z0-9]", "", url)), 'w', chardet.detect(data)['encoding'])
    f.write("")
#    f.close()
    f = codecs.open('./%s.html'%(re.sub(r"[^A-Za-z0-9]", "", url)), 'a+', chardet.detect(data)['encoding'])
    f.write(data)
    f.flush()
    f.close()

def picdata_xpath(html):
          selector = etree.HTML(html)
  #while True:
          print('== GET ALL CONTENT')
          count=1
#      while True:
#          print('== ENTER INTO THE WHILE')
          links = selector.xpath('//*[@id="J_Reviews"]/div')
          count=count+1
          for link in links:
              print((links.xpath('string(.)').strip()))
              time.sleep(10)
#          for link in links:
#              print(link)
#              pass
#     links = selector.xpath('//*[@id="J_Reviews"]/div/div[7]/div/a[5]').click()



def picTheData(data):
    soup = BeautifulSoup(data, 'lxml')
    print('== CONVERT 2 SOUP')
    time.sleep(3)
    print((type(soup)))
    print('== GET THE TAOBAO DATA')
    print(soup)
    alist = soup.findAll('h4',attrs=({'class':'hd'}))
    for a in alist:
        print(a)
        if('累计评价' in str(a)):
            print('== READY to CLICK')
            (a.click())
            print('== CLICK TO SHOW CUSTOMS SAYS')
            data=openurls(opener,baseurl)
            print('== REFRESH THE DATA')
            handle_data_from_response(data)


#

def getIp():
    # getIP from server web.py json style
    opener = urllib.request.build_opener()
    response=opener.open("http://127.0.0.1:8000", timeout=20)
    dicts=(json.loads(response.read().decode()))
    i=random.randint(0,len(dicts))
    ip=str(dicts[i][0])+':'+str(dicts[i][1])
    print(ip)
    return ip


def obtain_url_ajax(i):
  return('https://rate.tmall.com/list_detail_rate.htm?itemId=528438367552&spuId=425112205&sellerId=2371805669&order=3&currentPage='+str(i)+'&append=0&content=1&tagId=&posi=&picture=&ua=090UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2FQHxHc0xxSHZLdSM%3D%7CU2xMHDJ7G2AHYg8hAS8WLgAgDlIzVTleIFp0InQ%3D%7CVGhXd1llXGhXa1BkW2ZfYVxiVWhKfkB7R31Jc0d6RnNOckhzS2Uz%7CVWldfS0RMQo%2BBycbIgIsRxU%2BHiAAPBlPaAV%2BE0NtO20%3D%7CVmhIGCUFOBgkGCwRMQ87ATwcIB8qFzcNMg8vEywZJAQ%2FBDlvOQ%3D%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D&isg=AhUVQDCc4aQyRsrc7Vt_hgLeJBEEGskkegTixpe6owzb7jfgTGLZ9COszkch&needFold=0&_ksTS=1492169207294_850&callback=jsonp851')

  #return('https://rate.tmall.com/list_detail_rate.htm?itemId=542064021808&spuId=459884056&sellerId=1710401270&order=3&currentPage='+str(i)+'&append=0&content=1&ua=132UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2FQHxHe0d%2BQHRNdiA%3D%7CU2xMHDJ7G2AHYg8hAS8WLgAgDlIzVTleIFp0InQ%3D%7CVGhXd1llXGhXa1BsUGlXY1phVmtJcU50TntCfEd7QX9EcUh8UgQ%3D%7CVWldfS0TMwc9BCQePhBqGUksEzccMmQy%7CVmhIGCUFOBgkGCwRMQg1DDQUKBciHz8FOgcnGyQRLAw3DDFnMQ%3D%3D%7CV29PHzEfP29Wb1BwT3FOd1dpU2lJdU5uUm1YeER%2BKAg1FTsVNQo%2BBjxqPA%3D%3D%7CWGFcYUF8XGNDf0Z6WmRcZkZ%2FX2NXAQ%3D%3D&isg=AhUVQDCc4aQyRsrc7Vt_hgLeJBEEGskkegTixpe6owzb7jfgTGLZ9COszkch&needFold=0&_ksTS=1492161147608_752&callback=jsonp753')

#  return ajaxbaseurl


def get_mb_ajax_json():
  print('test')
  print('get_mb_ajax_json')
  for i in range(1,1000):
    try:
      print(i)
      opener=makeMyOpener()
      data=openurls(opener,obtain_url_ajax(i))
      print(chardet.detect(data)['encoding'])
      f=codecs.open('./hair_ajaxtemp%d.txt'%i,'w',chardet.detect(data)['encoding'])
      f.write(data)
      f.flush()
      f.close()
      if (len(f)==None):
          print('0')
    except:
        pass


# func: this is used to download the customer-reviews from taobao
# the store's url address
'''https://detail.tmall.com/item.htm?id=531337104528&ns=1&abbucket=1&
sku_properties=5919063:6536025;12304035:21508;122216431:27772'''
if __name__=="__main__":
#  while True:
#    print('main+')
#    get_mb_ajax_json()
  for i in range(1,1000):
    try:
      print(i)
      opener=makeMyOpener()
      data=openurls(opener,obtain_url_ajax(i))
      print(chardet.detect(data)['encoding'])
      print(chardet.detect(data.read())['encoding'])
    except:
        pass
