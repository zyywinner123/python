# -*- coding=utf-8 -*-
import  os
import requests
f=open(os.getcwd()+'/'+'短评_好评.txt','w')
f.write('正文开始')
f.close()
r=requests.request('get','https://movie.douban.com/subject/26266893/comments')
requests.
print()
