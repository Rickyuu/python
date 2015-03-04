# coding: utf8  
import urllib2

url = 'http://ts2.mm.bing.net/th?id=HN.608051899405107882&w=210&h=149&c=7&rs=1&qlt=90&o=4&pid=1.7'
socket = urllib2.urlopen(url)
data = socket.read()
path = 'hats/tt.jpg'
with open(path, "wb") as jpg:
	jpg.write(data)
socket.close()

print 'Finish!'