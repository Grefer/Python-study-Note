# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:32:47 2019

@author: Minevei
"""
a = 100
if a>=0:
    print(a)
else:
    print(-a)
print(5/4)
print('I\'m \"ok\"!')
print('I\'m learning\n\"python\"!')
# -*- coding: utf-8
b=ord('A')
print(b)
c='ABC'.encode('ascii')
print(c)
d=b'ABC'.decode('utf-8')
print(d)
print('%2d-%02d' %(3,100))
print('%.2f' % 3,1415926535897932384626)
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r=(s2-s1)/s1*100
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('Hello,%s,成绩提高了%.1f%%'%('小明',r))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    ]
print(L[0][0])
print(L[1][1])
print(L[-1][-1])
print(L[len(L)-1][-1])

age=int(input('Please enter your age:'))
if age >= 18:
    print('Adult')
else:
    print('Children')
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
h=float(input('Please input your height(m):'))
w=float(input('Please input your weight(kg):'))
BMI=w/h/h
if BMI<=18.5:
    print('Thin')
elif BMI<=25:
    print('Normal')
elif BMI<=28:
    print('Over weight')
elif BMI<=32:
    print('Fat')
elif BMI>32:
    print('Seriously fat')
    

x=list(range(101))
sum=0
for x in range(101):
    sum=sum+x
print(sum)
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello,',x)

dict={'L':200,'W':230,'Z':220}
print(dict['L'])
s1=set([0,1,2,3])
s2=set([2,3,4,5])
s1.add(4)
s2.remove(2)
print(s1&s2,s1|s2)

n1=255
n2=1000
print(hex(n1),hex(n2))

import math
def quadratic(a,b,c):
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return(x1,x2)

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
    
def product(*number):
    if len(number)==0:
        raise TypeError 
    S=1
    for n in number:
        S=S*n
    return S

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(10))


def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(1000))

def mov(n,a,b,c):
    if n==1:
        print(a,'--->',c)
    else:
        mov(n-1,a,c,b)
        mov(1,a,b,c)
        mov(n-1,b,a,c)
    return 'Done!'
print(mov(3,'A','B','C'))
print(mov(4,'A','B','C'))

def trim(s):
    n=len(s)
    i=0
    for p in s:
        while s[i:i+1]==' ':
            i=i+1  
    for q in s:
        while s[n-1:n]==' ':
            n=n-1
    print(s[i:n]) 
    print(i,n)
    return s[i:n]
    
trim('  hello  ')
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
# 去掉字符串首尾空字符

# 查找list中的最大值和最小值
def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    Max=Min=L[0]   
    for n in L:
        if    n>=Max:
            Max=n
        elif  n<=Min:
            Min=n            
    return (Min,Max)

        

# 测试
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
'''
需注意，此道题目并不需要切片，迭代+切片会输出整个list，
而我们需要对每一个值进行分别比较大小，因此直接使用list
调用更加简洁有效
'''
    
# 列表生成式
L1=['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s, str)==1]
 
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
    

#生成器generator（边循环边计算）
L3=(s.lower() for s in L1 if isinstance(s,str)==1)
next(L3)
for n in L3:
    print(n)
# 函数方法
def fib(n):
    i,a,b=0,1,1
    while i<n:
        print(b)
        a,b=b,a+b
        i=i+1
    return 'Down'
"""         a,b=b,a+b --------(a,b)=(b,a+b) 联合赋值
equal to
            t=(b,a+b)
            a=t(0)
            b=t(1)
"""
fib(4)
# 生成器方法
def fib(n):
    i,a,b=0,1,1
    while i<n:
        yield b
        a,b=b,a+b
        i=i+1
    return 'Down'

f=fib(5)
for n in f:
    print(n)


# 杨辉三角形
def triangles():
    p = [1]       
    while True:
       yield p         
       p =[1]+[p[x]+p[x+1] for x in range(len(p)-1)]+[1]
       
""" 此举真乃神人也
思路清奇，
代码明了，
不忍叹曰：
大佬大佬，
6666！
--------思路解析:
首先第一行的list为[1]，直接赋值定义------L1=[1]
第二行之后的list有个共同特点：首尾都为[1]，因此可以单独处理，[1]+...+[1]------L2=[1,1]
第三行之后的list都有新加元素且元素个数与元素值都有规律可循
    以第三行为例：新加的元素个数=len(L2)-1=1，值=L2[0]+L[1]-------L3=[1,2,1]
第四行依然：新加元素个数=len(L3)-1=2,值1=L3[0]+L3[1];值2=L3[1]+L3[2]
>>>>以此类推

     新增部分表示为： [P[x]+P[x+1] for x in range(len(L)-1)]
"""

# 测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
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
    print('测试通过!')
else:
    print('测试失败!')
    
"""
凡是可作用于for循环的对象都是Iterable（可迭代对象）类型；

凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass

实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break    
"""


def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


    
def normalize(name):
    return name.title()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce
def prod(L):
    def m(x,y):
        return x*y
    return reduce(m,L)


#test
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


###Solution A
def str2float(s):
    def char2num(s):
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':''}
        return dict[s]
    res = list(map(char2num,s))
    return reduce(lambda x,y:x if y=='' else x*10+y,res)/(10**(res.index('')))


#test
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

###Solution B
def str2float(s):
    def char2num(s):
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return dict[s]
    def fl(x,y):
        return 10*x+y
    def fr(x,y):
        return 0.1*x+y
    i=s.index('.')
    return reduce(fl,map(char2num,s[:i]))+reduce(fr,map(char2num,s[:i:-1]))*0.1
#小数点前为从左往右迭代计算，小数点后为从右往左迭代计算，且从小数点后一位开始需乘以0.1

#test
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


def is_palindrome(s):
    s1=str(s)               #将int型转为str，方便挨个儿读取
    if s1[:]==s1[::-1]:     #s[::-1]倒序输出字符串，也可以表示为s1.reverse()        
        return 1
    else:
        return 0


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)
print(L2)


"""反思与总结：
对于tuple元素是组值，调用L[0]表示第一个组值，L[1]表示第二个组值，以此类推
"""


""" 返回函数与闭包"""

def createCounter():
    i=0                                  ###外部函数声明
    def counter():
        nonlocal i                       ###内部函数声明
        i+=1
        return i
    return counter

"""
nonlocal声明使用方法总结
nonlocal只能在封装函数中使用，需要先在外部函数中声明，然后在内部函数中nonlocal声明，这样
声明的变量在内外部函数通用
"""


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
    
"""匿名函数"""

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)


print(list(filter(lambda n:n % 2==1,range(1,20))))


"""装饰器decorator"""

def now():
    print('2019年7月23日09:46:40')

f=now
def test(func):
    return func()
test(f)                 #test函数是一个传入函数，然后再返回传入函数的函数，Python特性之一



import logging

def use_logging(func):

    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的是函数对象 wrapper，这条语句相当于  foo = wrapper
foo()

"""
装饰器总结
装饰器是在不改动原函数代码框架的条件下，增加函数功能的一种方法。
在上面的例子中，函数use_logging，传入参数函数foo(),在内部继续定义函数wrapper()，函数wrapper
的功能是打印日志并返回传入函数foo()，而use_logging最终返回的是wrapper函数，通过这种嵌套达到调用原函
数foo()并新增打印日志功能。
"""

import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args,**kw)
    return wrapper


# 测试
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



"""偏函数"""

import functools
int2 = functools.partial(int,base=2)

int2('100000')

kw={'base':2}
int('100000',**kw)

max2 = functools.partial(max,10)          
max2(5,6,7)
"""这里相当于把10加入可变参数*args，也就是自动在传入的参数中加上10，因此最终结果=10"""
args = (10,5,6,7)
max(*args)


"""
可变参数&关键字参数（*args&**kw）
偏函数functool.partial()可以传入对象、*args、**kw三个参数
可变参数*args是直接传入函数的参数，一般为元素不可变的元组tuple，这个元组有多少个元素，最终
传入函数的参数就有多少个。
关键字参数**kw是一个字典dict，可以用来设定关键字key的值value，传入函数中时，可以用来更改
函数的默认关键字。
"""

"""模组Module"""

import sys

def test():   
    args = sys.argv
    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()


"""作用域"""

def _private_1(name):
    return 'Hello, %s' % name      #private

def _private_2(name):
    return 'Hi, %s' % name         #private

def greeting(name):                #public
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
















