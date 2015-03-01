# coding: utf8  
import urllib2  
import re  

url = 'http://www.dianping.com/search/category/2/20/g120p%d?aid=57f5c1b69be2798a2d593ffe88978885'
filename = 'page%d.html'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}

# 定向爬去10页最新的视频资源  
for i in range(1, 4):  
    cur_url = url % (i)
    print cur_url
    cur_filename = filename % (i)  
    # 下载数据
    request = urllib2.Request(cur_url, '', headers)
    response = urllib2.urlopen(request)
    page_html = response.read()  
    # 数据保存本地
    fp = file(cur_filename, 'w')
    fp.write(page_html)
    fp.close()
    print 'Done!', i

print 'Finish!'
