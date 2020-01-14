# region 多进程

#进程和多线程：对于操作系统来说，一个任务就是一个进程，比如打开一个浏览器，打开一个记事本，一个任务就是一个进程
    #而每个进程不可能只做一件事，比如word，可以写字，可以打印，而在一个进程内部，要同时做多件事，就要打开多个子任务，而这些子任务称之为’线程‘
    #多任务实现的三种方式：多进程模式；多线程模式；多进程+多线程模式。

#多线程：os模块封装了常见的系统调用，包括fork，可以在python程序中轻松的创建子进程,子进程永远为零，父进程返回子进程的id
    #注意，在window系统下，os的fork属性是不能用的，用的multiprocessing模块去代替
    # p = Process(target=test)  前面加上   if __name__=="__main__"：   语句，才不会报错


# 1、创建进程:multiprocessing(Windows下)
'''
from multiprocessing import Process,Pool
import os
import multiprocessing
import time
def action(a,b):
    for i in range(2):
        print(a,'',b)
        time.sleep(0.1)
if __name__=='__main__':
    j1=Process(target=action,args=('进程1',0))
    j2=Process(target=action,args=('进程2',1))
    j1.start()
    j2.start()

    j1.join()
    j2.join()

    print('所有进程执行完毕')
    j1.close()
    j2.close()

'''
#进程池：Pool，如果要启动大量的子进程，可以用进程池的方式批量创建进程

'''
def action1(name,b=2):
    for i in range(b):
        print(name,':',os.getpid())
        time.sleep(0.1)

if __name__=='__main__':
    ci=Pool(3)
    ci.apply_async(action1,args=('进程1',))
    ci.apply_async(action1, args=('进程2',3))
    ci.apply_async(action1, args=('进程3',1))
    ci.close()
    ci.join()
    print('执行完主进程后打印的')
    '''

#进程间的通信：Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据

'''
def foo(a):
    ss=a.get() # 管子的另一端放在子进程这里，子进程接收到了数据
    print('子进程已收到数据...')
    print(ss)

if __name__=='__main__':
    tx=multiprocessing.Queue()
    jc=multiprocessing.Process(target=foo,args=(tx,))
    print('主进程准备发送数据...')
    tx.put('有内鬼，终止交易！')  # 将管子的一端放在主进程这里，主进程往管子里丢入数据↑
    jc.start()
    jc.join()

'''

#子进程：有时候，子进程并不是自身，而是一个外部进程，subprocess模块可以让我们非常方便地启动一个子进程，然后控制输入和输出
# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

    #如果子进程还需要输入，则可以通过communicate()方法输入
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code:', p.returncode)

 #于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
    # 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
#小结：在Unix/Linux下，可以使用fork()调用实现多进程。
# 要实现跨平台的多进程，可以使用multiprocessing模块。
# 进程间通信是通过Queue、Pipes等实现的。
# endregion

#region  多线程

#多任务可以有多进程完成，也可以由一个进程内的多线程完成；一个进程至少有一个线程
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装

    #启动一个线程就是把一个函数传入并创建Thread实例，然后调用start（）开始执行
import time,threading
def loop():
    print('thread %s is running......'%threading.current_thread().name)
    for i in range(1,6):
        print('thread %s>>>%s'%(threading.current_thread().name,i))
        time.sleep(1)
    print('thread %s is ended......' % threading.current_thread().name)

print('thread %s is running......'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s is ended......' % threading.current_thread().name)

    #任何一个进程都会默认启动一个线程，我们把该线程称为主线程，主线程又可以启动新线程
    #current_thread（）函数永远返回当前线程的实例，主线程实例的名字叫做MainThread，子线程的名字在创建时指定

#Lock：由于线程的调度是由系统去进行的，可能出现交替执行的情况，如果变量在线程之间是共享的，那么不同的线程回去修改这个变量，
    #导致于变量不会是我们最终期望的结果，所以我们在一个线程操作变量时，为了防止其他线程操作变量，会给变量加一个锁
    #当多个线程同时执行lock,acquire()时，只有一个线程能成功获得锁，然后继续执行代码，其他线程就继续等待着直到获得锁
    #不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致所有程序全部挂起，无法开始，也无法结束
import time, threading

# 假定这是你的银行存款:
balance = 0
lock=threading.Lock()  #实例化锁
def change_it(n):
    # 先存后取，结果应该为0:
    global balance   #全局变量，所有的线程都能调用
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()#获取锁
        try:
            change_it(n)
        finally:
            lock.release()  #修改完变量后一定要释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)




#endregion

#region   ThreadLocal

#ThreadLocal：每个线程都有自己的数据，一个线程使用自己的局部变量比使用全局变量好，ThredLocal不用查找dict，自动做这件事情
import threading
#创建全局ThreadLocal对象
local_school=threading.local()

def process_student():
    std=local_school.student
    print('你好，%s（in %s）'%(std,threading.current_thread().name))

def process_thread(name):
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('Tom',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题

#endregion

#region 线程和进程的优缺点

'''
如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

多进程：最大的优点就是稳定性高，一个子进程崩溃不会影响其他子进程和主进程；缺点就是创建进程的代价大

多线程：多线程的效率比多进程高；缺点就是任何一个线程挂掉，都可能会导致整个进程崩溃

#无论是多进程还是多线程，只要数量一多效率都不会快；多任务一旦多到一个限度，就会消耗所有的资源，效率急剧下降，所有的任务都做不好

计算密集型：计算密集型任务的特点是要进行大量的计算，任务越多，花在任务切换的时间越多

IO密集型：设计到网络、磁盘IO的任务都是IO密集型任务，特点是CPU消耗很少，任务大部分时间都在等待IO操作完成；
          对于IO密集型任务，任务越多，CPU效率越高，但是也有一个限度

异步IO：如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，
        这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务
'''



#endregion

#region   分布式进程--------未看完，并不懂

#python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上

#应用场景：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，
    # 现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
    #原有的Queue继续使用，但是通过managers模块把Queue通过网络暴露出去，让其他机器可以访问Queue

# import random,time,queue
# from multiprocessing.managers import BaseManager
# task_queue=queue.Queue()   #发生任务的队列
# result_queue=queue.Queue()   #接受结果的队列
#
# class QueueManger(BaseManager):  #从BaseManger继承QueueManger
#     pass
#
# def task_q():
#     return task_queue
#
# def result_q():
#     return result_queue
#
#
# #把两个Queue都注册到网络上，callable参数关联了Queue对象
# QueueManger.register('get_task_queue',callable=lambda :task_q)
# QueueManger.register('get_result_queue',callable=lambda :result_q)
#
# #绑定端口5000，设置验证码’abc‘
# manger=QueueManger(address=('',5000),authkey=b'abc')
#
# #启动Queue
# manger.start()
# #获得通过网络访问的Queue对象
# task=manger.get_task_queue()
# result=manger.get_result_queue()
# #放几个任务进去
# for i in range(10):
#     n=random.randint(0,10000)
#     print('put task %s......'%n)
#     task.put(n)
#
# #从result队列读取结果
# for i in range(10):
#     r=result.get(timeout=50)
#     print('Result:%s '%r)
# #关闭
# manger.shutdown()
# print('master exit.')


#endregion

#region




#endregion
