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




"""面向过程与面向对象"""
#    Process Oriented Programming(POP)
std1={'name':'Bob','score':98}
std2={'name':'Tom','score':95}

def print_score(std):
    print('%s,%s' %(std['name'],std['score']))

#    Object Oriented Programming(OOP)
class Student(object):
    def __init__(self,name,score):   #定义类属性的特殊方法“__init__”前后分别有两个下划线！！！
        self.name = name
        self.score = score
    def print_score(self):           #类内部定义函数实现数据封装
        print('%s:%s' %(self.name,self.score))
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=80:
            return 'B'
        elif self.score >=60:
            return 'C'
        else:
            return 'D'
            

Mary = Student('Mary',60)
Jerry = Student('Jerry',75)

Mary.print_score()
Jerry.print_score()
print(Mary.name,Mary.get_grade())
print(Jerry.name,Jerry.get_grade())

"""
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，
不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、
关键字参数和命名关键字参数。
"""

# 访问限制

class Student(object):
    def __init__(self,name,score,gender):   #定义类属性的特殊方法“__init__”前后分别有两个下划线！！！
        self._name = name
        self._score = score
        self._gender = gender
    def print_score(self):           #类内部定义函数实现数据封装
        print('%s:%s:%s' %(self._name,self._score,self._gender))
    def get_grade(self):
        if self._score >=90:
            return 'A'
        elif self._score >=80:
            return 'B'
        elif self._score >=60:
            return 'C'
        else:
            return 'D'
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def get_gender(self):
        return self._gender
    def set_name(self,name):
        if type(name)==str:
            self._name = name
        else:
            raise ValueError('bad name')
    def set_score(self,score):
        if 0<=score<=100:
            self._score=score
        else:
            raise ValueError('bad score')
    def set_gender(self,gender):
        if gender == 'male' or 'famale':
            self._gender = gender
        else:
            raise ValueError('bad gender')
# 测试:
bart = Student('Bart',98,'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

Mary=Student('Mary',99,'female')
Mary.name

'''继承与多态'''

class Animal(object):
    def run(self):
        print('Animal is running...')
    
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog=Dog()
dog.run()
cat=Cat()
cat.run()

#判断数据类型
a=list()
b=Animal()
c=Dog()
isinstance(a,list)
isinstance(b,Animal)
isinstance(c,Dog)
isinstance(c,Animal)

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())


'''获取对象信息'''
type(123)
type('str')

import types
def fn():
    pass
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x:x)==types.LambdaType
type(x for x in range(10))==types.GeneratorType

isinstance([1,2,3],(list,tuple))

len('ABC')
'ABC'.__len__()


'''实例属性和类属性'''
class Student(object):
    def __init__(self,name):
        self.name=name
        
s=Student('bob')
s.score=90            #实例绑定属性

class Student(object):
    name='Student'    #类本身绑定属性

s=Student()
print(s.name)
print(Student.name)
s.name='Cony'
print(s.name)         #实例属性优先级高于类属性
print(Student.name)
del s.name
print(s.name)


class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1      #每创建一个实例，该属性+1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


'''使用__slots__'''
class Student(object):
    pass

s=Student()
s.name='Tom'
print(s.name)

def set_age(self,age):              #定义一个函数作为实例方法
    self.age=age
    
from types import MethodType
s.set_age=MethodType(set_age,s)     #给实例绑定一个方法
s.set_age(25)                       #调用实例方法
s.age

s2=Student()
s2.set_age(25)
s2.age                              #实例方法不通用

def set_score(self,score):
    self.score=score
Student.set_score=set_score         #给类绑定方法

s.set_score(100)
s.score                             #对每个实例都有效
s2.set_score(98)
s2.score                            #对每个实例都有效

class Student(object):
    __slots__ = ('name','age')      #用tuple定义类允许绑定的属性
s=Student()
s.name='Bob'
s.age=30
s.score=100                         #绑定此属性报错

class GraduateStudent(Student):
    pass
s2=GraduateStudent()
s2.score=100                        #子类不受__slots__绑定类属性限制

'''使用@property'''
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('Score must be integer!')
        if 0<=score<=100:
            self._score=score
        else:
            raise ValueError('Score must between 0~100!')

s=Student()
s.set_score(60)
s.get_score()

class Student(object):
    @property
    def score(self,score):
        return self._score
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('Score must be integer!')
        if 0<=score<=100:
            self._score=score
        else:
            raise ValueError('Score must between 0~100!')

'''getter&setter'''
s=Student()
s.score=90                         #实际转化为s.set_score(90)
s.score                            #实际转化为s.get_score()

class Student(object):
    @property                      #property用来定义读取属性,ie:getter
    def birth(self):
        return self._birth
    @birth.setter                  #setter用来定义写入属性
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2019-self.birth


#练习
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def resolution(self):
        return self._width*self._height
    @width.setter
    def width(self,value1):
        if not isinstance(value1,int):
            raise ValueError('Width must be integer!')
        self._width=value1
    @height.setter
    def height(self,value2):
        if not isinstance(value2,int):
            raise ValueError('Height must be integer!')
        self._height=value2


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')        


'''多重继承'''
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
#MixIn

class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass
class Bat(Mammal,FlyableMixIn,CarnivorousMixIn):
    pass
class MyTCPServer(TCPServer,ForkingMixIn):             #多进程TCP服务
    pass
class MyUDPserver(UDPserver,ThreadingMixIn):           #多线程UDP服务
    pass
class MyTCPServer(TCPServer,CoroutineMixIn):           #类MyTCPServer可以访问Coroutine,但不是它的子类
    pass


'''定制类'''
#__str__&__repr__
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object(name:%s)' % self.name
    __repr__=__str__

print(Student('Michael'))         #调用__str__，返回用户看到的字符串
s=Student('Michael')              
s                                 #调用__repr__，返回开发者看到的字符串，调试

#__iter__
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self               #实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a >100000:
            raise StopIteration()
        return self.a
        
for n in Fib():
    print(n)

#__getitem__
class Fib(object):
    def __getitem__(self,n):     #__setitem__&__delitem__
        if isinstance(n,int):            
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L

f=Fib()
f[0]
f[1]
f[2]
f[100]
f[0:5]
f[:10]

#__getattr__
class Student(object):
    def __init__(self):
        self.name='Michael'
    def __getattr__(self,attr):      #动态返回属性
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attrbute \'%s\'' % attr)

s=Student()
s.score
s.age()
s.gender        #默认返回None(空白)，定义返回值后更改
#调用URL的API
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__

Chain().status.user.timeline.list

#__call__
class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s.' %self.name)

s=Student('Michael')
s()

callable(Student())
callable([1,2,3])
callable(s)             #加入__call__的类实例可调用

'''使用枚举类'''
from enum import Enum                #Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thr=4
    Fri=5
    Sat=6

day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1==Weekday.Mon)
print(day1==Weekday.Tue)
print(day1==Weekday(1))
Weekday(7)
for name,member in Weekday.__members__.items():
    print(name,'=>',member)

#练习
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')    

'''使用元类'''
#type
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s.' %name)

h=Hello()
h.hello()
print(type(Hello))
print(type(h))


def fn(self,name='world'):
    print('Hello,%s' %name)
    Hello=type('Hello',(object,),dict(hello=fn))    #创建Hello class   
h=Hello()
h.hello()
print(type(Hello))
print(type(h))

'''要创建一个class对象，type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
   上例中(object,)这里多一个’,‘就是tuple的单元素写法，与括号区分！！！
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。'''

#metaclass元类
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)           #MyList可以调用add()
L
L2=list()
L2.add(1)          #p普通的list没有add()方法
L2

#ORM对象关系映射

class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)
    
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
    
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s' % name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s==>%s' %(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings      #保持属性和列的映射关系
        attrs['__table__']=name             #假设表明和类名一致
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" %key)
    def __setattr__(self,key,value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' %(self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS:%s' % str(args))

class User(Model):
    #定义类的属性到列的映射：
    id=IntegerField('id')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

'''错误处理'''
#错误代码
from logging import some_function
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    #do something
    return r

def bar():
    r = foo()
    if r ==(-1):
        print('Error')
    else:
        pass

#try
try:
    print('try...')
    r = 10 / int('2')
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
except ValueError as e:
    print('ValueError:',e)
else:
    print('No error!')
finally:
    print('finally...')
print('END')

try:
    foo()
except ValueError as e:
    print('ValueError：',e)
except UnicodeError as e:
    print('UnicodeError:',e)
#注意：第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
#常见的错误类型和继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error;',e)
    finally:
        print('finally...')

#错误的调用栈

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    bar('0')
main()

#记录错误
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')

#抛出错误
class FooError(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise FooError('Invalid value:%s'%s)
    return 10/n
foo('0')

def foo(s):
    n=int(s)
    if n==0:
        raise ValueError('Invalid value:%s'%s)
    return 10/n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()

try:
    10/0
except ZeroDivisionError:
    raise ValueError ('Input error')

#练习

from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        print('The %s is not int or float type' %s)
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

'''调试'''

#print
def foo(s):
    n=int(s)
    print('>>>n=%d'%n)
    return 10/n
def main():
    foo('0')
main()

#断言
def foo(s):
    n=int(s)
    assert n!=0,'n is zero!'      #断言n!=0，否则就调用AssertionError
    return 10/n
def main():
    foo('0')
main()

'''启动Python解释器时可以用-O参数来关闭assert,断言的开关“-O”是英文大写字母O，不是数字0'''

#logging
import logging
logging.basicConfig(level=logging.INFO)    #指定记录信息的级别debug/info/warning/error
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)

#pdb&pdb.set_trace()
'''启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
import pdb，在可能出错的地方放一个pdb.set_trace()，设置一个断点'''
#IDE
'''
目前比较好的Python IDE有：
Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
PyCharm：http://www.jetbrains.com/pycharm/
'''

'''单元测试'''
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" %s)
    def __setattr__(self,key,value):
        self[key]=value


    
