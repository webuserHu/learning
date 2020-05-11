#基础函数官方文档
#http://docs.python.org/3/library/functions.html#abs

#函数1-------------------------------------
#def myfunc(x):
#	if x > 0:
#		return ">0"
#	elif x==0:
#		return "=0"
#	else:
#		return "<0"
#如果你已经把myfunc()的函数定义保存为py文件了，
#那么，可以在该文件的当前目录下启动Python解释器，
#用from py_hanshu import myfunc来导入my_abs()函数，注意py_hanshu是文件名（不含.py扩展名）

#函数2-------------------------------------
#空函数
#def nop():
#    pass
#pass也可以用在语句中,如:
#if age >= 18:
#    pass

#函数3
#检查参数类型和异常处理
#def my_abs(x):
#    if not isinstance(x, (int, float)):		#检查类型
#        raise TypeError('bad operand type')	#抛异常
#    if x >= 0:
#        return x
#    else:
#        return -x

#函数4
#返回多个返回值
'''
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
'''

#函数5
'''
def add_end(L=None):
    if L is None:       #判断空
        L = []
    L.append('END')
    return L
print(add_end())
'''

#函数6
#传入数组
'''
def sum(nums):
    sum = 0;
    for num in nums:
        sum = sum + num
    return sum
print(sum(list(range(101))))
print(sum([1,2,3,4]))
'''

#函数7
#传入不定数量参数
'''
def sum(*nums):
    sum = 0;
    for num in nums:
        sum = sum + num
    return sum
nums = [0,1,2,3]
print(sum(nums[0],nums[1],nums[2]))     #一个一个传
print(sum(*nums))                       #传全部
'''

#函数8
#关键字,kw可不传,可传任意
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30))                        # name: Michael age: 30 other: {}
print(person('a3',40,gender='m',city='beijing'))    # name: a3 age: 40 other: {'gender': 'm', 'city': 'beijing'}
'''

#函数9
#复杂函数
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)         # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)    # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')    # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)     # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
'''

#函数10
#递归 n! = 1 x 2 x 3 x ... x (n-1) x n
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(3))
'''
                                #相当于
                                #===> fact(5)
                                #===> 5 * fact(4)
                                #===> 5 * (4 * fact(3))
                                #===> 5 * (4 * (3 * fact(2)))
                                #===> 5 * (4 * (3 * (2 * fact(1))))
                                #===> 5 * (4 * (3 * (2 * 1)))
                                #===> 5 * (4 * (3 * 2))
                                #===> 5 * (4 * 6)
                                #===> 5 * 24
                                #===> 120

#函数11
#迭代dict(map)
'''
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key,':',d[key])
'''
#迭代字符串
'''
for c in "ABCDE":
    print(c)
'''
#判断是否可迭代
'''
from collections import Iterable
print(isinstance('abc',Iterable))       #return true or false
'''

#函数12
'''
#生成list,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L0 = list(range(1,11))
#生成list[1x1, 2x2, 3x3, ..., 10x10]方式1
L1 =[]
for i in range(1,11):
    L1.append(i*i)
#生成list[1x1, 2x2, 3x3, ..., 10x10]方式2
L2 = [x*x for x in range(1,11)]
#list [4, 16, 36, 64, 100]
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
#list['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L2)
'''
