# -*- coding： utf-8 -*-



# region 循环、循环练习
a=[1,'1233',0.2]#列表 list
b=(1,'1233',0.2)#元组 tupe
c={'name':'Tom','Age':'21'}#字典 dict
d={'happy','bed','age','Tom'}#集合

print(type(a))#type（变量）输出变量类型，在python中不用申明变量类型，系统会自动分配
print(type(b))
print(type(c))
print(type(d))

#斐波纳契数列
a,b=0,1#给变量赋值
i=0#控制循环次数
while i<20:
    print(b)
    i=i+1
    a,b=b,a+b

#求和
sum=100
a=0
i=1
while i<=sum:
    a=a+i
    i=i+1
print('总和是',a)

#循环 while 条件：循环体   for  变量 in 需要循环的值： 循环体
list=['name','age','adress','sex']
for name in list:
   if name=='name':
       print(name)

 #range（）函数
for s in range(1,5):
    print(s)
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

#迭代器有两个基本的方法：iter() 和 next()
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
i=0
while i<3:
    try:
        print(next(it))
        i=i+1
    except StopIteration:
        sys.exit()


import sys

def fibonacci(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        sys.exit()

aa=int(input("请输入长："))
bb=int(input("请输入宽："))
def area(width, height):
    return width * height
print('%s与%s相乘的结果是%s'%(aa,bb,area(aa,bb)))


la=[1,2,3,4,5]
la[2]='x'
i=0
print(la.len())
while i>la.count():
    print(la[i])
    i=i+1
# endregion

#在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。


#参数

# region 函数参数
#1、必须参数

def nixu(str):
    "这是必须参数函数"
    print(str)
    return
nixu('必须参数函数')#不传参数就会报错

#2、关键字参数
def guan(str):
    print(str)
    #return
guan(str='这是关键字参数')

#俩个* 函数，加了两个星号 ** 的参数会以字典的形式导入，关键字参数
def lia(a,**b):
    print(a)
    for s in b:
        print(s)
    return

lia(10,name='包',age='22')

#3、在调用函数时，不需要使用指定顺序
def duo(name,age):
    print("你的名字是：%s，年龄为：%s"%(name,age))
    return

duo(name=input("请输入你的名字："),age=input("请输入你的年龄："))

#不定长参数
# 一个*函数，加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量

def yuan(a,*b):
    print(a,b)
    return
yuan(10,20,30)
yuan(10)

#命名关键字参数
#如果单独出现星号 * 后的参数必须用关键字传入,否则就会报错
def dan(a,b,*,c):
    return  a+b+c
print(dan(1,2,c=3))

'''
----匿名函数
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''

#lambda [arg1 [,arg2,.....argn]]:expression
c=lambda a,b:a+b
print('相加的结果：',c(10,30))
# endregion


#变量作用域
#Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

#变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

#L （Local） 局部作用域
#E （Enclosing） 闭包函数外的函数中
#G （Global） 全局作用域
#B （Built-in） 内建作用域
#以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，
# 再者去内建中找Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，
# 外部也可以访问，如下代码：

def wai():
    str="你的名字是什么"

print(str)

a=0
def sum(c,d):
    a=c+d
    print('局部变量：',a)
    return  a

sum(10,2)
print("全局变量：",a)


a = [66.25, 333, 333, 1, 1234.5]
print(a.count(66.25),a.count(333))
a.insert(3,45000)#在指定索引位置添加元素
a.append(52.5)#在列表最后添加一个元素
print(a)
a.index(333)# 返回列表中第一个指定的值，如果没有匹配元素，就会返回一个错误
a.remove(1)
print(a)
#a.reverse()
a.sort()
print(a)

#列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，
# 最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。
# 用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
[x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
[x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
print([vec1[i]*vec2[i] for i in range(len(vec1))])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print([[row[i] for row in matrix]for i in range(len(matrix[1]))])


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket )


a = {x for x in 'abracadabra' if x not in 'ar'}
print(a)


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
 print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)



#同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(answers,questions):
 print('What is your {0}?  It is {1}.'.format(q, a))

print(questions)
questions.reverse()
print(questions)

for i in reversed(range(1,10,3)):
    print(i)

    # 列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边  # 第一条语句是最后一层。

[x * y for x in range[1, 5] if x > 2 for y in range[1, 4] if x < 3]
#他的执行顺序是


print([x * y for x in range(1, 5) if x > 2 for y in range(1, 4) if y < 3])

for x in range(1, 5):
    if x > 2:
        for y in range(1, 4):
            if y< 3:
                print(x * y)


#有多个列表需要遍历时，需要zip，除了用'{0}{1}'.format(q,a)的方法，还可以使用%s方法（两者效果一样一样的）：注意是.format
a='你的名字：'
b='你的性别：'
name=input('请输入你的名字：')
age=input('请输入你的性别：')

print('%s%s，%s%s'%(a,name,b,age))



#在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就
# 都消失了。
#为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
#模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。
# 这也是使用 python 标准库的方法。

import  sys
print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')



#判断是否闰年（满足年份模400为0，或者是模4为0但模100不为0）
age=int(input('请输入你要判断的年份：'))
if (age%400==0 or (age%4==0 and age%100!=0 )):
    print('%s是闰年'%age)


#计算等式
a=12*34+78-132/6
b=(12*(34+78)-132)/6
c=(86/40)**5
print('12*34+78-132/6=%d'%a)
print('(12*(34+78)-132)/6=%d'%b)
print('(86/40)**5=%d'%c)

import math
x=math.fmod(145,23)
print(x)
print(math.cos(0.5))
print(math.sin(0.5))


from math import sqrt



# 基本的方法
#0-100之间的素数
N=100
sum=[]
for a in range(2,100):#产生
    f=True
    for b in range(2,int(sqrt(a)+1)):
        if a%b==0:
            f=False
            break
    if f:
        sum.append(a)
print(sum)

#列表推导式的方法
result2 = [ p for p in range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]
print(result2)

sum1=[]
for a in range(2,100):#产生
    f=True
    for b in range(2,int(sqrt(a)+1)):
        if a%b==0:
            f=False
            break
    if f:
        sum1.append(a)
print(sum1)



import  os
print(os.listdir('F:/文档/绩效表/月初'))

for root, dirs, files in os.walk('F:/文档/绩效表/月初'):
    print (root,dirs,files )



import os
for wen,lu,file in os.walk('F:/文档/绩效表/月初'):
    open('mycd.cdc ','a').write('%s%s%s'%(wen,lu,file))


#数字（number）
for a in range(0,10):
    print(a)

#字符串
a='123456'
for s in a:
    if s=='3':
        print('1111')
    else :
        print('222')

#列表[]
yuan=['tom','milk','jery','jick']
for a in yuan:
    print(a)

#元组()
lie=('item1','item2','item3','item4')
for l in lie:
    print(l)

#字典   字典是支持无限极嵌套的，如下面代码：{'key':'value'}
cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for s in cities['河北']['石家庄']:
    print(s)

#集合
ji={'小门','小蓝','小青','小北'}
for s in ji:
    print(s)



t=('参数1','参数2','参数3')
i=0
while i<5:
    try:
        i=i+1
        print(t[3])
    except Exception as e:
        print('对不起，语句异常！')



try:
    msg = input(">>")
    print(int(msg))
except Exception as e:
    print("异常的类型是:%s"%type(e))
    print("异常的内容是:%s"%e)
else:
    print('如果代码块不抛出异常会执行此行代码!')
finally:
    print('不管代码块是否抛出异常都会执行此行代码!')


class test:
    name='加菲猫'
    def Yuyan(self):
        return '你最近怎么样，'

a=test()

print('(｡･∀･)ﾉﾞ嗨，%s，%s过的还好吗？'%(a.name,a.Yuyan()))



#单继承
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()




# 在访问属性以及的时候，一定要用self.属性名  来访问
class people:
    name=''
    age=0
    sex=''
    def __init__(self,n,a,s):
        self. name=n
        self. age=a
        self.sex=s
    def ziwojieshao(self):
        print('我是%s，今年%s岁，性别%s'%(self.name,self.age,self.sex))

#单继承
class student(people):
    nian=''
    def __init__(self,n,a,s,na):
        #调用父类得构造函数
        people.__init__(self,n,a,s)
        self.nian=na
    #覆写父类方法
    def ziwojieshao(self):
            print('我是%s，今年%s岁，性别%s,现在在读小学%s年级'%(self.name,self.age,self.sex,self.nian))


sum=student('Tom',10,'女','4')
sum.ziwojieshao()


#先准备类一个多继承的类
class family():
    b=''
    Mom=''
    def __init__(self,b,m):
        self.b=b
        self.Mom=m
    def jia(self):
        print('我的爸爸是%s，妈妈是%s'%(self.b,self.Mom))

#多继承
class jiang(student,family):
    def __init__(self,n,a,s,na,b,m):
        student.__init__(self,n,a,s,na)
        family.__init__(self,b,m)


test=jiang('Tom',10,'女','4','Jick','Rose')
test.ziwojieshao()
test.jia()



#类的属性与方法

#不使用第三方变量，实现两个变量之间的值的转换
a=10
b=11
print('a=%s，b=%s'%(a,b))
a=a+b#21
b=a-b
a=a-b
print(a,b)

#正则表达式
import re
tell='0716-452-821 # 这是一个电话号码'

#删除指定的字符串
shan=re.sub(r'#.*$',"",tell)
print('电话号码：%s'%shan)

#删除非数字字符串
fei=re.sub(r'\D',"",tell)
print('电话号码：%s'%fei)



#compile函数，compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
# 供 match() 和 search() 这两个函数使用。语法格式为：re.compile(pattern[, flags])、


#正则表达式
import  re
parme=re.compile(r'\d')
m=parme.match('dgsh12fgsdfg54hfstf54')
s=parme.findall('dgsh12fgsdfg54hfstf54')
print(m)
print(s)


it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())



 # -*- coding: utf-8 -*-
import os
for root, dirs, files in os.walk('F:\基础'):
     open('mycd.cdc', 'a').write("%s %s %s" % (root,dirs,files))


import os
export = ""
for root, dirs, files in os.walk('F:\基础'):
    export+="\n %s;%s;%s" % (root,dirs,files)
    open('mycd.cdc', 'w').write(export)



print("不换行",end="")

print("换行")
print("测试数据",end="");


#练习1
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#产生1-4 4个数字，数字可能分布在各个位置，比如百位、十位和个位
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if  a!=b and a!=c and b!=c:
                print(a,b,c)


#练习2
#企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
# 求应发放奖金总数？

i=int(input("请输入净利润:"))
lirui=[0,100000,200000,400000,600000,1000000]
ticheng=[0.1,0.075,0.05,0.03,0.015,0.01]
sum=0

for s in range(0,6):
    if i>lirui[s]:
        sum+=(i-lirui[s])*ticheng[s]
        print("各个阶段得提成：%s"%((i-lirui[s])*ticheng[s]))
print("总提成：%s"%sum)


for x in range(1, 13):
    a = 84/x -x/2
    if int(a) == a:
        n = a ** 2 - 100
        print(n)

name = 'My name is Mike'

print(name[11:15])

i=True;
while i:
    tell=input("请输入您的电话号码：")
    if len(tell)==11:
        yin=tell.replace(tell[:-4],"*"*len(tell[:-4]))
        print("您的电话号码是%s,为了保障您账户的安全，我们对您的号码进行了加密，加密后的电话号码为%s"%(tell,yin))
        break;
    else :
        print("您输入的电话号码格式不正确，请重新输入")


#输入重量g，转换成kg
def zhong(a):
    liang=a/1000
    return str(liang)+"kg"

s=int(input("请输入要转换的重量："))
shu=zhong(s)
print(shu)



#输入直角三角形的两个直角边的值，输出斜边长
import  math

def xie(a,b):
    zong=a**2+b**2
    c=math.sqrt(zong)
    return c

one=int(input("第一条直角边长："))
two=int(input("第二条直角边长："))

shu=xie(one,two)
print("斜边长为：%s"%shu)





#在每一次打开文件之后，最好使用close关闭文件，否则，文件对象会一直操作系统的资源，在数据量大的时候，会导致电脑运行内存卡
file=open("E:\测试文档.txt","w")
file.write("你最喜欢的食物")

file=open("E:\测试文档.txt","r")
print(file.read())


#第一部分
def lu(name,filenei):
    filename="E:\\"
    filelujin=filename+name+".txt"
    file=open(filelujin,'w')
    file.write(filenei)

#调用函数
lu("新建文档20180817","这是我新写入的文件，第一次，应该不会报错吧？")

#第二部分
def text_filter(word,cencored_word="lame",changed_word="Awesome"):
    print(word.replace(cencored_word, changed_word))
    return  word.replace(cencored_word,changed_word)


#调用函数
text_filter("play game lame!")
#print(text_filter("play game lame!"))


#将两个函数写入一个函数，目的是为了，将写入文件的敏感词过滤替换成别人内容
def zong(name,msg):
    str=text_filter(msg)
    lu(name,str)

zong("两个函数","lame!lame!lame!")


username='admin'
password='cxl123456'

kai=True

while kai:
    name=input("请输入用户名：")
    word=input("请输入密码：",word.replace(word[:-4],"*"*len(word[:-4])))
    if name != username or word != password:
        print("输入的账号密码有误！请重新输入.....")
    else:
        print("互道晚安却在王者峡谷相遇......")
        break



#函数模拟数据库数据，登录账号

def login():
   password= input("请输入密码：")
   cheng=password=='123456'
   if cheng:
       print("登录成功！")
   else:
       print("密码错误！")


#重置密码
passwordlist=["###","123456"]
def twoLogin():
    password = input("请输入密码：")
    print("----------输入###可重置密码----------")
    success=password==passwordlist[-1]
    shi=password==passwordlist[0]
    if success:
        print("登录成功！")
    elif shi:
        pa=input("请输入新密码")
        passwordlist.append(pa)
        login()
    else:
        print("密码错误！")

twoLogin()



for a in range(1,10):
    for b in range(1,10):
        print("%s*%s=%s"%(a,b,a*b))



def login():
   password= input("请输入密码：")
   cheng=password=='123456'
   if cheng:
       print("登录成功！")
   else:
       print("密码错误！")


#重置密码
passwordlist=["###","123456"]

def twoLogin():
     i = 3
     while i > 0:
        password = input("请输入密码：")
        print("----------输入###可重置密码----------")
        success=password==passwordlist[-1]
        shi=password==passwordlist[0]
        if success:
            print("登录成功！")
        elif shi:
            pa=input("请输入新密码")
            passwordlist.append(pa)
            login()
        else:
            print("密码错误！")
            i=i-1

twoLogin()



def lu(name,filenei):
    filename="E:\\"
    filelujin=filename+name+".txt"
    file=open(filelujin,'w')
    file.write(filenei)

for a in range(1,11):
    flie=open("E:\\%s.txt"%a,"w")
    flie.write("这是第%s个文件"%a)


for a in range(1,100):
    if a%2==0:
        print(a)

#复利公式  S=P(1+i)^n

amount=int(input("请输入要存放的资金："))
rate=float(input("请输入银行利率："))
time=int(input("请输入投资的时间："))
i=1
while i<=time:
    print("第%s年：%s"%(i,amount*(1+rate)**i))
    i=i+1


#列表去重
nums = [1,1,2]
s=0
for a in range(len(nums)):
   if nums[s]!=nums[a]:
    s=s+1
    nums[s]=nums[a]


# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))



#运算符
a=int(input("请输入要计算的第一个数字："))
b=int(input("请输入要计算的第二个数字："))
c=input("请输入运算符：")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)


for x in range(1, 13):
    a = 84/x -x/2
    if int(a) == a:
        n = a ** 2 - 100
        print(n)

#判断今天是今年的第几天
#1、先定义一个列表，一年中每个月份共有多少天，二月是列外，要先判断是平年还是瑞年
#2、年份能被4整除；
#3、年份若是 100 的整数倍的话需被400整除，否则是平年。

days=[31,27,31,30,31,30,31,31,30,31,30,31]

yeas=int(input("请输入年："))
moths=int(input("请输入月："))
day=int(input("请输入天："))
zong=day
for i in range(0,moths-1):
    zong+=days[i]
    if yeas%4==0 or (yeas%100==0 and yeas%400==0) :
        if moths>2:
            print(zong+1)
        else :
            print(zong)
    else :
        print(zong)


import copy

list0 = [1, [2, 3], 4, 5]
print(list0)

newlist = list0
list1 = list(list0)
list2 = list0 * 1
list3 = list0[:]
list4 = copy.copy(list0)
list5 = copy.deepcopy(list0)  # 列表深拷贝，包括元素为子列表
list6 = list0.copy()

list0.append(6)
list0[1].append(23)

print("修改后的list0：\t", list0, "\t地址为：\t", id(list0))
print("---------")
print("=号方式：\t\t\t", newlist, "地址为：", id(newlist))
print("list()方式：\t\t\t", list1, "地址为：", id(list1))
print("*号方式：\t\t\t", list2, "地址为：", id(list2))
print("[:]方式：\t\t\t", list3, "地址为：", id(list3))
print("copy.copy()方式：\t\t\t", list4, "地址为：", id(list4))
print("list0.copy()方式：\t\t\t", list5, "地址为：", id(list5))
print("copy.deepcopy()方式：\t\t\t", list6, "地址为：", id(list6))



val = [['a'] * 3] * 3
val[0][0] = 'b'
print (val)
print(id(val[0]),id(val[1]),id(val[2]))

tmp = [['c', 'c', 'c'], ['c', 'c', 'c'], ['c', 'c', 'c']]
tmp[0][0] = 'a'
print (tmp)
print(id(tmp[0]),id(tmp[1]),id(tmp[2]))

#数值类型（int和float）、字符串str、元组tuple都是不可变类型。而列表list、字典dict、集合set是可变类型。
#由于是不可变对象，变量对应内存的值不允许被改变。当变量要改变时，实际上是把原来的值复制一份后再改变，开辟一个新的地址，
# astr再指向这个新的地址（所以前后astr的id不一样），原来astr对应的值因为不再有对象指向它,就会被垃圾回收。
# 这对于int和float类型也是一样的。
a = 2
b = 2
c = a + 0
c += 0

print(id(a), id(b), id(2))  # id都相同
print(c is b) #True

astr = 'good'
print(id(astr))
astr += 'aa'
print(id(astr)) # id和上面的不一样


tupe=(1,2,3)
print(id(tupe))
tupe+=(5,6)
print(id(tupe))

list=[1,2,3]
print(id(list))
list+=[6,5]
print(id(list))



list=[1,2,3]
b=list.copy()
print(b)
print(id(list))
print(id(b))


def lie(n):
    if n==1 or n==2:
        return 1
    return  lie(n-1)+lie(n-2)

print(lie(50))

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(3)  # 暂停 1 秒


list=[]
for i in range(1,100):
    if i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0:
        list.append(i)

print(list)



import turtle

t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(90)


print("let's go")
print('"hello,word"she said')



print("""我的名字、
哈尔的移动城堡、千与千寻""")


print("我的名字\deb")
print("hello,\nword")


months = [
 'January',
 'February',
 'March',
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December'
]
# 一个列表，其中包含数1～31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th']  + ['st', 'nd', 'rd'] + 7 * ['th']  + ['st']

year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(month_name + ' ' + ordinal + ', ' + year)

sentence = input("Sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print()
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '| ' + sentence + ' |')
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()

print("22")


# 列表
# 函数list
print(list("python"))
# 修改元素，给元素赋值
a = [0, 1, 2, 3, ]
a[2] = 5
print(a)

# 删除元素
del a[0]
print(a)

# 给切片赋值
a[1:] = [3, 4, 5, 6]
a[1:1] = [2]
print(a)

# append添加元素值（只能将值添加到最后一个）
a.append(7)
print(a)

# 使用clear清除列表值
# a.clear()
# print(a)

# copy赋值列表
b = a.copy()
# print(b)

# count统计元素在列表中出现过几次
sun = ['str', 'string', 'abc', 'str', 'abc', 'bca']
i = sun.count('string')
print(i)

# extend 能够同时将多个值添加到列表末尾，换言之，你可以使用一个列表来扩展另一个列表
one = [1, 2, 3]
two = [4, 5, 6]
# 拼接
print(one + two)
# 使用extend
one.extend(two)
print(one)
# 虽然拼接与extend输出结果一致，但是其实不然，拼接没有改变原列表值，但是extend改变了原值，
# extend类似于拼接a=a+b，但是效率没有a.extend(b)高

# index 查找列表中指定值出现的"第一个"索引
s = sun.index('abc')
print(s)

# insert 用于将对象插入列表
one.insert(3, '这是插入的第一个元素')
print(one)

# pop  方法pop从列表中删除一个元素（末尾为最后一个元素），并返回这一元素。
print(one.pop(3))
print(one)

# remove 方法remove用于删除第一个为指定值的元素
print("删除前：%s" % sun)
sun.remove('str')
print("删除后：%s" % sun)

# reverse按相反顺序排列列表中的元素,返回值为none，如果输出print（one.reverse）结果为none,sort也是类似
one.reverse()
print(one)

# sort 方法sort用于对列表就地排序。就地排序意味着对原来的列表进行修改，使其元素按顺序排列，而不是返回排序后的列表的副本
# sorted   这个函数可用于任何序列，但总是返回一个列表
one.sort()
print(one)

# 高级排序，方法sort接受两个可选参数：key和reverse，例如，按照元素长度排序
sun.sort(key=len)
print(sun)

# 对于另一个关键字参数reverse，只需将其指定为一个真值（True或False，），以指出是否要按相反的顺序对列表进行排序。
one.sort(reverse=True)
print(one)

# 元组：不可修改的序列，与列表一样，元组也是序列，唯一的差别在于元组是不能修改的
# 元组语法很简单，只要将一些值用逗号分隔，就能自动创建一个元组；也可以用（1,2，。。。）括起来
# 在定义一个只有一个值的元组时，要在值后面加上“，”，否则，系统不能识别该值为元组类型
# 它们用作映射中的键（以及集合的成员），而列表不行。
# 有些内置函数和方法返回元组，这意味着必须跟它们打交道。只要不尝试修改元组，与
# 元组“打交道”通常意味着像处理列表一样处理它们（需要使用元组没有的index和count等方法时例外）。

yuan = 1, 2, 3, 4, 5

#  函数tuple的工作原理与list很像：它将一个序列作为参数，并将其转换为元组①。如果参数已经是元组，就原封不动地返回它。
lis = [1, 2, 3, 4]
strs = 'python'

print(tuple(lis))
print(tuple(strs))

# 字符串，所有标准序列操作（索引、切片、乘法、成员资格检查、长度、最小值和最大值）都适用于字符串，
# 但别忘了字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的。
str='python'




# 1、字符串基本操作
# %，转换说明符，指出了要将值插入什么地方。s意味着将值视为字
#  符串进行格式设置。如果指定的值不是字符串，将使用str将其转换为字符串
format = "hello word,my name is %s ,你好，%s"
values = ("Tom", "sila")
print(format % values)

print("你的名字:%s,你的年龄：%s" % ("tom", 23))

# format，格式化字符串，它融合并强化了早期方法的优点。
# 替换字段没有名称或将索引用作名称。2、索引可以不按照顺序来排列
print("你的名字作者：{}，千与千寻作者：{}".format("新海诚", "宫崎骏"))
print("{0} {1} {2} {3} {0} {1}".format('to', 'be', 'or', 'not'))

from math import pi

print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))

'''
1、字段名：索引或标识符，指出要设置哪个值的格式并使用结果来替换该字段。除指定值外，还可指定值的特定部分，如列表的元素。
2、转换标志：跟在叹号后面的单个字符。当前支持的字符包括r（表示repr）、s（表示str）和a（表示ascii）。
   如果你指定了转换标志，将不使用对象本身的格式设置机制，而是使用指定的函数将对象转换为字符串，再做进一步的格式设置。
3、格式说明符：跟在冒号后面的表达式（这种表达式是使用微型格式指定语言表示的）。
   格式说明符让我们能够详细地指定最终的格式，包括格式类型（如字符串、浮点数或十六进制数），
   字段宽度和数的精度，如何显示符号和千位分隔符，以及各种对齐和填充方式。
'''

# 1、替换字段名 （填充方式：1、按顺序填充；2、指定参数名填充；3、通过索引指定填充参数）
# 在最简单的情况下，只需要向format提供要设置器格式的未命名参数，并在格式字符串中使用未命名字段
# 如果按顺序匹配参数和指定桉参数名同时使用，先填充参数之后，在将其他参数按顺序填充

print("{a}{}{}{b}".format(1, 2, a=3, b=4))  # {}按顺序填充参数，{参数1}，.format（参数=值）按参数填充值
print("{0}{1}".format(1, 2))  # 根据索引填充值

# 在填充值时，并不是只能范文值本身，也可以访问其组成部分，例如，列表、元组等
lis = ("Tom", "jack", "milk")
print("hello,{lis[1]}".format(lis=lis))

# 2、基本转换：指定要在字段中包含的值后，就可添加有关如何设置其格式的指令了，首先，可以提供一个转换标志
# 在要转换类型时，可以进行类型的指定，例如{pi：f}.format(pi=...)
print("{pi!s},{pi!r},{pi!a}".format(pi="π"))
print("The number is {num:f}".format(num=42))

'''
类型表：
b 将整数表示为二进制数
c 将整数解读为Unicode码点
d 将整数视为十进制数进行处理，这是整数默认使用的说明符
e 使用科学表示法来表示小数（用e来表示指数）
E 与e相同，但使用E来表示指数
f 将小数表示为定点数
F 与f相同，但对于特殊值（nan和inf），使用大写表示
g 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
G 与g相同，但使用大写来表示指数和特殊值
n 与g相同，但插入随区域而异的数字分隔符
o 将整数表示为八进制数
s 保持字符串的格式不变，这是默认用于字符串的说明符
x 将整数表示为十六进制数并使用小写字母
X 与x相同，但使用大写字母
% 将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）
'''

# 3、宽度、精度和千位分隔符
# 设置浮点数（或其他更具体的小数类型）的格式时，默认在小数点后面显示6位小数，
# 并根据需要设置字段的宽度，而不进行任何形式的填充

print("{num:3}".format(num=3))
print("{name:10}".format(name="Bob"))
print("Pi day is {pi:.3f}".format(pi=pi))

# 想要在输出时，修改默认的对其方式
# 左对齐、右对齐和居中，可分别使用<、>和^
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))

# center，方法center通过在两边添加填充字符（默认为空格）让字符串居中。
print("The Middle by Jimmy Eat World".center(39))

# find方法，在字符串中查找子串，如果找到，就返回第一个字符的索引，否则返回-1
# 使用find方法还可以指定搜索的起点和终点（起点和终点值（第二个和第三个参数）一般只指定起始值，不指定终点值）
name = 'hello word，my name is tom,my name is '
print(name.find("my"))

# join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素，合并序列的元素必须都是字符串
a = ["1", "2", "3"]
print(":".join(a))
print("+".join(a))

# lower方法，返回字符串的小写版本；另一个与lower相关的方法是title，。它将字符串转换为词首大写，即所有单
# 词的首字母都大写，其他字母都小写；另一种方法是使用模块string中的函数capwords；但是因为语法等一些影响，可能做不到那么规范
# 所以一般是自己写代码
print("HELLO,WORD!my name Is Tom".lower())

# replace方法，指定子串都替换为另一个字符串，并返回替换后的结果
test = "my name is tom"
print(test.replace("tom", "jack"))

# spilt方法，其作用与join相反，用于将字符串拆分为序列
# 注意，如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符等）处进行拆分
print("1+2+3+4+5".split("+"))

# strip方法，将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果，类似于tirm（）方法,
# 比如用户输入值得时候，不下心输入了空格，可以用strip方法来删除前后两端空格
# 也可以指定字符来删除，但是只会删除子串两端的指定字符，中间的不会删除
print(' internal whitespace is kept '.strip())
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))

# translate方法，与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
# 这个方法的优势在于能够同时替换多个字符，因此效率比replace高



# 字典：由值和键组成，这种键值对称为项（item），每个键、值之间用：隔开，项与项之间用，隔开；空字典就是{}
# 1、函数dict（实质是一个类，和list、tuple、str一样）
items = [("name", "tom"), ("age", 23)]
d = dict(items)
print(d)
print(d["name"])

# 使用关键实参调用函数
s = dict(name='Gumby', age=42)
print(s)

'''
字典的基本行为在很多方面都类似于序列。 d是字典名称
 len(d) 返回字典d包含的项（键值对）数。
 d[k] 返回与键k相关联的值。
 d[k] = v 将值v关联到键k。
 del d[k ]删除键为k的项。
 k in d 检查字典d是否包含键为k的项。
虽然字典和列表有多个相同之处，但也有一些重要的不同之处。
——————————
 与list、tuple和str一样，dict其实根本就不是函数，而是一个类。
 键的类型：字典中的键可以是整数，但并非必须是整数。字典中的键可以是任何不可变的类型，如浮点数（实数）、字符串或元组。
 自动添加：即便是字典中原本没有的键，也可以给它赋值，这将在字典中创建一个新项。
 然而，如果不使用append或其他类似的方法，就不能给列表中没有的元素赋值。
 成员资格：表达式k in d（其中d是一个字典）查找的是键而不是值，而表达式v in l（其中l是一个列表）
 查找的是值而不是索引。
'''
# 基本的字典操作
# 简单的数据库练习
people = {
    "Tom": {
        "Tell": "0716",
        "addr": "美国"
    },
    "婕妤晴子": {
        "Tell": "0718",
        "addr": "日本"
    },
    "滨崎步": {
        "Tell": "0718",
        "addr": "日本"
    }
}
shu = {
    "Tell": "电话号码为",
    "addr": "地址为"
}
userName = input("请输入要查询的用户名：")
request = input("查询电话号码请输入（t）,查询地址请输入（a）：")
if request == "t":
    key = "Tell"
if request == "a":
    key = "addr"
if userName in people:
    print("{}的{}{}".format(userName, shu[key], people[userName][key]))

# 将字符串格式设置功能用于字典

# 字典方法
# 1、clear，删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不返回（或者说返回None）
print(people)

# people.clear()
# print(people)

# copy方法
# 方法copy返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制，因为值本身是原件，而非副本）
# copy当替换副本的值时，原件值不发生变化；就地修改副本中的值，原件会发生变化，因为原件指向的也是被修改的值

# 浅复制copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
print(x)
y['username'] = 'mlh'
y['machines'].remove('bar')
print(x)
print(y)

# 深复制，copy中的函数deepcopy
from copy import deepcopy

d = {}
d["name"] = {"Alfred", "bad"}
qianfhizhi = d.copy()
shengfuzhi = deepcopy(d)
d["name"].add("tom")
print(qianfhizhi)
print(shengfuzhi)

# 方法fromkeys
# 创建一个新字典，其中包含指定的键，且每个键对应的值都是None
aa = {}.fromkeys(['name', 'age'])
print(aa)
# 直接对dict（前面说过，dict是所有字典所属的类型。类和类型将在第7章详细讨论）调用方法fromkeys
bb = dict.fromkeys(['name', 'age'])
print(bb)
# 如果你不想使用默认值None，可提供特定的值
cc = dict.fromkeys(['name', 'age'], '(unknown)')
print(cc)

# get方法
# 方法get为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发错误。
d = {}
# print(d["name"])#如果是通过字典本身的机制去访问不存在元素，会导致异常，但是get不会导致异常，会返回none
# 可指定“默认”值，这样将返回你指定的值而不是None
print(d.get("name"))
print(d.get("name", "对不起，没有找到该元素"))

people = {
    "Tom": {
        "Tell": "0716",
        "addr": "美国"
    },
    "婕妤晴子": {
        "Tell": "0718",
        "addr": "日本"
    },
    "滨崎步": {
        "Tell": "0718",
        "addr": "日本"
    }
}
shu = {
    "Tell": "电话号码为",
    "addr": "地址为"
}
userName = input("请输入要查询的用户名：")
request = input("查询电话号码请输入（t）,查询地址请输入（a）：")
key = request
if request == 't': key = 'Tell'
if request == 'a': key = 'addr'
person=people.get(userName,{})
shu=shu.get(key,key)
result = person.get(key, 'not available')
print("{} {} {}.".format(userName, shu, result))


# items，方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项在列表中的排列顺序不确定
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())

# 返回值属于一种名为字典视图的特殊类型,你还可确定其长度以及对其执行成员资格检查
it = d.items()
print(len(it))

# keys ,方法keys返回一个字典试图，其中包含指定的字典中的关键字

# pop，方法pop可用于“获取”与指定键相关联的值，并将该键值对从字典中删除，意思是在获取键和值得同时也将该键值从字典中删除
d = {'x': 1, 'y': 2}
print(d.pop("x"))
print(d)

# popitem，方法popitem类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地弹出一个字典项，
# 因为字典项的顺序是不确定的，没有“最后一个元素”的概念。
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)

# setdefault方法，方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault
# 还在字典不包含指定的键时，在字典中添加指定的键值对

d = {}
print(d.setdefault("name", "N/A"))
print(d)
d["name"] = "tom"
print(d.setdefault("name", "N/A"))
print(d)

# 指定的键不存在时，setdefault返回指定的值并相应地更新字典。如果指定的键存在，就返回其值，并保持字典不变。
# 与get一样，值是可选的；如果没有指定，默认为None。
d = {}
print(d)  # 为空
print(d.setdefault("name"))
print(d)  # 将指定键加入了字典中

# update，方法update使用一个字典中的项来更新另一个字典,可以修改原字典的值，也可以通过update给原字典新添加值

dd = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
x = {
    "title": "tom",
    "name": "jack"
}
dd.update(x)
print(dd)

# values ,方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视图可能包含重复的值。


# 1、映射：映射让你能够使用任何不可变的对象（最常用的是字符串和元组）来标识其元素。Python只有一种内置的映射类型，那就是字典。
# 2、将字符串格式设置功能用于字典：要对字典执行字符串格式设置操作，不能使用format和命名参数，而必须使用format_map。
# 3、字典方法：字典有很多方法，这些方法的调用方式与列表和字符串的方法相同。

# print函数可以打印多个参数，print（参数1，参数2，参数三，。。。。）
print("你的名字", "千与千寻")

# 导入时重命名
import math  # 一般情况，我们会以这种形式导入模块
# from math import pi
from math import pi, frexp, fabs  # 或者是已这两种方式导入指定的函数
from django import *  # 导入模块中的所有

# 在两个模块都包含相同函数的情况下，可以使用import 模块名，然后用
# import somemodule
# module1.open(...)
# module2.open(...)

# 也可以在语句末尾添加as子句并指定别名
import math as food

print(food.sqrt(4))

# 对于模块中有相同函数的情况，也可以像如下方式导入他们
from math import pi as one

# 赋值
# 1、序列解包
# 1.1、同时给多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)
# 交换多个变量的值,实际上，这里的操作被称为序列解包（或可迭代对象解包）：将一个序列（或任何可迭代
# 对象）解包，并将得到的值存储到一系列变量中
x, y = y, x
print(x, y, z)

values = 1, 2, 3
print(values)
x, y, z = values
print(x)

# 在使用返回元组（或其他序列或可迭代对象）的函数或方法时很有用
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, valuea = scoundrel.popitem()
print(key)
print(valuea)

# 要解包的序列包含的元素个数必须与你在等号左边列出的目标个数相同，否则会引发异常
# a, b, c = 1, 2
# print(a, b, c)

# 可使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同
a, b, *rest = 1, 2, 3, 4
print(rest)
# 可以将带星号的变量放在其他位置，赋值语句的右边可以是任何类型的序列，但带星号的变量最终包含的总是一个列表，在变量个数和值个数相同时也是这样
a, *b, c = "abc"
print(a, b, c)

# 2、链式赋值
# 2.1、链式赋值是一种快捷方式，用于将多个变量关联到同一个值,第一种方式和第二种方式不等价
x = y = "nide"  # 1
print(id(x), id(y))
x = "nide"  # 2
y = "nide"  # 2

# 3、增强赋值
# 类似于将x=x+1写成x+=1，这称为增强赋值，适用于所有的标准运算符，如*、/、%等
x = 2
x += 1
print(x)

food = "apple"
food += "+orange"
food *= 2
print(food)

# 代码块
# 代码块其实并不是一种语句，代码块是一组语句，可在满足条件时执行（if语句），可执行多次（循环），等等。
# 代码块是通过缩进代码（即在前面加空格）来创建的

# 条件和条件语句
# False None 0 "" () [] {} 标准值False和None、各种类型（包括浮点数、复数等）的数值0、空序列（如空
# 字符串、空元组和空列表）以及空映射（如空字典）都被视为假，而其他各种值都被视为真，包括特殊值True

# 布尔值True和False属于类型bool，而bool与list、str和tuple一样，可用来转换其他的值
# 鉴于任何值都可用作布尔值，因此你几乎不需要显式地进行转换(python会自动转换)
print(bool("I carry you"))

name = input('请输入用户名： ')
if name.endswith("Tom"):  # endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False
    print("%s，你是上天眷顾的幸运儿，恭喜你获得隐藏任务" % name)
else:
    print("%s，欢迎来到新手村" % name)

# 还有一个与if语句很像的“亲戚”，它就是条件表达式
status = "friend" if name.endswith("Gumby") else "stranger"
# 如果条件（紧跟在if后面）为真，表达式的结果为提供的第一个值（这里为"friend"），否则为第二个值（这里为"stranger"）


#elif相当于else if 语句
num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')

#代码块嵌套
ni = input('请输入用户名： ')
if ni.endswith("Tom"):
    if ni.startswith("Mr."):
        print("hello,Mr.%s"%ni)
    elif ni.startswith("Mrs."):
        print("hello,Mrs.%s"%ni)
    else:
        print("hello,%s"%ni)
else:
    print("%s,很抱歉，您目前不是我们的会员"%ni)


# 比较运算符
'''
x == y x 等于y
x < y x小于y
x > y x大于y
x >= y x大于或等于y
x <= y x小于或等于y
x != y x不等于y
x is y x和y是同一个对象
x is not y x和y是不同的对象
x in y x是容器（如序列）y的成员
x not in y x不是容器（如序列）y的成员
'''
# 1、相等运算符“==”，两个等号是比较运算符，一个等号是赋值运算符“=”
print("foo" == "foo")
x = 2
print(x)

# 2、is：相同运算符（是用来检查两个对象是否相同（而不是相等））,print(id(x),id(y),id(z)),所指向的地址不同
# 注意：不要将is用于数和字符串等不可变的基本值，结果不可预测
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)
print(x is y)
print(x is z)

# in：成员运算符

name = input("你最喜欢的动漫")
if "千与千寻" in name:
    print("宫崎骏主导")
elif "你的名字" in name:
    print("新海诚主导")
else:
    print("暂时查询不到")


# 3、字符串和序列的比较（字符串是根据字符的字母排列顺序进行比较的，但是字母都是Unicode字符，他们是按码点排列的）
print()

# 字符是根据顺序值排列的。要获悉字母的顺序值，可使用函数ord。这个函数的作用与函数chr相反
print(ord("m"))  # ord将字符转换成数值
print(chr(109))  # 将数值转换成字母

# 如果想要比较大小写，就需要使用lower函数来转换大小写
print("a".lower() < "B".lower())

# 其他序列的比较方式与此相同，但这些序列包含的元素可能不是字符，而是其他类型的值
print([1, 2] < [2, 1])

# 如果序列的元素为其他序列，将根据同样的规则对这些元素进行比较
print([2, [1, 4]] < [2, [1, 5]])

# 布尔运算符 and / or / nor三个布尔运算符
# 比如要判断数值范围，布尔运算符有个有趣的特征：只做必要的计算

'''number = int(input('Enter a number between 1 and 10: '))
if number <= 10 and number >= 1:
    print('Great!')
else:
    print('Wrong!')


nums = [2, 7, 11, 15]
target = 9
o = []
for s in range(4):
    for i in range(0, 4):
        sum = nums[s]+nums[i]
        aa = nums.index(s)
        bb = nums.index(i)
        if target == sum:
            o.append(aa)
            o.append(bb)
            print(o) 


#找两个列表的合集
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

nums3 = []
for i in range(len(nums1)):
    if nums1[i] in nums2:
        nums3.append(nums1[i])

print(list(set(nums3)))

c = set(nums1) & set(nums2)
print(list(c))

'''
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
# 也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

'''
输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
                a = 19
                d = {}
                while True:
                    l = list(map(int, list(str(a))))
                    print(l)
                    m = 0
                    for i in l:
                        m += i ** 2
                    if m in d:
                        print(d)
                        return False
                    if m == 1:
                        print(d)
                        return True
                    d[m] = m
                    n = m

import collections

a = [3,1]
nums2=collections.Counter(a)
for i in nums2.values():
    if i>=2:
        print(True)
print(False)
'''

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
num = [0, 0, 1]
x = num.count(0)
for i in range(x):
    num.remove(0)
    num.append(0)
print(num)

'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''
nums = [3, 2, 2, 3]
val = 3
x = nums.count(val)
for i in range(x):
    nums.remove(val)
print(len(nums))

'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''
'''
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
aa = list(set(nums))
for i in aa:
    x = nums.count(i)
    if x > 2:
        for j in range(x - 2):
            nums.remove(i)
print(nums)
'''
'''
# 给定两个数组，编写一个函数来计算它们的交集。
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
nums1 = [1, 2, 2, 1]
nums2 = [1,2]

nums3 = []
for i in range(len(nums1)):
    if len(nums1)==1 or len(nums2)==1:
        nums3 = list(set(nums1) & set(nums2))
    else:
        if nums1[i] in nums2:
            nums3.append(nums1[i])

print(list(nums3))
'''

'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
    l.append(s)
    l.reverse()
for j in l:
    zong.insert(0,j)
print(zong)


zong = [-1]
k = 0
l=[]
if len(zong)==1:
    print(zong)
else:
    if k<len(zong):
        for i in range(0, k):
           s = zong.pop()
           l.append(s)
        for j in l:
            zong.insert(0,j)
    if k>len(zong):
        for i in range(0, len(zong)):
           s = zong.pop()
           l.append(s)
        zong=l
    if k==len(zong):
        zong.reverse()

print(zong)

s='str'
result = s[::-1]
print(result)

mo=-1534236469
if -10<mo<10:
    print(mo)
strs=str(mo)
if strs[0]!='-':
    mo=int(strs[::-1])
    if mo>2**31-1:
        print(0)
    else:
        print(mo)
if strs[0] == '-':
    mo = int(strs[1:][::-1])
    if -mo<-2**31:
        print(0)
    else:
        print(mo)


s = "loveleetcode"
a=0

for i in s:
     if s.count(i)==1:
        a=s.find(i)
        break
     if s.count(i) != 1:
        print(-1)

'''

'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

cs = [2, 0, 2, 1, 1, 0]


class Solution:
    def sortColors(self, nums):
        # write your code here
        def swap(list, one, two):
            temp = list[one]
            list[one] = list[two]
            list[two] = temp
            return list

        left, right, i = 0, len(nums) - 1, 0
        while (i <= right and left < right):
            if (nums[i] == 1):
                i += 1
                continue
            if (nums[i] == 0):
                swap(nums, left, i)
                i += 1
                left += 1
                continue
            if (nums[i] == 2):
                swap(nums, right, i)
                right -= 1
                continue
        return nums


s = Solution()
print(s.sortColors([0, 2, 2, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 2, 0]))

# 排序方法
# 插入排序
# 以从小到大排序为例，元素0为第一个元素，插入排序是从元素1开始，
# 尽可能插到前面。插入时分插入位置和试探位置，元素i的初始插入位置为i，试探位置为i-1，
# 在插入元素i时，依次与i-1,i-2······元素比较，如果被试探位置的元素比插入元素大，
# 那么被试探元素后移一位，元素i插入位置前移1位，直到被试探元素小于插入元素或者插入元素位于第一位。

arr = [5, 6, 3, 5, 8, 2, 9]
length = len(arr)
for i in range(1, length):
    x = arr[i]
    for j in range(i, -1, -1):
        if x < arr[j - 1]:
            arr[j] = arr[j - 1]
        else:
            break
    arr[j] = x
print(arr)

'''
'''
希尔排序
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。
该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，
每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

def shellSort(nums):
    # 设定步长
    step = len(nums) / 2
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and nums[i - step] > nums[i]:
                nums[i], nums[i - step] = nums[i - step], nums[i]
                i -= step
        step = step / 2
    return nums


if __name__ == '__main__':
    nums = [9, 3, 5, 8, 2, 7, 1]
    print(shellSort(nums))
'''

'''
冒泡排序
描述
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


lst1 = input().split()
lst = [int(i) for i in lst1]
# lst = input()
bubble_sort(lst)
for i in range(len(lst)):
    print(lst[i])

'''

'''
直接排序
描述
基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
'''
dai = [1, 8, 6, 9, 2, 0, 0, 5]
length = len(dai)
for i in range(length):
    min = i
    for j in range(i + 1, length):
        if dai[min] > dai[j]:
            min = j
    dai[min], dai[i] = dai[i], dai[min]
print(dai)

'''
快速排序
描述(利用递归，效率较低，较难理解)
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

# 比较运算符
# 1、相同运算符==，=（一个等号是赋值运算）
# 2、is运算符，检查两个对象是否相同
# ==用来检查两个对象是否相同，而is用来检查两个对象是否相同
x = [1, 2, 3]
y = [2, 4]
del (x[2])
y[1] = 1
y.reverse()

print(x == y)
print(x is y)

# in成员运算符，可以用在表达式中
if 1 in x:
    print("在")

# 字符串和序列的比较
# 布尔运算符 and是一个布尔运算符，它接受两个真值，并在这两个值都为真时返回真，否则返回假，另外还有两个布尔运算符，or和not


# 断言，if语句的亲戚,目的就是为了让程序出现错误的时候立即崩溃，这项胜过以后再崩溃
# 要求某些条件得到满足，可以在语句中使用关键字assert，可以在条件后面加一个字符串，对断言做说明
'''
'''

age = -10
assert 0 < age < 100, "age值不在范围内"
print(age)
'''
'''
# 循坏
# 1、while
i = 0
while i < 3:  # 循环停止的条件
    i += 1
    print(i)

# 2、for循环  可迭代对象是可使用for循坏进行遍历的对象，py提供了一个创建范围的内置函数，range()函数
# 注意：如果能够使用for循环，就尽量不要使用while函数
for i in range(0, 10, 2):
    print(i)

# 一些迭代工具
# 1、并行迭代  zip函数是一个很有用的并行迭代工具，他可以将序列缝合起来，并返回一个有元组组成的序列
# 要查看zip的内容，可以用list转换为列表,缝合之后也可以在循环中将元组解包
# 需要注意的是，但序列的长度不易的时候，函数zip会将最短的序列用完就停止缝合
name = ['tom', 'jack', 'shanshan']
age = ['21', '22', '35']
sex = ['男', '女', '女']
for i in range(len(name)):
    print(name[i], ':', age[i])

# 将序列缝合，返回类型为zip的数据，但是要查看zip中的数据，必须将用list将zip转换为列表
sa = list(zip(name, age, sex))
print(sa)

# 利用循环将缝合后的zip解包
for name, age in zip(name, age):
    print(name, age)

# 2、迭代时获取索引，enumerate（）
for index, values in enumerate(name):
    if 'tom' in name:
        values[index] = '你的名字'
print(name)

# 3、反向迭代和排序后再迭代，reversed和sorted函数
print(sorted([4, 3, 6, 9, 2, 1, 0]))
print(sorted('hello word'))
print(list(reversed('hello word')))
print(''.join(reversed('hello word')))

# 跳出循环
# 1、break，直接跳出循环
#  2、continue   结束当前迭代
# 3、while  true/break 成例,while True导致循环永不结束

while True:
    word = input("输入一些数据：")
    if not word: break
    print("上级指令：", word)

'''
'''

# 简单推导
# 列表推导式
# 列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。

sex = ['男', '女']
shu = input("您的性别是：")
s = [shu for s in sex if shu == s]
print(s)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
mingzi = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(mingzi)
# 这种方法，不用检查每种配对的可能性，效率更高
kong = {}
for girls in girls:
    kong.setdefault(girls[0], []).append(girls)
mingzi2 = [b + '+' + g for b in boys for g in kong[b[0]]]
print(mingzi2)

# pass，del，exec语句
# 1、pass语句，当你的代码未完成，可是需要运行代码时，py中是不允许的，这是我们可以的在未完成代码的地方加上一天pass语句
if shu == '男':
    print("你是汉子")
elif shu == '女':
    pass
# 2、使用del删除,当计算机中没有任何与之关联的变量，无法获取他时，py就会直接将其删除，这被称为垃圾收集
# 使用del删除只是删除变量的名称，并没有删除变量本身（值）。
# 事实上，当你删除变量名称之后，没有与变量值相关联的变量时，计算机会自动给你删除值
aa = ['alice', 'bernice', 'clarice']
bb = aa
print(aa)
print(bb)

aa = None
bb = None

# 3、exec和eval执行字符串及计算其结果
# exec语句，在调用exec语句的时候，尽量不要只给exec传递一个参数，在大多数情况下，还应该给exec函数传递一个“命名空间”
# 命名空间--用来放置变量的地方，否则会污染你的命名空间，即修改你的变量,导致对象不可调用
exec("print('exec语句')")

from math import sqrt

scope = {}
exec('sqrt=1', scope)
print(sqrt(4))
print(scope['sqrt'])

# eval是一个类似于exec的内置函数。exec执行一系列Python语句，
# 而eval计算用字符串表示的Python表达式的值，并返回结果（exec什么都不返回，因为它本身是条语句）。
print(eval('6*5+6'))
print(eval(input("输入要计算的表达式：")))

# 向exec或eval提供命名空间时，可在使用这个命名空间前的在其中添加一些值
# scope['x'] = 5
# scope['y'] = 6
# print(eval((x * y), scope))

# 抽象和结构
import math

x = 1
y = math.sqrt
print(callable(x))
print(callable(y))


# 自定义函数
# def hello(name):
#     return "你好" + name + "初次见面，请多多指教！"
#
#
# print(hello("皮皮陈"))


# s = True
# duzi = ['暴力', '厚脸皮', '傻敷敷', '美人心计']
# while s:
#     print("----------------------------------")
#     pjl = input("请用一个词句形容彭婕莉（输入“结束”结束任务）：")
#     for it in duzi:
#         if pjl == it:
#             print("%s的彭婕莉，哈哈，果真如此"%pjl)


# 函数编写斐波那契数列,返回所有的数列
def fibs(nums):
    result = [0, 1]
    for i in range(nums - 2):
        result.append(result[-2] + result[-1])
    return result[9]


print(fibs(10))


# 函数文档,可以通过# 注释的方式编写函数注释
# 也可以在函数内，写入文档字符串（‘函数内容’），写入的文档字符串是函数的一部分，后面可以通过函数.___doc___的方式访问

# 这是一个直接返回传入参数的函数
def hanShu(x):
    '这是函数的注释'
    return x


print(hanShu.__doc__)


# 其实并不是函数的函数，在py中有些函数什么都不返回，如果你不告诉它返回值，他默认是返回None
def test():
    print('This is printed')
    return  # 结束函数
    print('This is not')


x = test()
print(x)  # None


# 参数魔法
# 1、值从何来。
# 写函数旨在为当前程序（甚至其他程序）提供服务，你的职责是确保它在提供的参数正确时完成任务，并在参数不对时以明显的方式失败
# 在函数内部给参数复制对外部结果没有任何影响
# 但当参数为可变列表时，需要注意，在函数内部改变值时会改变原列表的值，
# 在将同一个列表赋值给同一个变量时，这两个变量都指向同一个地址
def nnn(n):
    n = '你的名字'


na = '千与千寻'


def try_to_change(na):
    pass
    print(na)


try_to_change(na)

'''


# <editor-fold desc="默认参数">
# 在使用默认参数时，参数一定要指向不变对象，否则就会导致多次调用默认函数时，默认参数就会随之改变
def keng(L=[]):
    L.append("END")
    return L


print(keng())
print(keng())
print(keng())


# </editor-fold>


# <editor-fold desc="可变参数">

# 可变参数（*参数名），就是传入的参数个数是可以改变的，可以是任意个，也可以是0个关键，
# 这些可变参数在调用函数时自动组装成一个tuple
def calc(*nums):
    sum = 0
    for x in nums:
        sum = sum + x ** 2
    return sum


# 计算多个数的乘积

def calc(*nums):
    sum = 0
    i = 0
    for x in nums:
        if i == 0:
            sum = x
        if i != 0:
            sum = sum * x
        i += 1
    return sum


print('你的名字%s' % calc())


# 如果是要将list或者是tuple作为可变参数传入函数，python是允许在list或者是tuple前加一个*，作为可变参数传入函数
# list = [1, 2, 3]
# print(calc(*list))


# </editor-fold>

# <editor-fold desc="关键字参数">

# 关键字参数（**参数名）：关键字参数允许你传入0个或者是任意个含参数名的参数，
# 这些参数在函数内部自动组装成一个dict
def GuanJianZi(name, age, **qita):
    print("name:%s\n age:%s\n qita:%s" % (name, age, qita))


GuanJianZi('Tom', 21, city='湖北', Tell='13526548532')

extra = {'city': 'Beijing', 'job': 'Engineer'}
GuanJianZi('Tom', 21, **extra)


# 关键字参数的作用：扩展函数，“**extra”表示把extra这个dict的所有key-value用关键字传入到函数“**qita”参数，
# qita将获得一个dict，注意qita获得的dict是对extra的一份拷贝，对qita的改动不会影响函数外的extra

# </editor-fold>

# <editor-fold desc="命名关键字参数">

# 命名关键字参数（参数1，参数2，*，参数,3，参数4，...），命名关键字参数需要一个特殊的分隔符*，
# *后面的参数被视为命名关键字参数
# 1、对于关键字参数，我们可以检查传入的传入的参数是否是我们所期望的参数,至于到底传入了哪些，就需要在函数内部检查
# 但是调用者仍可以传入不受限制的关键字参数，列如：
def JianCha(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print(name, age, kw)


# 2、如果要限制关键字参数的名字，就可以用命名关键字参数，列如，只接受city和job作为关键字参数
def XianZhi(name, age, *, city, job):
    print(name, age, city, job)


# 调用关键字函数
XianZhi('Jack', 23, city='湖北', job='IT')


# 3、如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不需要一个特殊的分隔符*，列如：
def KeAndGuan(name, age, *kw, sex, tell):
    print(name, age, kw, sex, tell)


# 调用函数,注意，命名关键字调用时必须传入参数名，否则会报错，
# 这是因为调用函数时，缺少参数名，python解释器会把四个关键字参数视为位置参数，但是原函数只接受固定的位置参数，所以会报错
KeAndGuan('tom', 21, [1, 2, 3], sex='男', tell='13562548965')


# 命名关键字参数可以有默认值，从而简化调用，列如：
def MoRen(name, age, *, city='hubei', job):
    print(name, age, city, job)


# 函数调用,因为city参数有默认值，所以在调用时时可以不传入city参数值的
MoRen('Jack', 32, job='IT')


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

# </editor-fold>

# <editor-fold desc="参数组合">
# 参数组合
# 在python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是，请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数、和关键字参数
def f1(a, b, c=0, *d, **e):
    print(a, b, c, d, e)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, [1, 2, 3], sex='男', age=21)

# 可以通过一个tuple和dict，调用组合参数的函数
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用她，无论他的参数是如何定义的
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


# </editor-fold>

# <editor-fold desc="递归函数">
# 递归函数：如果一个函数在内部可以调用自身本身，那么这个函数就是递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))

# 使用递归函数一定要注意防止栈溢出，在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出，列如fact(1000)
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，把循环看成是一种特殊的尾递归函数也是可以的
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
# </editor-fold>

# <editor-fold desc="切片">
# 对于经常去指定索引范围的操作，py提供了切片操作，例如：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
# L[0:3]表示，从索引0处开始取，直到索引3为止，但不包含索引3，如果第一个索引为0，还可以省略L[:3]
# 如果要取倒数第一个元素的话，py也支持倒数切片L[-1]
print(L[-2:])
# 还有步长，去控制取的步长，列如
K = []
for i in range(100):
    K.append(i)

print(K[:10:2])  # 前十位数，每隔两个数取一个数字
print(K[::5])  # 所有的数字，每隔五个数取一个数字

# tuple也是一种list，唯一的却别是tuple是不可变的，切片后还是tuple
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'......'也可以看成是一种list，切片后还是字符串
print('你的名字'[-2:])
# </editor-fold>

'''
def trim(s):
    if len(s) == 1 or s == '':
        return


print(trim('   nide   '))
'''
# <editor-fold desc="可迭代对象">
# dict迭代的是key,如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
d = {'a': 1, 'b': 2, 'c': 3}
for i in d:
    print(i)

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, values in enumerate(L):
    print(i, values)


def ma(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    sum = set()
    for i in L:
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max


print(ma([7, 1, 3, 9, 5]))
# </editor-fold>

# <editor-fold desc="列表推导式">
# 列表推导式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)
# </editor-fold>


# <editor-fold desc="generator生成器">
# generator生成器，也是一个可迭代对象，生成generator的方法，generator保存的是一个算法：如下
# 1、只需要把列表生成式的[]改成().就会穿件一个generator
L = [x * x for x in range(1, 10)]
print(L)
g = (x * x for x in range(1, 10))
print(g)


# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
# 我们要打印generator的每个元素时，用next（）来获取
# 2、如果一个函数定义中包含关键字yield，那么这个函数就是一个generator
# 函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后一行函数就返回
# generator在每次调用next(）的时候执行，遇到yield语句返回，再次执行时从上次返回yield语句处继续执行
def fib(n):
    a, b, c = 0, 0, 1
    while a < n:
        yield c
        b, c = c, b + c
        a += 1
    return 'done'


g = fib(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

print(fib(3))


# 杨辉三角
def triangles():
    p = [1]
    while True:
        yield p  # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
# </editor-fold>

# <editor-fold desc="迭代器">
# 迭代器
# 可直接作用于for循环的数据类型有一下几种：
# 1、一类是集合数据类型，如list、tuple、dict、set、str
# 2、一类是generator，包括生成器和带yield的generator function
# 这些可直接作用于for循环的对象统称为可迭代对象：Iterable，可以用isinstance判断对象是否是Iterable对象
from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance('', Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections.abc import Iterator

print(isinstance((x * x for i in range(6)), Iterator))
print(isinstance('', Iterator))

# 生成器都是Iterator对象，但是list、tuple、dict、set、str虽然是可迭代对象（Iterable），但是不是Iterator
# 要想把可迭代对象变成迭代器，可以使用iter（）函数
print(isinstance(iter([]), Iterator))
# </editor-fold>

# 函数式编程：函数是面向过程的程序设计的基本单元，而函数式编程允许吧函数本身作为参数传入另一个函数，还允许返回一个函数

# <editor-fold desc="高阶函数">
# 高阶函数：变量可以指向函数，如下：
print(abs(-2))  # 调用了函数abs
print(abs)  # abs是函数本身
x = abs(-9)  # 获得函数调用结果，把结果赋值给变量
print(x)

# 把函数本身赋值给变量，即变量可以指向函数,当函数赋值给变量之后，直接调用函数和调用变量效果相同
y = abs
print(y(-12))


# 函数名也是变量
# abs = 10
# print(abs(-10))
#  当abs指向10时，通过abs（-10）无法在调用绝对值函数，他已经不指向绝对值函数了，而是指向一个常量

#  传入函数，一个函数接收另一个函数作为参数，称之为高阶函数，如下：


def add(x, y, f):
    return f(x) + f(y)


print(add(-2, -5, abs))
# </editor-fold>

# <editor-fold desc="map和reduce">
# map/reduce
# map函数接受两个参数，一个函数，一个是可迭代对象（Iterable）,map作为高阶函数，事实上将运算规则抽象了
# 如果传入的是多个参数，就以参数少的为准
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的迭代器（Iterator）返回。如下：
lia1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x ** 2


list2 = map(f, lia1)
print(list(list2))

print(list(map(str, lia1)))


# 已参数少的为准
def func(x, y):
    return x + y


m = map(func, range(1, 8), range(3, 6))
print(list(m))

# reduce的用法，reduce把一个函数作用在一个序列[x1,x2,x3,x4,....],这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def fn(x, y):
    return x * 10 + y


op = reduce(fn, lia1)
print(op)
print(type(op))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
    return digits[s]


po = reduce(fn, map(char2num, '2234'))
print(po)
s = 'hudwe'
print(s.title())


def normalize(name):
    return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

list1 = [3, 5, -4, -1, 0, -2, -6]

print(sorted(list1, key=lambda x: abs(x)))
# </editor-fold>

# filter函数，用来筛选不符合条件的元素，返回一个迭代器对象，如果需要转换成列表，可以用list()


# 自定义函数，判断某个对象是否可调用，可以用callable

import math

cs = 1
ss = math.sqrt
print(callable(cs))
print(callable(ss))

print('='*50)
import mypackage.ObjectProgramming
bart=Student('Tom','湖北荆州')
print(bart)
print(bart.print_data())