# region 函数，所有函数定义，都在testhan.py文件中，这里只是引用

#函数基本语法,可以定单独定义在py文件中，通过from improt的方式引入模块中的函数，也可以写在一个py文件中直接调用
#如果要写一个空函数，可以直接用pass语句，pass语句一般用来占位，如果我们还没想好，这个函数内的代码，就可以用pass
#函数可以返回多个值，但是返回多个值是，是以tuple的形式返回的
'''def 函数名(参数)：
        函数执行体（或者是pass，即表示空函数）
'''

from mypackage import testhan

print(testhan.my_testabs(-9))

print('quadratic(2, 3, 1) =', testhan.quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', testhan.quadratic(1, 3, -4))

if testhan.quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif testhan.quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

#参数位置
print(testhan.power(5, 1))
# 默认参数
    # 当定义了一个和已有函数一样的函数，并且参数个数不一样时，会调用旧函数失败，这是我们可以使用默认函数
    # 例如def ss(x,s=2),s=2就是默认参数，当值传入一个参数时，s默认等于2，如果要传入其他参数，则可以自行传入
# 默认参数注意点：默认参数必须指向不变对象
    #1、必选参数在线，默认参数在后，否则会报错
    #2、当函数有多个参数时，把变化大的参数放在前面，变化小的参数放在后面，变化小的可以当做是默认参数
    #3、当不按顺序提供默认参数时，需要把参数名写上，其他默认参数会继续使用默认值

#可变参数,不定长参数 （*参数）
    # 如果要传入整个的元组或者是字典，可以在传入之参数之前加*，会把list或tuple的元素变成可变参数传入
    #也可以直接传入list或者tuple
print(testhan.calc(1, 2, 3))#直接传入参数
lsit=[3,2,2]
print(testhan.calc(*lsit))#整个传入list或者tuple

#关键字参数,**kw
    #可变参数允许传入0个或者任意个参数，这些可变参数在调用函数时自动组装成一个tuple。
    #而关键字参数允许你传入0个或者任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
students= testhan.guanjian('张洵', '男', address='湖北潜江', tell='0716523412', mother='李清')
print(students)
    #上面的调用也可以简化，直接传入一个已经定义好的dict进去，只是在参数前需要加**
    #此时传入的dict，是对原本的dict的拷贝，对参数dict的改动，不会影响到原本的dict
dict={'address':'湖北潜江','tell':'0716523412','mother':'李清'}
print(testhan.guanjian('张洵', '男', **dict))

#命名关键字参数 (参数1，*，参数2)，参数2则必须以关键字传入
    #对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
    #和关键字参数**kw不同，命名关键字参数需要一个特殊的分割符*，*后面的参数被视为命名关键字参数
    #* 后的参数必须用关键字传入,否则就会报错
ming= testhan.mingming('tom', '男', address='湖北荆门', tell='13542365985')
print(ming)

    #如果函数中已经定义了一个可变参数，（参数1，*kw，参数3，参数4），后面跟着的命名关键字参数就不需要单独的分隔符*
    #命名关键字参数可以使用默认参数
mingandkebian= testhan.mingandbian('tom', '男', address='湖北荆门', tell='13542365985')

#函数参数组合
    #定义函数时，可以用必选、默认、可变、关键字、命名关键字参数，这五种参数可以任意组合
    #参数定义的顺序：必须参数、默认参数、可变参数（*args）、命名关键字参数（*，参数）、关键字参数（**kw ）

print(testhan.zuheone(1, 2, c=5, name='tom', sge=12, sex='男', sddress='湖北荆州'))
print(testhan.zuhetwo('hfjsdgh', 1, c=1, d='name', sex='男', sddress='湖北荆州'))

#  参数=值：默认参数；
# （*参数）：可变参数；
# （**参数）：关键字参数；
# （*，参数）：命名关键字参数；

print('product(5) =', testhan.product(5))
print('product(5, 6) =', testhan.product(5, 6))
print('product(5, 6, 7) =', testhan. product(5, 6, 7))
print('product(5, 6, 7, 9) =', testhan.product(5, 6, 7, 9))
if testhan.product(5) != 5:
    print('测试失败!')
elif testhan.product(5, 6) != 30:
    print('测试失败!')
elif testhan.product(5, 6, 7) != 210:
    print('测试失败!')
elif testhan.product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        testhan.product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

#递归函数
    # 在函数本身去调用自己,使用递归函数注意防止栈溢出
    #函数调用是通过栈（stack）这种数据结构实现的， 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧
print(testhan.fact(5))
#尾递归，可以解决栈溢出
    #尾递归是指，咋函数返回的时候，调用自身本身，并且，return语句不能包含表达式
print(testhan.nums(5))

# endregion

# region 函数式编程
#函数式编程：把大段代码拆成函数，一层一层调用，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元
#纯粹的函数式编程编写的函数没有变量，python允许使用变量，python不是纯函数式编程
#函数式编程的特点就是，允许吧函数本身作为参数传入另一个函数，还匀速返回一个函数

#高阶函数
    #变量指向函数：函数是可以赋值给变量的，例如：f=abs，将求绝对值的函数赋值给了变量f，后面可以直接调用f函数
f=abs
print(f(-5))
    #函数名也是变量，对于abs这个函数，可以把函数名abs变量，他指向一个可以计算绝对值的函数，可以把这个函数指向其他对象

    #传入函数
def yan(a,b,f):
    f(a)+f(b)

print(yan(4,9,abs))


#map()函数接受两个参数，一个是函数，一个是iterable；map将传入的函数一次作用到序列的每个元素，并把结果作为新的iterator返回
#例如：
def f(x):
    return x*x
r=map(f,[1,2,3,4])
print(list(r))

#reduce：把一个函数作用在一个序列[x1,x2,x3,.....]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做积累计算
from functools import reduce
dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    #把字符串转换成数字
def strandint(i):
    def fn(x,y):
        return x*10+y
    def s(i):
        return dicts[i]
    return reduce(fn,map(s,i))
print(strandint('123598'))

    #求list集合的乘积
def prod(L):
    def p(x,y):
        return x*y
    return reduce(p,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


    #把带小数点的的字符串转换成数字
def str2float(s):
    i=s.index('.')
    s=s[:i]+s[i+1:]
    def cheng(x,y):
        return x*10+y
    def dic(s):
        return dicts[s]
    return reduce(cheng,map(dic,s))/(10**(len(s)-i))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

#filter()函数用于过滤序列，接收一个函数和一个序列，把传入的函数一次作用于每个元素，然后根据返回值是true还是false保留还是丢弃该元素
def is_odd(n):
    return n%2==0
print(list(filter(is_odd,[1,5,9,3,4,6,7,4,1,2,3])))

def is_palindrome(n):
    s=str(n)
    return s==s[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#sorted，python内置的sorted()函数可以对list进行排序，它也是一个高阶函数么可以接收一个key函数实现自定义排序，例如key=abs
print(sorted([3,5,-8,-12,69]))
print(sorted([3,5,-8,-12,69],key=abs))

    #字符串排序，是按照ASCLL的大小比较的，如果需要忽略大小写，可以传入忽略大小写的函数,详细用法可以参看sorted函数的详细用法
sor=['bob', 'about', 'Zoo', 'Credit']
print(sorted(sor))
print(sorted(sor,key=str.lower,reverse=True))


#返回函数：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
    #返回一个函数,在函数lazy里面定义了函数sum，并且，内部函数sum可以引用外部函数lazy的参数和局部变量
    #当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）“
def lazy(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f=lazy(1,3,5,9)
print(f())

    #注意：当我们调用函数lazy时，每次调用都会返回一个新的函数，即使传入相同的参数
f1=lazy(1,3,5,9)
f2=lazy(1,3,5,9)
print(f1==f2)

    #闭包，返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量，例如：

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

    #如果一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
    # 无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def createCounter():
    n=[0]
    def counter():
        n[0]=n[0]+1
        return n[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#匿名函数，关键字lambda函数，就是表示匿名函数。匿名函数有个限制，只能有一个表达式，不用谢reutrn，返回值就是该表达式的结果
    #匿名函数没有名字，不用担心函数名冲突；
    #匿名函数也是一个函数对象，可以把匿名函数赋值给你一个变量，在用变量来调用匿名函数
f=lambda x,y:x*y
print(f(5,6))

    #同样，也可以把匿名函数作为返回值返回
def fe(x,y):
     return lambda x,y:x*x+y*y

print(fe(5,6))


l=list(filter(lambda x:x%2==1,range(1,20)))
print(l)

#装饰器
    #函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也可以调用此函数，函数对象有一个_name_属性，可以拿到函数的名字
def han(x):
    return  x*x
f=han
print(han.__name__)
print(f.__name__)

    #现在我们要在调用函数前后自动打印日志，但是有不希望修改函数han的定义
    # 种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。本质上，装饰器就是一个返回函数的高阶函数
def log(func):#装饰器，接受一个函数
    def weperr(*arges,**kw):#定义了可变参数和命名关键字参数，可以接受任意参数的调用
        print("call %s"%func.__name__)
        return func(*arges,**kw)
    return weperr

@log#把@log放到函数的定义处，相当于执行了语句，han=log(han)
def han1():
    print('2015-5-25')
print(han1())
print(han.__name__)

    #如果Decorator本身需要传入参数，那就需要编写一个返回Decorator的高阶函数
def log(text):
    def decorator(func):
        def weperr(*arges,**kw):
            print('%s %s'%(text,func.__name__))
            return func(*arges,**kw)
        return weperr
    return decorator
@log('调用函数名：')
def han():
    print('这是一个装饰器')

print(han())
print(han.__name__)#此时去调用经过装饰器的函数，函数名就会变成装饰器函数中调用的函数名
                   # 此时需要吧原始的函数属性复制到最终调用的函数中，否则，有些依赖函数签名的代码执行就会出错
    #用python内置的模块，不需要去写函数.__name__=函数.__name__
import functools

def log(func):
    @functools.wraps(func)#复制传入函数的属性到新函数
    def wepper(*arges,**kw):
        print('call %s'%func.__name__)
        return func(*arges,**kw)
    return wepper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def weperr(*arges,**kw):
            print('%s %s'%(text,func.__name__))
            return func(*arges,**kw)
        return weperr
    return decorator

@log('函数名称：')
def han():
    print('上面是打印的日志')

print(han())

import time


def metric(fn):
    def times(*arges,**kw):
        t1=time.time()*1000
        s=fn(*arges,**kw)
        t2=time.time()*1000
        print('%s executed in %s ms' % (fn.__name__, t2-t1))
        return s
    return times

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

    #小结：面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现
    # 而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

    #调用函数前打印begin和end
def printlog(fn):
    def weperr(*agres,**kw):
        print('begin call')
        s=fn(*agres,**kw)
        print('end call')
        return s
    return weperr
@printlog
def han():
    print('函数执行完成！')
print(han())

    #@log和log('de1')的函数，支持有参数和无参数的装饰器
def log(*arges,**kw):
    def decorator(fn):
        def weperr(*arg,**kk):
            return fn(*arg,*kk)
        return weperr
    for i in arges:
        if type(i).__name__=='function':
            return decorator(i)
        else:
            print(i)
    return decorator

@log('fsdbj1')
def f():
    print('1111')
print(f())

#偏函数，functools.partial就是帮助我们创建一个偏函数的
    #functools.partial的作用就是把一个函数的某些参数给固定住，也就是这只默认参数，返回一个新函数
import functools
int2=functools.partial(int,base=2)#base参数是进行N进制的转换
print(int2('1000000'))
    #创建偏函数时，实际上可以接受函数对象、*arges、**kw这三个参数
    #当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，
    # 从而在调用时更简单。


# endregion