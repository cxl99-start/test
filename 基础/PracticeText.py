# #练习1
# print("="*50)
# print("=\t 欢迎进入到身份认证系统V1.0\n=1.登录\n=2.退出\n=3.认证\n=4.修改密码")
# print("="*50)
#
# #练习2，接收用户输入的信息输出
# name=input("姓名：")
# qq=input("QQ:")
# tell=input("手机号:")
# address=input("公司地址:")
# print("="*50)
# print("姓名：%s\nQQ：%s\n手机号：%s\n公司地址：%s"%(name,qq,tell,address))
# print("="*50)
#
# #练习3，接收用户的账号密码，判断并输出
# password='123456'
# username='admin'
# user_name=input("请输入用户名：")
# pass_word=input("请输入密码：")
# if (user_name!='' and pass_word!=''):
#     if(user_name==username and pass_word==password):
#         print('欢迎登录%s'%username)
#     else:
#         print('用户名或密码输入错误！')
# else:
#     print('用户名或密码不能为空！')
#
# #练习四：写1-100的和
# x=0
# for i in range(1,101):
#     x+=i
# print(x)

# #练习四：实现一个整数加减乘除的计算器
# # a=int(input('请输入第一个数字：'))
# # fu=input('请输入运算符号：')
# # b=int(input('请输入第二个数字：'))
# # if(fu=='+'):
# #     print('%s+%s=%s'%(a,b,a+b))
# # if(fu=='-'):
# #     print('%s-%s=%s'%(a,b,a-b))
# # if(fu=='*'):
# #     print('%s*%s=%s'%(a,b,a*b))
# # if(fu=='/'):
# #     print('%s/%s=%s'%(a,b,a/b))
# # else:
# #     print('暂不支持这种运算符')

#练习五
# li = [11,22,33,44,55,66,77,88,99,90]
# li.sort()
# z=li.index(66)
# dic={"key1":li[0:z],"key2":li[z:-1]}
# print(dic)

#练习6
# li = [1,2,3,4,5,6,7,8,8]
# li2=[]
# li3=[]
# for i in li:
#     for x in li:
#         if i!=x:
#             a='%s%s'%(i,x)
#             li2.append(a)
# for s in li2:
#     if s not in li3:
#         li3.append(s)
#
# print(li3)
# print(len(li3))

#练习7：输出商品列表，用户输入序号，显示用户选中的商品
# def pr(li):
#     for i, v in enumerate(li, 1):
#         print(i, v)
# li=["电脑","显示器","笔记本","机械键盘"]
# pr(li)
# xan=input("查询还是添加新的商品：")
# if(xan=='添加'):
#     shangp=input('请输入要添加的商品名称：')
#     li.append(shangp)
#     pr(li)
# if(xan=='查询'):
#     select=input('请输入要查询的商品序号：')
#     if(select.isdecimal()):
#         print(li[int(select-1)])
#     else:
#         print('输入有误！！')


#练习8：判断润年
# nian=int(input("请输入需要判断的年份："))
# if(nian%400==0 or nian%4==0 or nian%100==0):
#     print("%s是闰年"%nian)
# else:
#     print("%s是平年" % nian)

#练习9:输入年月日,判断这一天是这一年的第几天
# def jisuan(m,d):
#     all_day=0
#     if (m > 0 and m < 12):
#         if (d > 0 and d < nian[month - 1]):
#             for i in nian[0:month - 1]:
#                 all_day += i
#             all_day += day
#         else:
#             print("天数输出超出范围，请重新输入")
#     else:
#         print("月份输出超出范围，请重新输入")
#     return  all_day
#
# zong=input("请输入格式为年-月-日的时间：")
# all_days=0
# while True:
#     nian=[31,28,31,30,31,30,31,31,30,31,30,31]
#     zongsum=zong.split('-')
#     year=int(zongsum[0])
#     month=int(zongsum[1])
#     day=int(zongsum[2])
#
#     if(year%400==0 or year%4==0 or year%100==0):
#         nian[1]=29
#         all_days=jisuan(month,day)
#         break
#     else:
#         all_days = jisuan(month, day)
#         break
#
# print('这是%s的第%s天'%(year,all_days))

#isdecimal（）函数判断是否为十进制数字，返回类型是布尔，isalpha判断是否为字符型
#练习10：计算用户输入的内容中有几个十进制小数，几个字母
# zifu=input("输入：")
# num=0
# string=0
# for i in zifu:
#     if(i.isdecimal()):
#         num+=1
#     if(i.isalpha()):
#         string+=1
# print('字符串数量为：%s，数字数量为%s'%(string,num))


#练习12:9*9
# for i in range(1,10):
#     for x in range(1,i+1):
#         print('%s*%s=%s\t'%(x,i,i*x),end="")
#     print("")


#练习13：质数
# a=[]
# for i in range(100,201):
#     count=0
#     for x in range(2,i-1):
#        if i%x==0:
#            count+=1
#     if count==0:
#         a.append(i)
# print(a)

#练习14：输出图形
# xing=1
# zong=9
# while zong>=1:
#     if zong>5:
#         print("*\t"*xing)
#         xing+=1
#     if zong<=5:
#         print("*\t"*xing)
#         xing -= 1
#     zong-=1

# li=[]
# for i in range(1,302):
#     li.append("alex-%salex%s@live.com%s"%(i,i,i))

print('='*50)
from mypackage.ObjectProgramming import Students
barts=Students('测试','111')
print(barts.get_name())
ss=barts.__name='fsdfs1'
barts.set_name('de1')

print(ss)
print(barts.get_name())


# 测试:
from mypackage.ObjectProgramming import stustrs
bart = stustrs('Bart', 'male')
print(bart.get_gender())
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')