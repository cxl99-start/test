#爬虫的的关键：请求、提取、自动化

#发起请求：
    #通过http库向目标站点发起请求，也就是发送一个Request，请求可以包含额外的header等信息，等待服务器响应

#获取响应内容：
    #如果服务器能正常响应，会得到一个Response,Response的内容便是所获取的页面内容，类型可能是HTML，Json字符串、二进制数据等

#解析内容：
    # 得到的内容可能是HTML，可以用正则表达式，页面解析库进行解析，可能是Json，可以直接转换为Json对象解析，可能是二进制数据，可以做保存或者进一步的处理

#保存数据：
    # 保存形式多样，可以存为文本，也可以保存到数据库，或者保存特定格式的文件


# region 基本流程
'''
浏览器发送消息给网址所在的服务器，这个过程就叫做HTTP Request
服务器收到浏览器发送的消息后，能够根据浏览器发送消息的内容，做相应的处理，然后把消息回传给浏览器，这个过程就是HTTP Response

1、Request
请求方式：
    主要有：GET/POST两种类型常用，另外还有HEAD/PUT/DELETE/OPTIONS
    Get和Post的区别：请求的数据get是在url中，post则是存放在头部

    GET和POST的区别就是：请求的数据GET是在url中，POST则是存放在头部

    GET:向指定的资源发出“显示”请求。使用GET方法应该只用在读取数据，而不应当被用于产生“副作用”的操作中，例如在Web Application中。其中一个原因是GET可能会被网络蜘蛛等随意访问

    POST:向指定资源提交数据，请求服务器进行处理（例如提交表单或者上传文件）。数据被包含在请求本文中。这个请求可能会创建新的资源或修改现有资源，或二者皆有。

    HEAD：与GET方法一样，都是向服务器发出指定资源的请求。只不过服务器将不传回资源的本文部分。它的好处在于，使用这个方法可以在不必传输全部内容的情况下，就可以获取其中“关于该资源的信息”（元信息或称元数据）。

    PUT：向指定资源位置上传其最新内容。

    OPTIONS：这个方法可使服务器传回该资源所支持的所有HTTP请求方法。用'*'来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。

    DELETE：请求服务器删除Request-URI所标识的资源。

请求URL：
    URL的格式由三个部分组成：
    第一部分是协议(或称为服务方式)。
    第二部分是存有该资源的主机IP地址(有时也包括端口号)。
    第三部分是主机资源的具体地址，如目录和文件名等。

请求头：
    包含请求时的头部信息，如User-Agent、Host、Cookies等信息

请求体：
    请求时携带的数据，如提交表单数据时候的表单数据（POST）


2、Response：所有http响应的第一行都是状态行，依次是当前http版本号，3位数字组成的状态码，以及描述状态的短语，彼此由空格分隔
响应状态：
    有多种响应状态，如：200代表成功，301跳转，404找不到页面，502服务器错误
    1xx消息——请求已被服务器接收，继续处理
    2xx成功——请求已成功被服务器接收、理解、并接受
    3xx重定向——需要后续操作才能完成这一请求
    4xx请求错误——请求含有词法错误或者无法被执行
    5xx服务器错误——服务器在处理某个正确请求时发生错误
     常见代码：
         200 OK 请求成功
         400 Bad Request 客户端请求有语法错误，不能被服务器所理解
         401 Unauthorized 请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
         403 Forbidden 服务器收到请求，但是拒绝提供服务
         404 Not Found 请求资源不存在，eg：输入了错误的URL
         500 Internal Server Error 服务器发生不可预期的错误
         503 Server Unavailable 服务器当前不能处理客户端的请求，一段时间后可能恢复正常
         301 目标永久性转移
         302 目标暂时性转移

响应头：
    如内容类型，类容长度，服务器信息，设置cookie，如下图

响应体：
    最主要的部分，包含请求资源的内容，如网页HTML，图片，二进制数据等

能爬取的数据：
    1、网页文本：如HTML文档，Jaon格式化文本等
    2、图片：获取到的是二进制文件，保存为图片格式
    3、视频：同样是二进制文件
    4、只要请求到的，都可以获取

如何解析数据：
    1、直接处理
    2、Json解析
    3、正则表达式处理
    4、BeautifulSoup解析处理
    5、PyQuery解析处理
    6、XPath解析处理

关于抓取的页面数据和；浏览器看到的不一样的问题：
    出现这种情况可能是因为网站的的数据是通过js、ajax动态加载的，所以直接通过get请求获取的页面和浏览器显示的不同。
    解决js渲染的问题：
    分析ajax
    Selenium/webdriver
    Splash
    PyV8,Ghost.py

保存数据：
    文本：纯文本、json、Xml等
    关系型数据库：mysql，serversql、oracle等结构化数据库
    非关系型数据库：MongoDB,Redis等key-value形式存储

    '''
# endregion

# region Urllib模块

'''
Urllib是python内置的HTTP请求库，包含一下模块：
    urllib.request 请求模块
    urllib.error 异常处理模块
    urllib.parse url解析模块
    urllib.robotparser robots.txt解析模块
'''
#urllib.request.urlopen参数的介绍
# urllib.requst.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

#urlopen

# url参数的使用：
'''
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
data1=response.read().decode('utf-8')
print(data1)
'''
    #urlopen一般常用的三个参数，urllib.request.urlopen(url,data,timeout)
    #response.read()可以获取到网页的内容，如果没有read（），将返回如下内容

#data参数的使用：
import urllib.parse    #解析模块
import urllib.request  #请求模块
    #通过bytes（urllib.parse.urlencode()）可以将post数据进行转换到urllib.request.urlopen的data参数中。
    # 这样就完成了一次post请求。
    #添加了data参数就是post请求方式；没有data参数就是get请求方式
'''
data2=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
print(type(data2))
response=urllib.request.urlopen('http://httpbin.org/post',data=data2)
data3=response.read()
print(data3)
'''

#timeout参数的使用：
    #在网络情况不好的情况下，会出现请求慢或者是请求异常的情况，这个时候我们可以给请求设置一个超时时间，不让程序一直等待
'''
import urllib.error
import socket
try:
    response=urllib.request.urlopen('http://httpbin.org/post',data=data2,timeout=0.1)
    data4=response.read()
    # print(data4)
except urllib.error.URLError as e:  #对异常进行抓取
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
'''

#响应
    #响应类型、状态码、响应头
'''
import urllib.request
response=urllib.request.urlopen('https://www.python.org')
 print(type(response))
'''

    #可以看到结果为：<class 'http.client.httpresponse'="">
    # 我们可以通过response.status、response.getheaders().response.getheader("server")，获取状态码以及头部信息
    # response.read()获得的是响应体的内容
    #上述urlopen只能用于简单的请求，因为无法添加一些header信息，写爬虫很多情况下是需要添加头部去访问信息网站，这时候需要用到request

#Request
#设置Headers：有很多网站为了防止程序爬虫造成网站瘫痪，会需要携带一些headers头部信息才能访问，最常见的有user-agent参数
'''
import urllib.request
request=urllib.request.Request('https://python.org')
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''

    #给请求添加头部，从而定制自己请求网站时的头部信息
    #第一种方法:
        # 1、定义请求地址，定义请求头部信息
        #2、把请求传入的数据，转换成bytes
        #3、Request请求，传入地址，data，头部，和确定访问方式（get或者是post）
        #4、urlopen请求打开网站
        #5、read（）读取网页内容
'''
from urllib import request,parse
url='http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}
dict={
    'name':'zhaofan'
}
data=bytes(parse.urlencode(dict),encoding='utf-8')
req=request.Request(url=url,data=data,headers=headers,method='post')
response=request.urlopen(req)
print(response.read().decode('utf-8'))
'''

    #第二种方法
        # 1、定义请求地址，定义请求传入信息
        #2、把请求传入的数据，转换成bytes
        #3、Request请求，传入地址，和确定访问方式（get或者是post）
        #4、通过add_header的方式，添加自定义头部信息
        #5、urlopen请求打开网站
        #6、read（）读取网页内容
'''
from urllib import request,parse
url='http://httpbin.org/post'
dict={
    'name':'zhaofan'
}
data=bytes(parse.urlencode(dict),encoding='utf-8')
req=request.Request(url=url,data=data,method='POST')
req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# req.add_header('Host','ceshi.org')
response1=request.urlopen(req)
print(response1.read().decode('utf-8'))
'''

#高级用法各种handler
# 1、代理，ProxyHandler
    #通过urllib.request.ProxyHandler()可以设置代理，网站它会检测某一段时间某个ip的访问次数
    # 如果访问次数过多，它会禁止你的访问，所以这个时候就要通过用代理来爬取数据
''' 网址问题
import urllib.request
proxy_handler=urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})
opener=urllib.request.build_opener(proxy_handler)
response=opener.open('http://httpbin.org/get')
print(response.read())

'''

#2、cookie、HTTPCookiProcessor
    #cookie中保存着我们常见的登陆信息，有时候需要爬取网站需要携带cookie信息访问，这里用到了http.cookijar，用于获取cookie以及存储cookie

    #获取cookie：
        #1、调用CookieJar（）函数
        #2、调用HTTPCookieProcessor函数，传入调用CookieJar实例对象
        #3、调用build_opener函数，传入HTTPCookieProcessor实例
        #4、build_opener实例.open（网站地址）
        #5、for循环CookieJar实例，获取cookie信息
'''
import http.cookiejar,urllib.request
cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
for i in cookie:
     print(i.name+'='+i.value)
'''

    # 存入cookie，有两种方式http.cookiejar.MozillaCookieJar和http.cookiejar.LWPCookieJar()
    #http.cookiejar.MozillaCookieJar()方法：
        # 1、定义文件名称
        # 2、MozillaCookieJar（），传入调用文件名对象
        # 3、调用HTTPCookieProcessor函数，传入MozillaCookieJar实例对象
        # 4、调用build_opener函数，传入HTTPCookieProcessor实例
        # 5、build_opener实例.open（网站地址）
        # 6、MozillaCookieJar实例对象.save(ignore_discard=True,ignore_expires=True)
'''
import http.cookiejar
filename='cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''

    #http.cookiejar.LWPCookieJar()方法（）：
        # 1、定义文件名称
        # 2、LWPCookieJar（），传入调用文件名对象
        # 3、调用HTTPCookieProcessor函数，传入LWPCookieJar实例对象
        # 4、调用build_opener函数，传入HTTPCookieProcessor实例
        # 5、build_opener实例.open（网站地址）
        # 6、LWPCookieJar实例对象.save(ignore_discard=True,ignore_expires=True)
'''
import http.cookiejar
filename='cookie1.txt'
cookie=http.cookiejar.LWPCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''

    #获取cookie文件中的信息，通过load方式，哪种写入方式，就用哪种方式读取
'''
import http.cookiejar,urllib.request
cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
'''

#异常处理：
    #很多时候我们通过程序访问页面的时候，有的页面可能会出现错误，这时候我们需要捕捉异常
'''
from urllib import request,error
try:
    response=request.urlopen('http://pythonsite.com/1111.html')
except error.URLError as e:
    print(e.reason)
'''

    #urllib里面有两个异常错误：
        # 1、URLError、HTTPError：HTTPError是URLError的子类
        # 2、URLError：只有一个属性，就是reason，类似上面的例子
        # 3、HTTPError：三个属性，code、reason、headers，即抓异常的时候可以获得code、reason、headers三个信息，例子如下：
'''
from urllib import request,error
try:
    response=request.urlopen('http://pythonsite.com/1111.html')
except error.HTTPError as e:
    print('这是reason：',e.reason)
    print('这是code：',e.code)
    print('这是headers：',e.headers)
except error.URLError as e:
    print('这是reason：',e.reason)
else:
    print('request Successfully')
'''

    #同时也可以在e.reason中做深入的判断：
'''
import socket
from urllib import request,error
try:
    response=request.urlopen('http://www.pythonsite.com/',timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('time out')
'''

#URL解析
    # 1、urlparse：
        #urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
        #这里可以对你传入的url地址进行拆分
        #同时，我们可以指定协议类型，通过scheme，但是如果原本的url中已经带了协议，设置就无效
'''
from urllib.parse import urlparse
result=urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)
'''

    # 2、urlunpars：与urlparse功能相反，它是用于拼接：
'''
from urllib.request import urlunparse
data=['http','www.baidu.com','index.html','user','a=123','commit']
print(urlunparse(data))
'''

    # 3、urljoin：做拼接:如果拼接时，传入多个url，后面的url优先级是高于前面的url
'''
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://pythonsite.com/FAQ.html'))
'''

    #urlencode：这个方法可以将字典转换成url参数
'''
from urllib.parse import urlencode
params={
    'name':'zhaofan',
    'age':23
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)
'''

# endregion

# region Requests模块

# Requests：是用python语言基础urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库，requests是python实现的最简单易用的HTTP库
    #有很多网站直接用response.text会出现乱码的问题，可以使用response.content
    #response.context返回的数据格式是二进制格式，可以通过decode（'utf-8'）转换成utf-8，就解决了乱码的问题
import requests   #需要另外安装pip
'''
response=requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode('utf-8'))
'''

    #请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。
    # 当你访问 response.text 之时，Requests 会使用其推测的文本编码。
    # 你可以找出 Requests 使用了什么编码，并且能够使用 response.encoding 属性来改变它
'''
response=requests.get('http://www.baidu.com')
response.encoding='utf-8'
print(response.text)
'''

# 请求方式：requests里面提供了各种请求方式；post、put、delete、head、options.....
import requests
    # 1、基本get请求方式：
'''
response=requests.get('http://httpbin.org/get')
response.encoding='utf-8'
print(response.text)
'''
        #1.1、带参数的get请求
'''
response=requests.get('http://httpbin.org/get?name=zhaofan&age=23')
print(response.text)
'''
        #如果想要在URL查询字符串传递数据，通常会以“网站地址/get?key=val”方式传递
        #Requests模块允许使用params关键字传递参数，以一个字典来传递这些参数，但是，如果字典中的参数为None，不会添加到url上，如下：
'''
import requests
data={
    'name':'zhaofan',
    'age':25
}
response=requests.get('http://httpbin.org/get',params=data)
print(response.text)
'''

        #1.2、解析json
'''
import requests,json
response=requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
'''

        #1.3、获取二进制数据：可以通过response.content获取二进制数据，同样也可以用于下载图片以及视频资源

        #1.4、添加headers：在谷歌浏览器里面输入chrome://version，就可以看到用户代理，将用户代理添加到头部信息
'''
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
response=requests.get('http://www.zhihu.com',headers=headers)
print(response.text)
'''

    # 2、基本的post请求：在发生请求时，添加一个data参数，这个data参数可以通过字典构成
'''
import requests
data={
    'name':'zhaofan',
    'age':25
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
response=requests.post('http://httpbin.org/post',data=data,headers=headers) #也可以像get请求一样通过headers参数传递一个字典类型的数据
print(response.text)
'''

        #2.1、响应：我们可以通过response获得很多属性，如下：
'''
import requests
response=requests.get('http://www.baidu.com')
print(type(response.status_code),response.status_code)  #响应状态码
print(type(response.headers),response.headers)   #头部信息
print(type(response.cookies),response.cookies)   #cookie信息
print(type(response.url),response.url)    #url地址
print(type(response.history),response.history)
'''

        # 2.2、状态码判断
'''
import requests
response=requests.get('http://www.baidu.com')
if response.status_code==200 or response.status_code==requests.codes.ok:  #两种判断方式都一样，但是通过状态码去判断更方便
    print('访问成功！')
'''

    # 3、requests的高级用法
        #3.1、文件上传，和其他方法类似，也是构造一个字典，然后通过files参数传递
'''
import requests
files={'files':open('E:\图片\演示.png','rb')}
response=requests.post('http://httpbin.org/post',files=files)
print(response.text)
'''

        # 3.2、获取cookie
'''
response=requests.get('http://www.baidu.com')
print(response.cookies)
for i,v in response.cookies.items():
    print(i+'='+v)
'''

        # 3.3、会话持续：cookie的一个作用就是用于模拟登陆，做会话持续
        #因为这种方式是两次requests请求之间是独立的，而第一次是创建一个session对象，两次请求都通过这个对象访问
'''
import requests
s=requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456')
response=s.get('http://httpbin.org/cookies')
print(response.text)
'''

        #3.4、证书验证：现在很多网站都是通过https的方式访问，这个时候就设计到证书的问题
        #如果证书验证不通过的情况下，可以通过verify=False,可以去访问页面，当然也可以通过cert参数放入证书路径，具体例子如下
'''
import requests
import urllib3
urllib3.disable_warnings()
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
'''

        #3.5、代理设置
'''
import requests
proxies={
    'http':'http://127.0.0.1:9999',
    'https':'http://127.0.0.1:8888'
}
response=requests.get('https://www.baidu.com',proxies=proxies)
print(response.text)

如果代理需要设置账户名和密码,只需要将字典更改为如下：
proxies = {
"http":"http://user:password@127.0.0.1:9999"
}
如果你的代理是通过sokces这种方式则需要pip install "requests[socks]"
proxies= {
"http":"socks5://127.0.0.1:9999",
"https":"sockes5://127.0.0.1:8888"
}

'''

        #3.6、超时设置，通过timeout参数设置超时时间
'''
import requests
response=requests.get('http://www.baidu.com',timeout=1)
response.encoding='utf-8'
print(response.text)
'''

        #3.7、认证设置：如果碰到需要认证的网站可以通过requests.auth模块实现
'''
import requests
from requests.auth import HTTPBasicAuth
response=requests.get('https://www.12306.cn',auth=HTTPBasicAuth('user','123'))
print(response.status_code)
'''
        #另一种方式：
'''
response=requests.get('https://www.12306.cn',auth=('user','123'))
print(response.status_code)
'''

        # 3.8、异常处理：所有的异常都是在requests.excepitons中
'''
from requests.exceptions import ConnectionError,RequestException,ReadTimeout
import requests
try:
    response=requests.get('http://httpbin.org/get',timeout=0.000001)
    print(response.status_code)
except ReadTimeout as e:
    print('timeout')
except ConnectionError as e:
    print('ConnectionError')
except RequestException as e:
    print('RequestException')
'''

# endregion

# region 正则表达式的基本使用

#正则表达式：对字符串操作的一种逻辑公式，事先定义好一些特殊字符、及特殊字符的组合，组成一个规则字符，用来过滤字符
    #python中的正则，封装了re模块

    # 1、re.match():尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
        #语法格式：re.match(pattern,string,flags=0)

        # 1.1、常规匹配
'''
import re
content= "hello 123 4567 World_This is a regex Demo"
result=re.match('^\w{5}\s\d{3}\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())   #获取匹配结果
print(result.span())    #获取匹配字符串的长度范围
'''

        # 1.2、泛匹配
'''
result=re.match('^hello.*Demo$',content)
print(result.group())
'''

        # 1.3、匹配目标，分组，group()
import re
'''
content= "hello 123 4567 World_This is a regex Demo"
result= re.match('^hello\s(\w+)\s(\w+)\sWorld.*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
'''
        #1.4、贪婪匹配
'''
content= "hello 1234567 World_This is a regex Demo"
result=re.match('^hello.*(\d+).*Demo$',content)   #贪婪匹配，.*会将7以前的数字尽量的匹配，所以\d+只能匹配到7
print(result)
print(result.group(1))

results=re.match('^hello.*?(\d+).*Demo$',content)  #非贪婪匹配
print(results)
print(results.group(1))
'''
        #1.5、匹配模式
            # 1、re.S可以匹配换行的内容
            # 2、当我们要匹配的内容中存在特殊字符的时候,就需要用到转义符号\
'''
content = """hello 123456 world_this
my name is zhaofan
"""
tesu="price is $5.00"
result=re.match('^he.*?(\d).*?zhaofan$',content,re.S)
su=re.match('^price is \$5\.00',tesu)
print(result)
print(result.group())

print(su)
print(su.group())
'''
        # 小结：尽量使用泛匹配，使用括号得到匹配目标，尽量使用非贪婪匹配模式，有换行符就用re.S

    # 2、re.search：扫描整个字符串返回第一个成功匹配的结果
        # match必须匹配头部，所以我们更多的用search，不需要写 ^ 和 $
'''
content='extra things hello 123456 world_this is a Re Extra things'
result=re.search("hello.*?(\d+).*Re",content)
print(result)
print(result.group())
print(result.group(1))
'''

    # 3、re.findall：搜索字符串，以列表的形式返回全部能匹配的子串
import re
'''
html = '<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'
result=re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
for i in result:   #findall获得是的是一个列表，需要循环去获取列表中的值
    print(i[0],i[1],i[2])    
'''

    # 4、re.sub 替换字符串中每一个匹配的子串后返回替换后的字符串
content1="Extra things hello 123455 World_this is a regex Demo extra things"
# print(re.sub('\d+',"",content1))
        #在某些情况下，我们需要获取我们匹配的字符串，然后在后面添加一些内容，可以通过下面的方式：
import re
content1="Extra things hello 123455 World_this is a regex Demo extra things"
# print(re.sub('(\d+)',r'\1 7890',content1))     #这里的\1是获取第一个匹配的结果，为了防止转义字符的问题在前面加上r

    # 5、re.compile：将正则表达式编译成正则表达式对象，方便复用该正则表达式
'''
content1=hello 12345 word_this
123 fan

pattern=re.compile('hello.*fan',re.S)
resut=re.match(pattern,content1)
print(resut)
print(resut.group())

import requests
con=requests.get("https://book.douban.com").text
# prame=re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results=re.findall(pattern,con)
print(results)
for result in results:
    url,name,auttor,date=result
    auttor=re.sub('\s','',auttor)
    date = re.sub('\s', '', date)
    print(url,name,auttor,date)
'''

# endregion

# region BeautifulSoup库的使用
    # BeautifulSoup：一个灵活又方便的网页解析库，处理高效，支持多种解析器
from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')     #html.parser  python标准库
# print(soup.prettify())   #获取整个BeautifulSoup对象
# print(soup.title)     #获取title标签
# print(soup.title.name)    #获取title标签的名称，即title本身
# print(soup.title.string)    #获取title标签中的内容
# print(soup.title.parent.name)   #获取title标签的父级标签的名称
# print(soup.p)       #获取p标签
# print(soup.p["class"])     #获取p标签的class
# print(soup.a)     #获取a标签
# print(soup.find_all('a'))     #获取所有的a标签
# print(soup.find(id='link3'))    #获取id等于link3的标签
    #标签选择器：
    #需要注意，如果通过soup.标签的方式获取标签内容，返回的是第一个标签的内容，不能获取所有的，需要通过其他属性去获取

    #获取名称： soup.title.name
    #获取属性：soup.p["class"])
    #获取内容：soup.title.string
    #嵌套选择：soup.head.title.string

    #子节点和子孙节点：
        #contents的使用：将获取到的标签存入到一个列表
# print(soup.p.contents)

        #children的使用：获取标签下所有子节点内容，只是通过children获取到的是一个可迭代对象，只能用过for循环获取有用信息
# for i,child in enumerate(soup.p.children):
#     print(i,child)

        #通过contents和children都是获取子节点，如果想要获取子孙节点可以通过descendants，获取的结果也是一个迭代器

    #父节点和祖先节点：通过soup.标签.parent获取父节点的信息
        #通过list(enumerate(soup.a.parents))可以获取祖先节点

    #兄弟节点
soup.a.next_siblings   #获取后面的兄弟节点
soup.a.previous_siblings   #获取前面的兄弟节点
soup.a.next_sibling    #获取下一个兄弟标签
soup.a.previous_sinbling     #获取上一个兄弟标签

    # find_all
        # find_all(name,attrs,recursive,text,**kwargs)
        # 可以根据标签名，属性，内容查找文档

        #1、name的用法
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))

    #2、attrs用法：可以传入字典的方式来查找标签，但是这里class是特殊的，因为python本身这个关键字，所以要查找class的关键字
        #attrs={'class_':'element'}或者soup.find_all('',{"class":"element}),特殊标签属性可以不写attrs，列如id
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name','element'}))

    #3、text：返回结果是查询到的指定的text的文本
# print(soup.find_all(text='Foo'))

    #4、find：find返回匹配结果的第一个元素
        #find_parents()返回所有祖先节点，find_parent()返回父节点
        #find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点
        #find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点
        #find_all_next()返回节点后所有符合条件的节点，find_next()返回第一个符合条件的节点
        #find_all_previous()返回节点后所有复合条件的节点，find_previous()返回第一个符合条件的节点

    # CSS选择器：通过select()直接传入css选贼器就可以完成选择
# print(soup.select('.panel .panel-heading'))
# print(soup.select('#list-1 .element'))
# print(soup.select('ul')[0])

    #获取内容：通过get_text()就可以获取文本内容
# for i in soup.select('li'):
#     print(i.get_text())

    #获取属性：可以通过[属性名]或者attrs[属性名]
# for i in soup.select('ul'):
    # print(i['id'])
    # print(i.attrs['id'])


# endregion

# region PyQuery库的使用

#初始化：一般有三种传入方式：传入字符串，传入url，传入文件
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
# print(doc)
# print(type(doc))
# print(doc('li'))

    #我们可以通过doc进行元素的选择，比如获取class：doc('.class_name'),id：doc('#id_name')

#url初始化
doc=pq(url='http://www.baidu.com',encoding='utf-8')
print(doc('head'))

#文件初始化：在pq（）里面可以传入文件参数，这里的文件通常是一个html文件

#查找元素
    #1、子元素：children，find





# endregion