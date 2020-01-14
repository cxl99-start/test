# region 基础语法
# num1=int(input('请输入你要计算的第一个数字'))
# num2=int(input('请输入你要计算的第二个数字'))
# print("%s*%s=%s"%(num1,num2,num1*num2))

# 转义\,\本身也是需要转义的，\n换行，\t制表符、r‘’表示字符转义,
# 如果一行代码输出需要换行，可以直接在"""换行显示"""中写代码，然后直接换行，输出的内容也会换行了
# 通过end=""也可以实现两个输出语句不换行显示

print(r'这里面不需要转义\\\\', '\n\\\\\n')
print("""张三
李四
王五""")
str1 = "你好，我是"
str2 = "jack"
print(str1, end='')
print(str2)

# /计算结果是一个浮点数，就算是两个整数相除，得到的也是一个浮点数
# //地板除，永远都是整数，即使除不尽
# %取余
print(10 / 3, ';', end="")
print(10 // 3, ';', end="")
print(10 % 3)

# 格式化字符串，%运算符用来格式化字符串，%s表示字符串替换，%d表示用整数替换,%f浮点型，%x十六进制整数
# 如果%只是一个普通的字符，就需要用%%转义，即表示一个%
# 另一种就是format(),{0}，{...}来表示占位符，后面.format（参数）
print('你是%s，我是%s' % ('jack', 'rose'))
print("你昨天{0}在干嘛，你与死者{1}有没有见过".format('早晨六点', '张三'))

# list,添加元素到末尾：append（元素）；添加元素到指定位置：insert（i，元素）
# 删除末尾元素：pop（），删除指定位置：pop（i）
# list中元素数据类型可以不一样，list中也可以放list，也可以通过list[i]的方式去替换原本list中的值
list1 = ['tom', 'jack', 'rose', 'hazzy']
for i in list1:
    print(i, '-', end='')

# tuple，和list很相似，但是tuple一旦初始化之后就不能在修改
# 定义tuple是，元素就必须被确定，如果为空的话，就直接tuple=(),如果只有一个元素就是tuple=(元素1，)
# tuple不可变，指的是一开始确定的指向，如果指向的是list，那我指向的的list对象就不能变成其他的对象，
# 但是list对象是可变的，所以list的元素可以变，但是tuple指向的list这个对象本身不能变为其他对象
s = ()
a = (1,)
print(a)
kebian = ('粥', '水煮鱼', ['毛血旺', '鸭血'])
kebian[2][1] = '鸭血粉丝'
print(kebian)

# dict,字典，使用键-值（key-value）存储。dict的key是不可变的对象；一个key只能对应一个value，
# 所以当对一个key放入多个value时，后面的值会替换掉前面的值,pop(key)删除key，对应的value也会删除
# 如果key在dict中不存在，就会报错，可以通过in dict的方式，判断key是否存在，或者是get（）方法
d = {'name': 'jack', 'sex': '女'}
print(d['name'])
print('name' in d)  # 判断key是否存在
# get（）方法只有一个参数：key不属于dict时，返回none；两个参数：key不属于dict时，放回第二个参数值
print(d.get('name', '不属于dict时，返回的字符串，可以只用一个参数'))

# list与dict对比
# dict特点：
# 1、查找和插入很快，不会随着key的增加而变慢
# 2、需要占用大量的内存，内存浪费多
# list特点：
# 1、查找和插入的时间随着元素的增加而增加
# 2、占用空间小，内存浪费少

# set和dict类似，也是一组key的集合，但不存储value。因为key不能重复，所以set中没有重复的key，如果有重复，会自动过滤
# add()添加元素，remove（）删除元素
list1 = (1, 2, 3, 4)
set = {1, 3, 4, 5, 1, list1}

print(set)

# 对于不可变对象来说，调用对象自身的任意方法，也不会改变对象自身的内容；想法，会创建一个新的对象并返回

# 条件判断语句，if(条件判断)：.....elif（条件判断）：......else.......
# int(),转换成int类型；str（）转换成字符型类型
height = 1.59
weight = 70
bmi = weight / (height * height)
print(bmi)
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif 18.5 < bmi <= 25:
    print('正常')
elif 25 < bmi <= 28:
    print('正常')
elif 28 < bmi <= 32:
    print('过重')
elif bmi > 32:
    print('严重肥胖')

# 循环：有两种循环
# 循环迭代出list或者是tuple中的元素，所以for x in就是把每个元素带入变量x，然后执行缩进块的语句
# range()函数，自动生成指定范围的整数序列，例如需要计算1到50的和，range（51）
temp = [1, 4, 2, 68, 6, 4]
for x in temp:
    print(x)

# 第二种是while循环，条件满足一直循环，不满足退出循环，同样的，break可以结束循环，continue是跳出当前循环
num = 1
while num < 5:
    print(num)
    num = num + 1

# endregion

# region 高级特性
from mypackage import testhan

# 切片，取指定索引范围的操作
qie = ['tom', 'secrale', 'yi.mao', 'hayzz']
print(qie[0:3])  # 正取
print(qie[-3:-1])  # 倒取，-1是最后一个索引

L = [range(100)]
l1 = L[:10]  # 取前十个数
l2 = L[-10:]  # 取后十个数
l3 = L[:10:2]  # 前十个数，每两个取一个
l4 = L[::5]  # 所有数，没五个取一个

if testhan.trim('hello  ') != 'hello':
    print('测试失败!')
elif testhan.trim('  hello') != 'hello':
    print('测试失败!')
elif testhan.trim('  hello  ') != 'hello':
    print('测试失败!')
elif testhan.trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif testhan.trim('') != '':
    print('测试失败!')
elif testhan.trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

# 迭代，定一个list或tuple，通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration），字符串也是可迭代的
# 在python中，无论数据有没有下标，只要是可迭代对象，都可以迭代，例如dict
dicts = {'name': 'tom', 'age': 25}
for key in dicts:  # dict默认是迭代key的，如果要迭代values可以用，dict.values的方式
    print(key)

for values in dicts.values():  # 迭代values
    print(values)

for k, v in dicts.items():  # 迭代dict的key和values
    print(k, ':', v)

    # 判断一个对象是否可迭代
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))
print(isinstance('123', Iterable))

# 如果要实现类似于java的下标循环，python内置enumerate函数可以把list变成索引-元素对
for i, v in enumerate(['tom', 'jack', 'rose']):
    print(i, v)

for i, v in [('tom', 23), ('jack', 12), ('rose', 25)]:
    print(i, v)

    # 练习
from mypackage.testhan import findMinAndMax

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 列表推导式，isinstance判断变量是否为字符串，例如：
lie = [x * x for x in range(1, 11) if x % 2 == 0]
print(lie)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 生成器，边循环编辑算的机制称之为生成器，generator
# 1、只需要吧列表生成的[]改成()，就创建了一个generator,next()获取generator的下一个值
list1 = [i * i for i in range(10)]
print(list1)
generator = (i * i for i in range(10))
for i in generator:
    print(i, ',', end='')

    # 如果一个函数定义包含yield关键字，那么这个函数不在是一个普通的函数，而是一个generator


def fib(s):
    n, a, b = 0, 0, 1
    while n < s:
        print('\n', b, end='')
        a, b = b, a + b
        n = n + 1
    return 'done'
    # generator和函数执行流程不一样，函数是顺序执行，遇到return就返回；
    # 变成generator的函数，每次调用next()的时候执行，遇到yield的时候返回，再次执行是从上次返回的yield语句处继续执行


def fiby(s):
    n, a, b = 0, 0, 1
    while n < s:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(6))
s = fiby(6)
while True:
    try:
        x = next(s)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!!!!')
else:
    print('测试失败!')

# 迭代器：iterator；可迭代对象：iterable；python中iterator表示一个数据流，可以被next()函数调用并不断放回下一个数据
# 可以把list、dict、str等iterable变成iterator，使用iter（）函数即可
# 凡是可作用于for循环的对象都是iterable类型；
# 凡事可用next()函数的对象都是iterator，他们表示一个惰性计算的序列
from collections.abc import Iterator

print(isinstance([1, 2, 3], Iterator))

# endregion

# region 模块

# 模块：一个.py文件就被称之为，取名时尽量不要与python的内置函数冲突
# 如果在自定义的模块和其他的模块冲突时，可以通过包（Package）来组织模块，避免冲突
# 引入包后，只要顶层的包与别的包不冲突，那所有的模块都不会与别人冲突，而包下面的模块就变成了 包.模块名
# 每个包下面必须有一个__init__.py文件，他本身就是一个模块，模块名就是包名
# 注意：自己创建模块时要注意命名，不能和python自带的模块名称冲突
# 列如系统自带的sys模块，自己创建的就不能命名为sys，否则无法引用系统自带的模块
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':  # Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时
    # if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()


# 作用域：函数的变量是通过_前缀来实现公开和非公开
# 正常的变量名是公开的，可以直接被引用，列如abc、PI
# 类似于__xxx__这种是特殊变量，可以直接被引用
# _xxx和__xxx这样的函数或者是变量是非公开的，不应该被直接引用
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
    # 我们在模块里面公开greeting，把内部逻辑用private隐藏起来，这样调用greeting函数不用关心private内部细节
    # 这也是一种非常有用的代码封装和抽象的方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


print(greeting('你的名字'))


# endregion

# region  错误、调试和测试

# 错误处理：try.....except......finally的错误处理机制
# 错误有很多类型，应该由不同的except语句块处理
# 所有的错误类型都继承自BaseException，他不但捕获改类型的错误，也会捕捉其他子类的错误
# try.....except捕获错误还有一个好处，就是可以跨越多层调用，不需要在每个函数捕捉错误，只要在合适的层次捕获错误就可以了，比如在主函数调用错误机制
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except BaseException as e:
#     print('发生错误：',e)
# except ZeroDivisionError as e:
#     print('发生错误：', e)
# finally:
#     print('finally......')
# print('END')

# 调用栈：如果错误没有被捕获，它就会一直往上抛，最后被python解释器捕获，打印一个错误信息，然后程序退出
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# print(main())

# 记录错误：如果我们不捕获错误，可以让python来打印错误堆栈，但是程序也会结束，我们可以自己捕获错误，然后记录错误，用内置的logging模块
# import logging
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# print(main())
# print('END')

# 抛出错误：捕获一个错误就是捕获一个该class的一个实例，raise语句就可以抛出一个错误的实例，自己编写的函数也可以抛出错误
# 只有必要的时候，我们才会去定义，python有内置的错误类型
# 在execpt中raise一个Error，还可以把一种类型的错误装换成另一种
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10/n
# foo('0')

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()


# 调试：用来调试bug，修复bug
# 1、直接用print打印可能有问题的变量来看看
# 2、断言：因为print用完后还得删除，我们可以用断言assert来代替，启用python解释器时可以用-O（英文大写字母o）参数来关闭assert
def ruo(s):
    n = int(s)
    assert n != 0, 'n is zero'  # 如果断言失败，assert语句本身就会抛出AssertionError
    return 10 / n


def main():
    print(ruo('0'))

    # 3、logging：把print替换为logging，和assert相比，logging不会抛出错误，而且可以输出到文件；
    # logging它允许你指定记录信息的级别，有debug、info、warning、error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了
    # logging的另一个好处就是通过简单的配资，一条语句可以输出去到不同的地方


# import logging
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# 4、pdb：启动python的调试器pdb，让程序以但不方式运行，可以随时查看运行状态
# 5、pdb.set_trace()，也是用pdb，不需要但不执行，只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点


# 单元测试：单元测试就是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
# 以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例,为了编写单元测试，需要引入python自带的unitest

import unittest
from mypackage.testhan import Dict


# class TestDict(unittest.TestCase): #编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承，不以test开头的方法不被认为是测试方法
#     #unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们期望的，最常用的断言就是assertEqual（）
#     def test_init(self):
#         d=Dict(a=1,b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d=Dict()
#         d['key']='value'
#         self.assertEqual(d.key,'value')
#
#     def test_attr(self):
#         d=Dict()
#         d.key='value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'],'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty

# if __name__ == '__main__': #一次可以批量很多单元测试，并且，有很多工具可以自动来允许这些单元测试
#     unittest.main()


# setUp与tearDown：可以在单元测试中编写两个特殊的方法，这两个方法会分别在每调用一个测试方法的前后分别被执行
# 比如测试启动一个数据库，setUp（）方法中连接数据库，在tearDown（）中关闭数据库


# 文档测试：可以自动执行写在注释中的代码，python内置的‘文档测试’模块可以直接提取注释中的代码并执行测试
# 例如：
def absd(n):
    '''
       Function to get absolute value of number.

       Example:

       abs(1)

       abs(-1)

       abs(0)

       '''
    return n if n >= 0 else (-n)


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1

    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# endregion

# region  正则表达式

# 在正则表达式中，如果直接给出字符，就是精确匹配
# 用\d可以匹配一个数字；\w可以匹配一个字符或数字；.可以匹配任意字符；\s可以匹配一个空格，（也包括tab的那个空白符）
# 匹配变长的字符，*表示任意个字符，
# 包括0；用+表示至少一个字符；
# 用?表示0个或1个字符；
# 用{n}表示n个字符；
# 用{n,m}表示n-m个字符

# 进阶：要做更加精确的匹配，可以用[]表示范围
# [0-9a-zA-Z\_]可以匹配一个数字、字母伙子下划线
# [0-9a-zA-Z\_]+可以至少匹配一个由数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0 - 9a - zA - Z\_]*可以匹配字母或下划线开头，后面接任意个数字、字母或下划线组成的字符串
# [a-zA-Z\_][0 - 9a - zA - Z\_]{0,19}限制了变量的长度是1-20个字符，（前面一个字符，后面最多19个字符）
# A|B可以匹配A或者是B
# ^表示行的开头，^\d表示必须以数字开头
# $表示行的结束，\d$表示必须以数字结束

# re模块，包含正则表达式的所有内容
import re

s = 'ABC\-001'  # 需要转义才能输出\，使用r，就不用考虑转义的问题了
print(r'ABC\\-001')

# match方法判断是否匹配成功；如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '012-25368'))

# 切分字符串，用正则表达式切分字符串比用固定的字符更灵活
print(re.split(r'\s+', 'a  b  d'))
print(re.split(r'[\s\,\;]+', 'a  f ; d'))

# 分组，除了简单的判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '201-59862')
print(m)
print(m.group(0), m.group(1), m.group(2))
# 分组后的子串，group（0）永远是原始字符串，group（1），group（2）.....表示第1,2.....个子串

# 贪婪匹配：正则表达式默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # 由于\d+采用的贪婪匹配，直接把后面的0全部匹配了，所以0*只能匹配空字符串了

# 要让\d+采用非贪婪匹配，加个？就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 如果一个正则表达式要重复使用很多次，我们可以预编译这个表达式，后面可以直接拿来用
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
re_phone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 预编译
print(re_phone.match('021-53689').groups())


def is_valid_email(addr):
    # re_mail = re.compile(r'^([a-z]+)(\.[a-z]+|[a-z])(@[a-z]+)\.com$')
    re_mail = re.compile(r'^([a-z]+)([\.\_\#a-z]+)(@[a-z]+)\.com$')
    if re_mail.match(addr):
        return True


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# endregion

# region   常用内建模块

# datetime：处理日期和时间的标准库
from datetime import datetime  # datetime模块下包含一个datetime类

dt = datetime(2015, 8, 12, 12, 20)  # 用指定日期时间创建datetime

# 1、datetime转换成timestamp：
stap = dt.timestamp()
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
print(stap)  # 将datetime转换成timestamp只需要调用timestamp()方法
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数

# 2、timestamp转换成datetime：使用datetime提供的fromtimestamp（）方法
dtt = datetime.fromtimestamp(stap)  # 装换成本地的时间
udt = datetime.utcfromtimestamp(stap)  # UTC标准时区的时间
print(dtt, '\n', udt)

# 3、str转换为datetime：通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
cady = datetime.strptime('2019-05-25 12:25:28', '%Y-%m-%d  %H:%M:%S')
print(cady)
# 4、dateime转换成str：转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
strtime = cady.strftime(('%a,%b %d %H:%M'))  # 要转换的时间.strftime()
print(strtime)

# 5、datetime加减：加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import timedelta

now = datetime.now()  # 获取当前的日期时间
print(now + timedelta(hours=1))  # 加小时
print(now + timedelta(days=1))  # 加天数
print(now + timedelta(weeks=1))  # 加星期

# 6、本地时间转换为UTC时间：datetime类型有一个时区属性tzinfo，但默认为None，所以无法区分时区，除非强制给datetime设置时区
from datetime import timezone, tzinfo

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dt)
datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=timezone(timedelta(0, 28800)))

# 7、时区转换：我们先通过utcnow（）拿到当前UTC时间，在转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bi_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bi_dt)

# astimezone()将bi_dt转换为东京时间
dong_dt = bi_dt.astimezone(timezone(timedelta(hours=9)))
print(dong_dt)

# 小结：
'''datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
 
 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。'''

# collections：python内建的一个集合模块，提供了许多有用的集合类

# 1、namedtuple：一个函数，用来创建一个自定义的tuple对象，并且规定tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, '\n', p.y)

# 2、deque：为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
print(q)

# 3、defaultdict：使用dict时，如果key不存在就会抛出异常。如果希望key不存在返回默认值，可以用defaultdict
# 默认值是调用函数返回的，而函数在创建defaultdict对象是传入。其余的行为和dict一样
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'aaa'
print(dd['key1'])
print(dd['key2'])  # key不存在，返回默认值

# 4、OrderedDict：使用key时，key是无序的，在对dict做迭代是，我们无法确认key的顺序，要保持key的顺序，可以用OrderedDict
from collections import OrderedDict

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
od = OrderedDict({'a': 1, 'b': 2, 'c': 3})
print(od)
odd = OrderedDict()  # key会按照插入的顺序排序，不是key本身排序
odd['z'] = 2
odd['x'] = 1
odd['y'] = 3
print(list(odd.keys()))


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

    # 5、ChainMap：ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
    # 适用场景：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
    # 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。


from collections import ChainMap
import os, argparse

# 构造缺省函数
defaults = {
    'color': 'red',
    'user': 'guest'
}
# 构造命令行参数
parser = argparse.ArgumentParser()
# parser.add_argument('--u','--user')
# parser.add_argument('--c','--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
# 没有任何参数时，打印默认参数；当传入命令行参数时，优先使用命令行参数；同时传入命令行参数和环境变量，命令行参数的优先级较高

# 6、Counter：一个简单的计数器，也是dict的一个子类
from collections import Counter

c = Counter()
for i in 'holle word':
    c[i] = c[i] + 1
print(c)

# base64：是一种用64个字符来表示任意二进制数据的方法
import base64

bs = base64.b64encode(b'binary\x00string')
print(bs)
# 标准的Base64编码后可能会出现字符+和-，在URL中就不能直接作为参数，所以又有一种’url safe‘的base64编码，把字符+和/分别变成-和_
print()

# struct：解决bytes和其他二进制数据类型的转换；struct的pack函数把任意数据类型变成bytes
import struct

print(struct.pack('>I', 10240099))  # '>I'表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数

# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))  # ‘>IH’后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数

# 'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))

import base64, struct

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    s = struct.unpack('<ccIIIIIIHH', bmp_data[:30])
    fs = s[0] + s[1]
    if not s:
        print('不是位图')
    if not fs == b'BM' or fs == b'BA':
        print('不是位图')
    return {
        'width': s[6],
        'height': s[7],
        'color': s[9]
    }

    # 测试


bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

# hashlib:
# 摘要算法简介：摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# 摘要算法通过函数f（）对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过

# 摘要函数是一个单向函数，计算f(data)很容易，但是通过digest反推data很困难
import hashlib

md = hashlib.md5()
md.update('hello word?'.encode('utf-8'))  # 如果数据量大，可以分块多次调用update（），最后计算的结果是一样的
print('哈希%s'%md.hexdigest())

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符串表示
# 另一种常见的摘要算法是SHA1，和MD5类似
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

hs = hashlib.sha1()
hs.update('hello word?'.encode('utf-8'))  # 如果数据量大，可以分块多次调用update（），最后计算的结果是一样的
print(hs.hexdigest())

# 摘要法的应用：比如存储用户名和密码，如果以明文存用户名密码，可能会落入他人之手，我们可以存储用户口令的摘要
# 然后当用户输入用户名和密码时，去与数据库存储的MD5字符对比
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    mds = hashlib.md5()
    mds.update(password.encode('utf-8'))
    mss = mds.hexdigest()
    if mss == db[user]:
        return True
    return False


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 由于常用的口令的MD5很容易被计算出来，如果用户名不能修改的情况下，可以把用户名和密码结合起来
import hashlib, random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# hmac:通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
# 注意：需要传入的message和key都是bytes类型，如果是str类型必须转成bytes类型
import hmac

message = b'Hello,world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

# itertools：用于操作迭代对象的函数
# itertools提供的几个‘无限’迭代器
# count()创建一个无限迭代器
import itertools

na = itertools.count(1)
# for i in na:
# print(i)

# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('abc')
# for i in cs:
#     print(i)

# repeat()负责把一个元素无限重复下去，该函数的第二个参数可以限定重复次数
ns = itertools.repeat('abc', 3)
for i in ns:
    print(i)

    # takewhile：无限函数虽然可以无限迭代，但是我们通常会通过takewhile()等函数根据条件判断来截取一个有限的序列
naa = itertools.takewhile(lambda x: x <= 5, na)
print(list(naa))

# chain():把一组迭代对象串联起来，形成一个更大的迭代器
ch = itertools.chain('abc', 'xyz')
for i in ch:
    print(i)

    # groupby():把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AaaBbBcCAA', lambda c: c.upper()):  # 忽略大小写
    print(key, list(group))

    # 练习：


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # l=list(filter(lambda x:x%2==1,range(1,N)))
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    p, c = 0, 1
    for si in itertools.takewhile(lambda x: x <= 2 * N - 1, itertools.count(1, 2)):
        p, c = p + c * 4 / si, -c
    return p


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


# contextlib：
# 任何对象，只要正确实现了上下文管理，就可以用with语句，不用再去担心资源有没有关闭
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


# with Query('Bob') as q:
#     q.query()


# @contextmanager：编写__enter__和__exit__很繁琐，python标准库提供了更简单的写法
from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q  # 用yiled语句把with...as var 把变量输出出去，然后，with语句就可以正常工作了
    print('end')


with create_query('Tom') as f:
    f.query()

    # 有时候需要在执行某段代码前自动执行特定的代码，也可以用@contextmanager


@contextmanager
def tog(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)


with tog('h2'):
    print('hello')
    print('word')
    '''
    代码执行顺序：
        1、with语句首先执行yiled之前的语句，因此打印出<h2>
        2、yiled调用会执行with语句内部的所有语句，因此打印出hello和word
        3、最后执行yiled之后的语句，打印出<h2>
    '''

    # @closing：如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
    # 例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen

# with closing(urlopen('https://www.python.org')) as op:
#     for line in op:
#         pass
        # print(line)

    # closing也是一个经过@contextmanager装饰的generator，这个generator编写起来非常简单
    # 它的作用就是把任意对象变为上下文对象，并支持with语句


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


# urllib:提供了一系列用于操作URL的功能

# Get：urllib的request模块可以非常方便的抓取url内容，也就是发送一个get请求到指定的页面，然后返回http的响应

from urllib import request

'''
# with request.urlopen('http://news-at.zhihu.com/api/4/news/latest') as f:
#     data=f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         pass
#         print('%s:%s'%(k,v))
#     print('Data:',data.decode('utf-8'))

'''
# 如果我们想要模拟浏览器发送get请求，就需要使用Request对象，通过往Request对象添加Http头，我们就可以请求伪装成浏览器
'''
req=request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        pass
        print('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

'''

# Post：如果要以post发送一个请求，只需要把参数data以bytes形式传入
from urllib import request, parse

'''
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
    '''

# Handler：如果需要更复杂的控制，比如通过一个proxy去访问网站，我们需要利用ProxyHandler来处理
'''
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

'''

# XML：操作XML的两种方式DOM和SAX
# 1、DOM：DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意的遍历树的节点
# 2、SAX：SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# SAX通常关心的事件：
# start_element事件，读取节点的开始标记；char_data事件，读取节点的内容；end_element事件，读取节点的结束标记。

# HTMLParser:解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!---', data, '--->')

    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_charref(self, name):
        print('&#%s' % name)


parser = MyHtmlParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

'''
    feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
'''

# endregion

# region 常用第三方模块

# Pillow 图像处理库
from PIL import Image

# 打开一个JPG图像文件，当前路径
im1 = Image.open('E:\笔记图片\文件夹.jpg')
# 获取图像尺寸
w, h = im1.size
print('size %s%s' % (w, h))
# 缩放到50%
im1.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图片保存
# im1.save('E:\笔记图片\d1.jpg','jpeg')

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('E:\笔记图片\文件夹.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
# im2.save('E:\笔记图片\lur.jpg', 'jpeg')

# 生成字母验证码图片：
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

    # 随机颜色


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色2


def rndColor2():
    return (random.randint(34, 127), random.randint(34, 127), random.randint(34, 127))


width = 60 * 4
height = 60
image = Image.new("RGB", (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('E:\笔记图片\验证码.jpg', 'jpeg')

# requests     访问网络资源，详情请参考pa.py文件，里面有requests的详细用法
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# r=requests.get("https://www.douban.com/",headers=headers)
# print(r.status_code)
# print(r.text)


# chardet    检测编码    encoding：检测到的编码    confidence：检测的概率，1.0  表示100%
from chardet import detect

print(detect(b'hello 123456'))
data = '小荷才立尖尖脚，早有蜻蜓立上头'.encode('utf-8')
datet = 'あいうえお'.encode('euc-jp')
print(detect(datet))

# psutil   系统监控

# 获取cpu信息
import psutil

print(psutil.cpu_count())  # 获取系统cpu逻辑数量
psutil.cpu_count(logical=False)  # cpu物理核心

# 获取内存信息
psutil.virtual_memory()  # 获取物理内存
psutil.swap_memory()  # 获取交换内存信息

# 获取磁盘信息
psutil.disk_partitions()  # 磁盘分区信息
psutil.disk_usage("/")  # 磁盘使用情况
psutil.disk_io_counters()  #

# 获取网络信息
psutil.net_io_counters()  # 获取网络读写字节/包个数
psutil.net_if_addrs()  # 获取网络接口信息
psutil.net_if_stats()  # 获取网络接口状态
psutil.net_connections()  # 获取当前网络连接信息

# 获取进程信息
# psutil.pids()  #所有进程的id
# p=psutil.Process(3776)   #获取指定进程ID
# p.name()  #进程名称
# p.exe()   #进程exe路径
# p.cwd()   #进程工作目录
# p.cmdline()   #进程启动的命令行
# p.ppid()   #父进程ID
# p.parent()   #父进程
# p.children()   #子进程列表
# p.status()   #进程状态
# p.username()   #进程用户名
# p.create_time()   #进程创建时间
# p.terminal()    #进程终端
# p.cpu_times()   #进程使用的cpu时间
# p.memory_info()   #进程使用的内存
# p.open_files()    #进程打开的文件
# p.connections()   #进程相关网络连接
# p.num_threads()   #进程的线程数量
# p.threads()   #所有线程信息
# p.environ()   #进程环境变量
# p.terminate()   #结束进程

# endregion

# virtualenv：用来为一个应用创建一套“隔离”的python运行环境
# https://www.jianshu.com/p/a83a8f5d68dd?utm_campaign=maleskine&utm_content=note&utm_medium=writer_share&utm_source=weibo
# 详情请参看网站地址中的解释

# region 图形界面
# python支持多种图形界面的第三方库,包括：TK，wxWidgets,Qt，GTK等

# Tkinter
# from tkinter import *
# import tkinter.messagebox as mess
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameinput=Entry(self)
#         self.nameinput.pack()
#         self.quitButton=Button(self,text='Hello',command=self.hello)
#         self.quitButton.pack()
#
#     def hello(self):
#         name=self.nameinput.get() or 'world'
#         mess.showinfo('Message','Hello,%s'%name)
#
# app=Application()
# app.master.title('Hello Word')
# app.mainloop()

# 海龟绘图：python内置了turtle库
from turtle import *

# 画一个长方形
# width(4)   #设置笔刷宽度
# forward(200)   #前进
# right(90)    #右转90度
#
# pencolor('red')   #笔刷颜色
# forward(100)
# right(90)
#
# forward(200)
# right(90)
#
# forward(100)
# right(90)
#
# done()


# 通过循环画一个五角星
# def drawStar(x,y):
#     pu()
#     goto(x,y)
#     pd()
#     seth(0)
#     for i in range(5):
#         fd(40)  #forward，前进距离
#         rt(144)  # right  ，右转度数
#
# for x in range(0,250,50):
#     drawStar(x,0)
#
# done()


# 递归画树
'''
from turtle import *
from random import *
from math import *

def tree(n, l):
    pd() # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l) # 画树枝


    if n > 0:
        b = random() * 15 + 10 # 右分支偏转角度
        c = random() * 15 + 10 # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        tree(n - 1, d)

        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n*0.8, n*0.8)
        circle(3)
        left(90)

        # 添加0.3倍的飘落叶子
        if(random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)


            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            pu()

            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)

    pu()
    backward(l)# 退回

bgcolor(0.5, 0.5, 0.5) # 背景色
ht() # 隐藏turtle
speed(0) # 速度，1-10渐进，0最快
# tracer(0, 0)
pu() # 抬笔
backward(100)
left(90) # 左转90度
pu() # 抬笔
backward(300) # 后退300
tree(12, 100) # 递归7层
done()
'''

# 递归分型树

'''
colormode(255)  # 设置色彩模式是RGB
lt(90)  # 左转90度

lv = 14
l = 120
s = 45

width(lv)  # 笔刷宽度

# 初始化RGB颜色
r = 0
g = 0
b = 0
pencolor(r, g, b)
penup()  # 画笔抬起，不留痕迹
bk(l)
pendown()
fd(l)


def draw_tree(l, level):
    global r, g, b
    w = width()

    width(w * 3.0 / 4.0)
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    width(w)


speed("fastest")
draw_tree(l, 4)
done()
'''

# endregion

# region 网络编程

#TCP/IP简介
    #IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去
    #IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。

    #TCP协议则是建立在IP协议之上的。
    # TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
    # TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。
    #一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口

#TCP编程
    #客户端
    #创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
    #创建一个基于TCP连接的Socket，可以这样做

'''
import  socket
import ssl
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建一个socket  ,http协议
s=ssl.wrap_socket(socket.socket())
s.connect(('www.sina.com.cn',443))   #建立连接,80是web服务的标准端口
    #创建socket时，AF_INET指定使用IPv4协议，如果要用IPv4，就指定为AF_INET6
    #SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接

s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\Connection:close\r\n\r\n')   #发送数据
    #TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定

    #接收数据
buffer=[]
while True:
    d=s.recv(1024)    #每次最多接收1K字节,一次指定接收指定的字节数，在while中循环，反复接收，知道recv()返回空，接收完成，退出
    if d:
        buffer.append(d)
        d = s.recv(1024)
    else:
        break
data=b''.join(buffer)
s.close()  #关闭连接

    #接收到的数据包括http头和网页本身
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('E:\笔记图片\sina.html','wb') as f:
    f.write(html)

    #服务器：服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
    # 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建一个基于IPv4和TCP协议的Socket
s.bind(('127.0.0.1',9999))  #监听端口
    #0.0.0.0绑定到所有的网络地址，127.0.0.1绑定到本机地址，如果绑定到这个地址，客户端必须在本机允许才能连接，外部计算机无法连接进来
s.listen(5)     #listen()方法监听端口
print("Waiting for connection......")

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s')%data.decode('utf-8').encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock,addr=s.accept()   #接收一个新连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

    #测试服务器的客户端
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))    #创建连接
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    s.send(data)    #发送数据
    print(s.recv(1024).decode('uft-8'))
s.send(b'exit')
s.close()

'''

#UDP编程
    #TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
    #使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是能不能到达就不知道了
    #UDP传输数据不可靠，但是它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议
'''
import socket
    #服务器：首先需要绑定端口，绑定端口和TCP一样，但是不需要调用listen()方法，直接接收来自任何客户端的数据
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #SOCK_DGRAM指定这个socket的类型是UDP
s.bind(('127.0.0.1',9999))    #绑定端口
print('Bind UDP on 9999...')
while True:
    data,addr=s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s!'%data,addr)
    #recvfrom()方法返回数据和客户端的地址与端口，服务器接收到数据后，直接调用sendto()把数据用UDP发给客户端
    #客户端：首先创建基于UDP的socket,不需要调用connent()，直接通过sendto给服务器发数据：

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarah']:
    s.sendto(data,('127.0.0.1',9999))    #发送数据
    print(s.recv(1024).decode('utf-8'))
s.close()
'''

# endregion

# region 电子邮件
    #编写程序来发送和接收邮件，本质就是：
        #1、编写MUA把邮件发到MTA
        #2、编写MUA从MDA上收邮件

#SMTP发送邮件：email复制构造邮件，smtplib负责发送邮件

'''
from email.mime.text import MIMEText
msg=MIMEText('hello,send by Python......','plain','utf-8')
    #构造MIMEText对象时，第一个参数就是邮件正文，第二个参数就是MIME的subtype
from_addr=input('From:')    #输入Email地址和口令
password=input('password:')
to_addr=input('To:')    #输入收件人地址
smtp_server=input('SMTP server:')

import smtplib
server=smtplib.SMTP(smtp_server,25)   #SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,[to_addr],msg.as_string())
server.quit()
'''


# endregion

# region 访问数据库

#使用SQLite：
    # 嵌入式数据库，他的数据库就是一个文件。在python中内置了SQLite，不需要安装就可以使用
    #操作关系型数据库，首先需要连接到数据库，一个数据库连接称为connection，之后需要打开游标（cursor），通过cursor执行sql语句


'''
import sqlite3
conn=sqlite3.connect('test.db')  #创建数据库文件，如果文件不存在，会自动在当前目录创建
cursor=conn.cursor()   #创建一个cursor
cursor.execute('create table user (id varchar(20) primary key ,name varchar(20))')
cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
print(cursor.rowcount)
cursor.close()   #关闭cursor
conn.commit()    #提交事务
conn.close()     #关闭connection


conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id =?',('1'))
print("sql查询结果为：%s"%cursor.fetchall())
cursor.close()
conn.close()
'''



    #connection对象和cursor对象，打开后一定记得关闭
    #使用cursor对象执行insert、update、delete语句时，执行结果rowcount返回影响的行数，可以拿到执行结果
    #使用cursor对象执行select语句时，通过featchall（）可以拿到结果集。结果集是一个list，每一个元素都是一个tuple，对应一行记录
    #如果sql语句带参数，那就把参数按照位置传递给execute方法，有几个？占位符就必须对应几个参数
'''
import os,sqlite3
db_file=os.path.join(os.path.dirname(__file__),'test.db')   #dirname（__file__）获取文件路径，path.join()拼接路径
if os.path.isfile(db_file):
    os.remove(db_file)

    #初始数据
conn=sqlite3.connect(db_file)
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values('A-001','Adam',95)")
cursor.execute(r"insert into user values('A-002','Bart',62)")
cursor.execute(r"insert into user values('A-003','Lisa',78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    conn=sqlite3.connect('test.db')
    cursor=conn.cursor()
    cursor.execute('select name from user where score between %s and %s order by score '%(low,high))
    values=cursor.fetchall()
    resultValues=[]
    for i in values:
        resultValues.append(i[0])
    return resultValues

    #测试
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('pass')

#SQLite的特点是轻量级、可嵌入、但不能承受高并发访问，是和桌面和移动应用

'''

#使用MySQL：
    #mysql是web世界中使用最广泛的服务器数据库。
    #MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite
'''
import mysql.connector
conn=mysql.connector.connect(user='root',password='ic+jujfww9X_',database='test')
cursor=conn.cursor()
cursor.execute('insert into user (id,name) values(%s,%s)'%('1','Michael'))
print('执行结果：%s'%cursor.rowcount)
conn.commit()   #提交事务
cursor.close()

    #查询
cursor=conn.cursor()
cursor.execute('select * from user where id=%s'%1)
print(cursor.fetchall())
cursor.close()
conn.close()
'''

#使用SQLAlchemy


# endregion

# region web开发

#http协议简介：在web应用中，服务器吧网页的html代码传给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议就是http
    #1、HTML是一种用来定义网页的文本，会HTML，就可以编写网页
    #2、HTTP是在网络上传输html的协议，用于浏览器和服务器的通信

    #http请求流程：
        #步骤1、浏览器首先向服务器发送http请求，请包括：
            #方法：get还是post，get仅请求资源，post会附带用户数据
            #路径：/full/url/path
            #域名：由Host头指定：Host：网站地址
            #其他：以及其他相关的Header，如果是post请求，那么还会包括一个boby，包含用户数据
        #步骤2：服务器向浏览器返回HTTP响应，响应包括：
            #响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务端处理时发生了错误
            #响应类型：由Content-Type指定，如：Content-Type: text/html;charset=utf-8表示响应类型是HTML文本，并且编码是UTF-8
            # Content-Type: image/jpeg表示响应类型是JPEG格式的图片
        #步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出http请求，重复步骤1、2

    #http格式：每个http请求和响应都遵循相同的格式，一个http包含header和body两部分，其中body是可选的
    #http GET 请求的格式：
'''
#每个header一行一个，换行符就是\r\n,不同的操作系统下，换行符不同
GET/path HTTP/1.1
Header1:v1
Header2:v2
Header3:v3
'''

    #HTTP POST请求格式：
'''
#当遇到连续两个\r\n时，Header部分结束，后面的数据全是body
POST/path HTTP/1.1
Header1:v1
Header2:v2
Header3:v3


body data goes here.....
'''

    #HTTP响应的格式：
'''
200 OK
Header1:v1
Header2:v2
Header3:v3


body data goes here.....
'''
    # 注意：当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip
    # 看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。
    # 压缩的目的在于减少Body的大小，加快网络传输。

# WSGI接口：因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以有一个统一的接口，这个接口就是WSGI
'''
web应用的本质：
    1、浏览器发送一个HTTP请求；    
    2、服务器收到请求，生成一个HTML文档；    
    3、服务器把HTML文档作为HTTP响应的Body发送给浏览器；    
    4、浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
'''
    #WSGI接口定义：只要开发者实现一个函数，就可以响应HTTP请求
'''
def appliction(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body= '<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
    return  [body.encode('utf-8')]
'''

    #上面的函数就是符合WSGI标准的一个HTTP函数
    # 它接收两个参数：environ：一个包含所有HTTP请求信息的dict对象；start_response：一个发送HTTP响应的函数。
'''
一个Header只能发送一次，也就是只能调用一次start_response（）函数；
start_response接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示；
函数的返回值，作为HTTP响应body发送给浏览器的
'''

    #运行WSGI服务：这个服务模块不考虑任何运行效率，仅供开发和测试使用
'''
from wsgiref.simple_server import make_server

httpd=make_server('',8000,appliction)
print('Serving HTTP on port 8000.....')
httpd.serve_forever()
'''

#使用web框架：用Flask框架来测试；详情参考falskApp.py文件

#使用模板：详情参考falskApp.py文件



# endregion

# region 异步IO

#在IO操作中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了
#异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程。使用异步IO将大大提升系统的多任务处理能力

#协程：协程看上去就是一个子程序，但是在执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行
    #优点：1、协程的执行效率高。因为子程序切换不是线程切换，而是程序自身控制，所以没有线程切换的开销
    #2、不需要多线程的锁机制，只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态
    #多线程+协程，充分利用多核，充分发挥协程的高效率
    # python对协程的支持是通过genertor实现，可以通过next()函数获取yield语句返回下一个值，yield也可以用来接收调用者发出的参数
'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
'''


# asyncio:asyncio的变成模型就是一个消息循环
    #从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO

'''
import asyncio
@asyncio.coroutine    #把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行
def hello():
    print('hello word!')
    r=yield  from asyncio.sleep(1)     #异步调用asyncio.sleep(1):
    print('Hello again!')
loop=asyncio.get_event_loop()    #获取exentloop
loop.run_until_complete(hello())    #执行coroutine
loop.close()
'''


    #用Task封装两个coroutine
'''
import asyncio,threading
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)   #停顿一秒
    print('Hello again! (%s)' % threading.currentThread())

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''

    #用asyncio的异步网络连接来获取sina、sohu和163的网站首页
'''
asyncio提供了完善的异步IO支持；
异步操作需要在coroutine中通过yield from完成；
多个coroutine可以封装成一组Task然后并发执行
import asyncio

@asyncio.coroutine
def wget(host):
    print('wegt %s'%host)
    connect=asyncio.open_connection(host,80)
    reader,writer=yield from connect
    header='GET/HTTP/1.0\r\nHost:%s\r\n\r\n'%host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()

    while True:
        line=yield from reader.readline()
        if line==b'\r\n':
            break
        print('%s header>%s'%(host,line.decode('utf-8').rstrip()))
    writer.close()
loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''

#asyncio和await：两步简单的替换：1、@asyncio.coroutine替换为async；2、把yield from 替换成await

'''
import asyncio

@asyncio.coroutine
def hello():
    print('没替换之前')
    r=yield from asyncio.sleep(1)
    print('结束')

async def hello1():
    print('新语法')
    r=await asyncio.sleep(1)
    print('新语法结束')

loop=asyncio.get_event_loop()
loop.run_until_complete(hello())

loop1=asyncio.get_event_loop()
loop1.run_until_complete(hello1())
loop1.close()
'''

    #练习，将用异步网络获取sina、sohu、163的网站用新的语法写
'''
import asyncio

async def wget(host):
    print('wget %s'%host)
    connect=asyncio.open_connection(host,80)
    reader,writer=await connect
    header='GET/HTTP/1.0\r\nHost:%s\r\n\r\n'%host
    writer.write(header.encode('utf-8'))
    await writer.drain()

    while True:
        line=await reader.readline()
        if line==b'\r\n':
            break
        print('%s header>%s' % (host, line.decode('utf-8').rstrip()))
    writer.close()
loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''

'''

import asyncio

@asyncio.coroutine
def test():
    n = "1"
    return n

async def hello():
    print('Hello, world!')
    r = await test()
    print('Hello, again %s' % r)

loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
'''


#aiohttp：基于asyncio实现的HTTP框架

from aiohttp import web

routes = web.RouteTableDef()

#Django写法
async def hello(request):
    return web.Response(text='Hello word!')

app=web.Application()
app.add_routes([web.get('/',hello)])
web.run_app(app)

#路由装饰器写法
@routes.get('/')
async def index(request):
    await asyncio.sleep(2)
    return web.json_response({
        'name':'index'
    })

@routes.get('/about')
async def about(request):
    await asyncio.sleep(0.5)
    return web.Response(text='<h1>baout us</h1>')

loop=web.Application()
loop.add_routes(routes)
web.run_app(loop)





# endregion
