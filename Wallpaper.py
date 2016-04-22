#-*- coding:utf-8 -*-
__author__ = 'Lynn'

'''
利用Python下载指定页面的图片

Author : Lynn Lau
Version : 1.0
Language : Python 2.7.10
IDE : Pycharm
'''
import urllib
import urllib2
import re

class DownIMG:

    def __int__(self):
        self.imgurl = "http://tieba.baidu.com/p/2460150866"

    def getHtml(self,pageIndex):
        url = "http://tieba.baidu.com/p/2460150866" +"?pn=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        HtmlCode = response.read()
        return HtmlCode

    def getcontent(self,pageIndex):
        page = self.getHtml(pageIndex)
        reg = r'<img.*?pic_type="0".*?class="BDE_Image".*?src="(.*?)".*?width="560">'
        contentreg = re.compile(reg,re.S)
        contentlist = re.findall(contentreg,page)
        name = 0
        for imgURL in contentlist:
            urllib.urlretrieve(imgURL,'%s.jpg' %name)
            name+=1
            print imgURL

spider = DownIMG()
spider.getcontent(1)