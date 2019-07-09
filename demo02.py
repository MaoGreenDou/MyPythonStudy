#-*- utf-8 -*-

import  requests
from bs4 import BeautifulSoup
import  re

#抓取过程

r = requests.get('https://book.douban.com/subject/30281339/comments/')
print(r.status_code)        #正常的状态码是 200
print(r.text)               #解码方式有二进制，jason等。用text会自动选择

#解析过程

markup = ' <p class="title"><b>The little prince</b></p> '    #定义一个字符串用来测试

soup = BeautifulSoup(markup,'lxml')        #第二个参数用来选择解析方式 选lxml

#BeautifulSoup对象有四种， tag / navigable string / beautifulsoup / comment
#tag就是maruuo中的一些标签，ns就是标签当中的字符串，大部分bs都是tag，comment是tag的子类

print(soup.b)    # <b>The little prince</b>
print(soup.p)    # Out[12]: <p class="title"><b>The little prince</b></p>
print(type(soup.b))  # Out[13]: bs4.element.Tag

tag = soup.p
print(tag.name)    # Out[15]: 'p'

print(tag.attrs)   # tOut[16]: {'class': ['title']}

print(tag['class'])  # Out[17]: ['title']

print(tag.string)   # Out[18]: 'The little prince'

print(type(tag.string))    # Out[19]: bs4.element.NavigableString

soup.find_all('b')     # Out[20]: [<b>The little prince</b>]

#下面开始解析抓取到的《万物皆数》的书评中的短评 (用BeautifulSoup库)

soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('span','short')   #前一个参数是指定的标签，后一个参数是标签的属性
for item in pattern:
    print(item.string)

#下面开始解析抓取到的《万物皆数》的书评中的评分（用正则表达式，正则表达式方法常用来处理所要抓取的内容部分被替换的情况）

pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')    #用re的compile方法将指定的内容编译一个pattern实例
p = re.findall(pattern_s,r.text)    #用正则表达式的findall方法，在抓取到的内容中解析指定的内容
sum = 0;
for item in p:
    print('个人评分：',item)
    sum += int(item)
print(sum)



#总结：
#网络数据爬取的过程主要分两步：
#1.抓取  2.解析
#针对抓取过程，中小型的爬虫项目通常采用Request库（Anaconda已包含）
#针对解析过程，有两个库，一个是BeautifulSoup库，一个是re库（Anaconda均已包含）。其中，re库用来解决解析指定部分的内容
#上述两个过程的原理是：客户机向服务器发送request，服务器向客户机发送response，用户机进行解析即可
#需要注意的是一些网页的内容由js编写，无法直接通过爬取获得内容
#另外需要注意的一点是要实现查询网站的robots协议（可以通过百度资源查询）