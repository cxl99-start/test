
# region 面向对象

#面向对象：面向对象的程序设计把计算机程序视为一组对象的集合
    # 而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递
    #在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念
    #面向过程
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print(print_score(std1))

    #面向对象
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print(bart.print_score())
print(lisa.print_score())

    #面向对象的设计思想是抽象出class，根据class创建实例。抽象度比函数高，class即包含数据，又包含操作数据的方法

#类和实例：面向对象最重要的概念就是类和实例，必须牢记类是抽象的模板，比如Student类，
    # 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
    #定义类
class Student(object):#类名通常是大写开头的单词，紧接着（object），表示该类是从哪个类继承下来的，
    # 如果没有合适的继承类，就用object，这是所有的类最终都会继承的类
    pass
bart=Student()#创建类的实例，是通过类名+（）
print(bart)
bart.name='Tom'#给实例绑定一个name属性
print(bart.name)

    #由于类可以起到末班的作用，因此，在创建实例时，把我们认为一些必须的属性强制写进去，通过定义一个特殊的方法__init__，把属性写进去
    #方法__init__的第一个参数必须是self，表示创建实例本身，所以在这个方法内部，就可以把属性绑定到self上
    #有参数后，在创建实例时，就不能传入空参数了，必须传入和__init__方法匹配的参数，但是self不需要传入
    # 也可以自己使用函数的默认参数、可变参数、关键字参数和命名关键字参数
class Student(object):
    def __init__(self,name,address):
        self.name=name
        self.address=address
bart=Student('Tom','湖北荆州')

#数据封装：面向对象的一个重要特点就是数据封装。在类内部定义访问数据的函数，就把这些数据“封装”了，封装数据的函数和类本身有关联，我们称之为类的方法
class Studentes(object):
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def print_data(self):
        print('%s:%s'%(self.name,self.address))

# bart=Student('Tom','湖北荆州')
#
# print(bart.print_data())
    #封装的另一个好处就是可以给类新增新的方法
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_score(self):
        s=int(self.score)
        if s>90:
            return 'A'
        if 80<s<90:
            return 'B'
        if 60<s<80:
            return 'C'
        else :
            return 'D'
    def print_score(self):
        print('%s:评分-%s'%(self.name,self.get_score()))

bart=Student('王麻子','85')
print(bart.print_score())

    # 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；#
    # 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；#
    # 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

#访问限制：，__变量名，这种变量外部不能访问，如果要访问和修改可以给属性添加get_属性，和set_属性这样的方法
    #__变量__,特殊变量，可以直接访问，不是私有的变量
    #__变量，私有变量，只有通过get方法或者是set方法才能访问和修改变量
    #_变量，这样的实例变量可以访问，但是这样的变量一般视为私有变量，不要随便访问


class Students(object):
    def __init__(self,name,address):
        self.__name=name
        self.__address=address
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def set_name(self,name):
         self.__name=name
    def set_address(self,address):
        self.__address=address
    def print_data(self):
        print('%s:%s'%(self.__name,self.__address))

    #通过


class stustrs(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender in ('female','male'):
            self.__gender = gender
        else:
            print('传入值有误')


#继承、多态，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类，被继承的类称为基类、父类、超类
class Animal(object):
    def run(self):
        print('测试继承')
    #当父类和子类存在同样的方法时，子类会覆盖父类的方法，在运行代码的时候，总是会调用子类的方法
    # 子类的数据类型不仅仅是自身，还是父类的数据类型，反过来就不行
class c1(Animal):
    def run(self):
        print('c1 is running……')
    def eat(self):
        print('Eating meat……')
class c2(Animal):
    def run(self):
        print('c2 is running……')
class c3(object):#
    def run(self):
        print('11111111111111')

    #多态的好处：我们只需传入实体类，接受父类类型，就会自动调用其中的方法，调用方只需要调用，不需要管细节
    #开闭原则，对扩展开放：允许新增父类类型的子类。对修改封闭：不需要修改依赖父类类型的其他函数
def run_twice(animal):
    animal.run()

# c1=c1()   实例化对象
# c1.run()

print(run_twice(Animal()))
print(run_twice(c1()))
print(run_twice(c3()))
    #继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    #动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。只要有和父类一样的方法，那么也可以传入


#获取对象信息，type()函数可以获取对象的类型
    #使用type()
print(type(111))#判断对象类型
print(type(abs))#判断函数或者类的类型
import types
def fn():
    pass
print(type(fn)==types.FunctionType)#判断一个对象是否为函数，使用模块types中的常亮

a=c1()
print(isinstance(a,Animal))#对于继承关系来说，使用type不方便，就可以使用isinstance，用tyep判断的数据也可以使用isinstance()判断
    #isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上

print(isinstance([1,2,3],(list,tuple)))#可以判断一个变量是否是某些类型中的一种

    #dir()：获取一个对象的多有属性和方法，它返回一个包含字符串的list
print(dir('123'))
    #类似__xxx__的属性和方法在python中都是有特殊用途，比如返回长度，len（）函数和__len__方法实际上是一样的，len()内部就是调用的__len__方法
print('123'.__len__())

class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()
#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
print(hasattr(obj,'x'))#判断对象是否有这个属性
setattr(obj,'y',19)#设置对象属性
print(hasattr(obj,'y'))
print(getattr(obj,'y'))#获取对象属性

print(hasattr(obj,'power'))#判断对象是否含有这个方法

#实例属性和属性
    #python是动态语言，根据类创建的实例可以任意绑定属性，给实例绑定属性的方法是通过实例变量，或者通过self变量
    #可以直接在class中定义属性，这种属性是类属性，归类所有

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

# endregion

#region  面向对象高级编程

#使用__slots__
    #创建一个class之后，我们可以给实例绑定任何属性和方法给实例绑定属性，直接通过实例后的变量.属性名=值
class ban(object):
    pass

def set_age(self,age):
    self.age=age

s=ban() #给一个实例绑定的方法，对另一个实例是不起作用的，为了所有的实例都能用绑定的方法，可以直接给class绑定方法
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(12)
print(s.age)

ban.set_age=set_age
s2=ban()
s2.set_age(25)
print(s2.age)

    #如果我们要显示实例允许添加的属性，那我们可以用特殊变量__slots__，来限制class实例能添加的属性
    #需要注意的是，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    #除非是在子类中也定义了__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class xianzhi(object):
    __slots__ = ('name','address')

s3=xianzhi()
s3.name='你的名字'
print(s3.name)


#使用@property：python内置的@property装饰器就是把方法变成属性调用的
    #先用@property把getter方法变成属性，而这个装饰器本身又创建了一个setteer方法，负责把这个方法变成属性赋值
    #如果只需要定义一个可读属性，就只需要
class propertyStudent(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integeer')
        if value<0 or value>100:
            raise ValueError('学生成绩在0到100之间！')
        self._score=value

    @property  #只读属性
    def address(self):
        return self._address

p=propertyStudent()
p.score=60
print(p.score)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
          self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
         self._height=value

    @property
    def resolution(self):
        return self._height*self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
# print(s.height)
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



#多重继承：通过继承，子类可以扩展父类的功能，多重继承，一个子类就可以同时获得多个父类的所有功能
    # class 子类1(父类1，父类2，父类3……):  #多重继承
    #     pass

    #MixIn，在设计类的继承关系时，通常主线都是单一继承下来的；但是需要混入额外的功能，可以通过多重继承实现，这种设计通常称之为MixIn
    #MixIn的目的就是给一个类增加多个功能，
    # class MyTCPServer(TCPServer,ForkingMixIn):
    #     pass

#定制类：python中有很多特殊用途的函数，可以帮我们定制类
#__str__
class dingzhi(object):
    def __init__(self,name):
        self.__name=name
    #__str__和__repr__：__str__和__（）返回用户看到的字符串，__repr__（）返回程序开发者看到的字符串
    def __str__(self):
        return 'dingzhi object （name：%s）'%self.__name
    __repr__=__str__

print(dingzhi('定制类'))

# __iter__：如果一个类想被用于for……in循坏，类似于tuple那样，必须实现一个__iter__（）方法，改方法返回一个迭代对象
    # python的for循坏会不断的调用改迭代对象__next()__方法拿到循坏的下一个值，知道遇到StopIteration错误时退出循坏
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>20:
            raise StopIteration()
        return self.a

for i in Fib():
    print(i)
#__getitem__：定义了__iter__类方法的实例虽然能作用于for循坏，类似于list，但是真正当做list来使用是不行的
    # 比如取特定的元素，实例()[索引]这种方式是不能取出元素的，如果要向list一样取出元素，就需要__getitem__()方法
class Fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
print(f[5])
#list有个神奇的切片方法,对于fib实例却会报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
print(list(range(100)[5:10]))

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):#传入的参数是索引
            a, b = 1, 1
            for x in range(n):
                a,b=b,a+b
            return  a
        if isinstance(n,slice):#传入的参数是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                    a,b=b,a+b
            return L

f1=Fib()
print('实例切片：%s'%f1[5])


# __getattr__：当我们调用类的方法或属性时，如果不存在，就会报错，为了避免这个错误，可以写一个__getattr__()方法，动态返回一个属性
    #但是只有在类中没有这个属性的时候，才会去__getattr__()中查找，默认返回的就是None
class Student(object):
    def __init__(self,name):
        self.name=name

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        else:
            return '没有该属性'

s=Student('你的！')
print(s.name)
print(s.ff)
    #__getattr__()也可以返回一个函数，
class StudentAge(object):
    def __getattr__(self,attr):
        if attr=='age':
            return lambda :25

s=StudentAge()
print(s.age())#调用函数

    #链式调用：
class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self, path):
        return Chain('%s/%s'%(self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__

print(Chain().status.user.timeLine.list)

#__call__：一个对象实例可以有自己的属性和方法，任何类，只要定义一个__call__()方法，就可以直接对实例进行调用
    #__call__()也可以定义参数，
class StuCall(object):
    def __init__(self,name):
        self._name=name

    def __call__(self):
        print('我的名字是%s'%self._name)
s=StuCall('陈雪林')
print(s())

    #判断一个变量是对象还是函数，能被调用的对象就是一个Callable对象

print(callable(StuCall))

#使用枚举类：
from enum import Enum,unique
Month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)#value属性是自动赋值给成员的int常量，默认从1开始计数

    #如果需要更精确地控制枚举类型，可以从Enum派生出自定义类,@unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

    #访问枚举的若干方法
print(Weekday.Mon)   #类.枚举名
print(Weekday['Mon'])  #类['枚举名']
print(Weekday.Mon.value)   #类,枚举名.value,获取枚举的值
print(Weekday(1))  #类(枚举值)

#使用元类：动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
    #type():type()函数可以查看一个类型或变量的类型
    #type():这个函数可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello定义类
class Hello(object):   #Hello是一个class,它的类型就是type，而h是一个实例，他的类型就是class  Hello
    def hello(self,name='word'):
        print('Hello,%s'%name)
h=Hello()
type(h.hello())

    #实际调用
def fn(self,name='world'):
    print('Hello,%s' % name)

# Hello = type('Hello', (object,), dict(hello=fn))
# h=Hello()
# print(h.hello)
    #要创建一个class对象，tyoe()函数一次传入三个参数
    #1、class的名称
    # 2、继承的父类集合，注意python支持多次继承，如果只有一个父类，别忘了tuple的单元素写法
    # 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

# metaclass：除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass



#endregion

#region  IO编程

#IO编程：io在计算中是指input/output，也就是输入输出。访问网站，请求网站，叫output，然后网站根据用户的请求返回数据较input

#文件读写
#读文件：使用python内置的open（）函数，传入文件名和标示符
f=open('E:/新建文本文档 (2).txt','r') #标示符‘r’，标示读取文件，如果文件不存在，就会抛出一个IOError的错误，告诉你文件不存在
print(f.read())  #调用read（）方法可以一次读取文件的全部内容，python把内容读到内存，用一个str对象表示
f.close()  #最后一步是用close（）关闭文件。文件使用完毕后必须关闭，不然会一直占有操作系统的资源

    #由于文件读写可能会产生IOError，可以用try  finally来实现不管是否出错都关闭文件，但是比较繁琐
    # 我们就直接用python字典的with语句来自动调用close（）方法
with open('E:/新建文本文档 (2).txt') as f:
    print(f.read())
    #如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
# for line in f.readlines():
#     print(line.strip())

#file-like Object：像open（）函数返回的这种有个read（）方法的对象，在python中统称为file-like Object
    #StringIO就是在内存中创建的file-like Object，常用作临时缓冲

#二进制文件：要读取二进制的文件，如图片、视频，用‘rb'模式打开文件即可
# f=open('E:/图片/演示.png','rb')
# print(f.read())  #十六进制表示的字节

#字符编码：要读取非UTF-8编码的文本文件，需要给open（）函数传入encoding参数，例如读取GBK编码的文件：
    #如果在文本文件中可能夹杂了一些非法编码的字符，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
# f=open('E:/账.txt','r',encoding='gbk',errors='ignore')
# print(f.read())

#写文件：写文件和读文件是一样的，唯一区别是调open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
    #你可以反复调用write（）来写入文件，但是一定要调用close（）关闭文件，操作系统不会立刻把数据写入磁盘，而是放到内存放起来
    #只有调用过close（）方法时，操作系统才会把没有写入的数据全部写入磁盘。如果忘记写close可能会丢失数据，所以最好使用with语句
f=open('E:/新建文本文档 (2).txt','w')
f.write('这是写入的文件')
f.close()

with open('E:/新建文本文档 (2).txt','w') as f:
    f.write('这是一个测试数据\n')
    #要写特定的编码文本文件，请给open（）函数传入encoding参数，将字符串自动转换成指定编码
    #如果要追加到文件的末尾，我们可以传入一个参数‘a'，然后去追加到末尾

with open('E:/新建文本文档 (2).txt','a') as f:
    f.write('这是追加的内容')

#StringIO:在内存中读写str
    # 要把str写入StringIO，需要先创建一个StringIO，然后像文件一样写入就可以了：
from io import StringIO
f=StringIO()
print(f.write('hello'))  #打印的是写入字符的长度
print(f.getvalue())   #打印的是写入的字符串，getvalue（）方法用来获取写入后的str

    #读取StringIO，可以用一个str初始化StringIO，然后，想读文件一样读取：
f=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

#BytesIO:StringIO操作的只能是str，要操作二进制数据，需要使用BytesIO
    #创建一个BytesIO，然后写入bytes
from io import BytesIO
f=BytesIO()
print(f.write('中文'.encode('utf-8')))   #写入的是经过utf-8编码的bytes
print(f.getvalue())

    #读取BytesIO
f.read()

    # StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。


#操作文件和目录：Python内置的os模块可以直接调用操作系统提供的接口函数。
import os
print(os.name)  #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。os的模块的某些函数是跟操作系统相关的

    #环境变量：在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)

    #如果要获取某个环境变量的值，可以调用os.environ.get('key'):
print(os.environ.get('PATH'))

#操作文件和目录：操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print(os.path.abspath('.'))   #查看当前目录的绝对路径
print(os.path.join('E:\个人文件\练习\练习文件\基础','sest'))
    #创建一个目录
os.mkdir('E:\个人文件\练习\练习文件\基础\sest')
    #删除目录
os.rmdir('E:\个人文件\练习\练习文件\基础\sest')
    #把两个路径合成一个路径时，不要拼接字符串，要通过os.path.join，
    #拆分路径，也不要直接去split，而是通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或者是文件名
print(os.path.split('E:\个人文件\练习\练习文件\基础\sest'))
    #os.path.splitext()可以直接让你得到文件扩展名
    #拆分、合并路径的函数并不要求目录和文件真实存在，他们只是对字符串进行操作


#序列化：把变量从内存中变成可存储或传输的过程称为序列化（pickling）；把变量内容从序列化对象重新读到内存里称为反序列化（unpickling）
import pickle
    #把变量写入文件
d={'name':'Bob', 'age':20, 'score':88}
pickle.dumps(d)  #pickle.dumps()方法把任意对象序列化成一个bytes
with open('E:\新建文本文档 3.txt','wb') as f:  #打开文件
    pickle.dump(d, f)  # 把定义的变量存入文件 ,dump()


    #从文件读取变量
with open('E:\新建文本文档 3.txt','rb') as f:
    d = pickle.load(f)  #pickle.load()方法反序列化对象，此时的变量和原来的变量是完全不相干的，只是内容相同
    print(d)
# f=open('E:\新建文本文档 3.txt','rb')
# d=pickle.load(f)
# f.close()
# print(d)

#JSON：不同语言之间传递对象，就必须吧对象序列化成标志格式，比如xml，最好的序列为JSON，因为JSON表示出来是一个字符串
    #python内置的json模块提供了很完善的python对象到json格式的转换：
import json
d={'name':'Bob', 'age':20, 'score':88}
xu=json.dumps('json:%s'%d)  #类型为str
print(xu)  #dumps()返回一个str，内容是标准的str。类似的，dump（）可以直接把json写入一个file-like Object。

    #把json对象反序列化为python对象，用loads（）或者对应的load（）方法，loads（）把json对象反序列化，load从file-like Object中读取字符串并反序列化
dd=json.loads(xu)
print(type(dd))  #类型为dict

#json进阶：序列化类，dumps（）方法处理第一个o必须的obj参数外，还提供了一堆可选参数，这些参数就是让我们来定制json序列化
    #可选参数default就是把任意一个对象编程一个可序列化json的对象，我们只需要吧student专门写一个转换函数，再把函数传进去
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def studentdict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
    #类实例受限被定义的函数转换成dict，然后转换成json
classjson=json.dumps(s,default=studentdict)  #把类转换成dict，然后在转换成json
print(classjson)
    #但是下次在遇到一个新的类，又无法序列化，所以我们可以吧任意的class的实例变成dict，每一个实例class都有一个__dict__属性

print(json.dumps(s,default=lambda obj:obj.__dict__))

    #将json反序列化为一个类的实例，loads（）方法首先转换成一个dict，然后传入object_hook函数负责把dict转换为类的实例
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
print(json.loads(classjson,object_hook=dict2student))

    #对中文进行序列化，json.dumps()提供了一个ensure_ascii参数，当参数为True时，序列的值是Unicode码，为False时，直接传入中文
obj = {'name':'小明', 'age':20}
s = json.dumps(obj, ensure_ascii=True)
print(s)



#endregion

# region 图形界面
#python支持多种图形界面的第三方库,包括：TK，wxWidgets,Qt，GTK等

#Tkinter
from tkinter import *

# endregion
