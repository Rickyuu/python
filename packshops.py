# coding: utf8  
import urllib2

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	textpart = False
	titlepart = False
	count = 0
	f = open('packshops.txt', 'w')

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			if len(attrs) == 0:
				pass
			else:
				for(variable, value) in attrs:
					if variable == 'data-hippo-type':
						if value == 'shop':
							self.titlepart = True
						else:
							pass
					elif variable == 'title' and self.titlepart:
						self.f.write(value+',')
						self.titlepart = False
					else:
						pass
		elif tag == 'span':
			if len(attrs) == 0:
				pass
			else:
				for(variable, value) in attrs:
					if variable == 'class':
						if value == 'tag' or value == 'addr':
							self.textpart = True
						else:
							pass
					else:
						pass

	

	def handle_endtag(self, tag):
		if tag == 'span':
			self.textpart = False

	def handle_data(self, data):
		if self.textpart:
			self.count+=1
			if self.count == 3:
				self.f.write(data+'\n')
				self.count = 0
			else:
				self.f.write(data+',')


# 将url的不可变部分固定下来，并设置headers模拟浏览器身份访问网页，方式被403 Forbidden
# clothes
# url = 'http://www.dianping.com/search/category/2/20/g120p%d?aid=57f5c1b69be2798a2d593ffe88978885'
# supermarkets
# url = 'http://www.dianping.com/search/category/2/20/g187p%d?aid=d573689841d53e74033309968a481515&tc=1'
# jewelry
# url = 'http://www.dianping.com/search/category/2/20/g122p%d'
# digital products
url = 'http://www.dianping.com/search/category/2/20/g124p%d'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}

# 爬取所有北京的商店信息  
for i in range(15, 51):
    cur_url = url % (i)
    print cur_url 
    # 下载数据
    request = urllib2.Request(cur_url, '', headers)
    response = urllib2.urlopen(request)
    page_html = response.read()  
    # 数据打印
    myparser = MyHTMLParser()
    myparser.unescape("&#38472;&#39062;").encode("utf-8") 
    myparser.feed(page_html)
    myparser.close()
    print 'Done!', i

print 'Finish!'