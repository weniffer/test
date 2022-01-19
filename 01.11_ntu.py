# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:01:45 2022

@author: USER
"""

from bs4 import BeautifulSoup as bp

ntu="""<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>"""





s=bp(ntu,'lxml')
#print(s.prettify())

#for c in s.findAll('a'):
#    print(c.get("class"))


print('標題:',s.title)
print('第一個標籤a:',s.a)
print('第一個標籤b:',s.b)
print(s.find_all('a',{'class':'union'}))
print(s.find('a',{'id':'link2'}))
print(s.find('a',{'href':'http://www.ntust.edu.tw'}))
# search=s.find('a',{'id':'link1'})
# print(search.get('href'))
print((s.find('a',{'id':'link1'})).get('href'))
data=s.select(".union") #css語法 [.]=class
print(data[0].text)
print(data[1].text)
print(s.select('#link3')) #css語法 [#]=id












