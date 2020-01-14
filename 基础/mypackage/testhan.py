import math

#求解
def quadratic(a, b, c):

    num1 = (-b + math.sqrt(abs(b * b - 4*a*c))) / (2*a)
    num2 = (-b - math.sqrt(abs(b * b - 4*a*c))) / (2*a)
    return num1,num2

#绝对值
def my_testabs(num):
    if  num>0:
        return num
    elif num<0:
        return  -num

#默认参数
def power(x,n=2):
    s=1
    while  n>0:
        n=n-1
        s=s*x
    return s

#可变参数,不定长参数
def calc(*nums):
    sum=0
    for x in nums:
        sum=sum+x*x
    return sum

#关键字参数，传入的关键字参数在函数内部自动封装成dict，**标志关键字参数
def guanjian(name,sex,**address):
    return name,sex,address

#命名关键字参数
def mingming(name,sex,*,address,tell):
    return name,sex,address,tell

#可变参数后面的命名关键字参数无需用分隔符*
def mingandbian(name,sex,*age,address,tell):
    return name,sex,age,address,tell

#函数参数组合
def zuheone(a,b,c=1,*duo,**kw):
    return a,b,c,duo,kw
def zuhetwo(a,b,c=0,*,d,**kw):
    return a,b,c,d,kw

#函数练习
def product(a,*x):
    sum=a
    for n in x:
         sum=sum*n
    return sum

#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

#尾递归
# def pi(n):
#     return num(n,1)
def nums(n,m=1):
    if n==1:
        return m
    return nums(n-1,n*m)

#切片函数，去除字符串两端的空格
def trim(s):
    if s[0:1]==' ':
        return  trim(s[1:])
    elif s[-1:]==' ':
        return trim(s[:-1])
    else:
        return s

#迭代练习
def findMinAndMax(l):
    if len(l)>0:
        max1 = l[0]
        min1 = l[0]
        for s in l:
            if  s>max1:
                max1=s
            if s<min1:
                min1=s
    else:
        max1 = None
        min1 = None
    return min1,max1;

def f(x):
    return x*x
r=map(f,[1,2,3,4])
# tuple(r)

print(list(r))


class Dict(object):
    '''
      Simple dict but also support access as x.y style.

       d1 = Dict()
       d1['x'] = 100
       d1.x
      100
       d1.y = 200
       d1['y']
      200
       d2 = Dict(a=1, b=2, c='3')
       d2.c
      '3'
       d2['empty']
      Traceback (most recent call last):
          ...
      KeyError: 'empty'
      d2.empty
      Traceback (most recent call last):
          ...
      AttributeError: 'Dict' object has no attribute 'empty'
      '''
    def __init__(self,**kw):
        super().__init__(**kw)

    # def __getter__(self,key):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setter__(self,key,value):
        self[key]=value

if __name__=='__main__':
    import doctest
    doctest.testmod()