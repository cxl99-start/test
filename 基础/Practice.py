# -*- coding： utf-8 -*-

# region 代码注释

'''
a=[1,'1233',0.2]#列表
b=(1,'1233',0.2)#元组
c={'name':'Tom','Age':'21'}#字典
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

#在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。


#参数

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
#俩个* 函数，加了两个星号 ** 的参数会以字典的形式导入
def lia(a,**b):
    print(a)
    for s in b:
        print(s)
    return

lia(10,name='包',age='22')

#如果单独出现星号 * 后的参数必须用关键字传入,否则就会报错
def dan(a,b,*,c):
    return  a+b+c
print(dan(1,2,c=3))

----匿名函数
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

#lambda [arg1 [,arg2,.....argn]]:expression
c=lambda a,b:a+b
print('相加的结果：',c(10,30))


#变量作用域
#Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

#变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

#L （Local） 局部作用域
#E （Enclosing） 闭包函数外的函数中
#G （Global） 全局作用域
#B （Built-in） 内建作用域
#以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，
再者去内建中找Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，
外部也可以访问，如下代码：

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

    列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边  # 第一条语句是最后一层。

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

print(name[11,15])



import math
math.floor()

from math import sqrt
print(sqrt(-1))


permissions = 'rw'
print('w' in permissions)

'''
# print("sssss")
# endregion

