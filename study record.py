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

import unittest
from mydict import Dict
class TestDict(unittest):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.asserEqual(d.a,1)
        self.asserEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d= Dict()
        d['key']= 'value'
        self.assertEqual(d.key,'value')
    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty
if __name__ == '__main__':
    unittest.main()  

#setUp&tearDown
class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
        
#练习
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score < 0 or self.score >100:
            raise ValueError('Wrong score!')
        if 0 <= self.score < 60:
            return 'C'
        elif self.score < 80:
            return 'B'
        elif self.score <= 100:
            return 'A'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

'''文档测试'''
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

#练习
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
    
'''IO编程-文件读写'''

f=open(r"C:\Users\Admin\Documents\GitHub\Python-study-Note\GBM.py")
f.read()     #文件路径前加 r 表示非转义字符
f.close()

try:
    f=open(r"C:\Users\Admin\Documents\GitHub\Python-study-Note\GBM.py")
    print(f.read())
finally:
    if f:
        f.close()

with open(r"C:\Users\Admin\Documents\GitHub\Python-study-Note\GBM.py") as f:
    print(f.read())

#file like object
'''
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object,
file-like Object不要求从特定类继承，只要写个read()方法就行,
StringIO就是在内存中创建的file-like Object，常用作临时缓冲
'''
#二进制文件
'''读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可'''
with open(r'E:\picture.png','rb') as f:
    print(f.read())
#写文件
with open(r'C:\Users\Admin\Documents\GitHub\Python-study-Note\GBM.py','w') as f:
    f.write('Hello,world')
with open(r'C:\Users\Admin\Documents\GitHub\Python-study-Note\GBM.py','r') as f:
    print(f.read())          #'r'表示读取，'w'表示写入(覆盖慎用啊！)，'a'表示增加

#练习
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

'''StringIO'''
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())     #getvalue()方法用于获得写入后的str

from io import StringIO
f=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s == '':
        break
    print(s.strip())

'''BytesIO'''
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

from io import BytesIO
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

'''操作文件和目录'''
import os
os.name       #posix，代表Linux、Unix或Mac；nt，代表Windows
os.uname_result

#环境变量
os.environ
os.environ.get('PATH')

#查看当前目录的绝对路径
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('C:\\User\\Admin','testdir')    #合并路径
## 然后创建一个目录:
os.mkdir('C:\\User\\Admin\\testdir')
# 删掉一个目录
os.rmdir('C:\\User\\Admin\\testdir')

os.path.split('C:\\User\\Admin\\testdir')    #拆分路径

os.path.splitext('C:\\User\\Admin\\testdir\\test.txt')  #获取拓展名

os.rename('test.txt','test.py')   #更改文件名

os.remove('test.py')              #删除文件

#列出当前目录所有文件
[x for x in os.listdir('.') if os.path.isdir(x)]
#列出拓展名为py的文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#输入关键字查找文件
import os
def get_all(path=os.path.abspath('.'),res=[]):
    for x in os.listdir(path):
        if os.path.isdir(x):
            get_all(x,res)
        else:
            res.append(x)
    return res
def search(k):
    def _match(x):
        return x.find(k) !=-1   #find() 检测字符串中是否包含子字符串 str,是返回开始的索引值，否则返回-1
    return list(filter(_match,get_all()))
key=input('Please input the key word:')
for x in list(map(lambda x:'filename:%s abs path:%s\n' %(x,os.path.abspath(x)),search('key'))):
    print(x)

'''序列化pickling(把变量从内存中变成可存储或传输的过程称之为序列化)'''
import pickle
d=dict(name='Mary',age=23,score=88)
pickle.dumps(d)    #把任意对象序列化成一个bytes,然后就可以把这个bytes写入文件
f=open('dump.txt','wb')
pickle.dump(d,f)  #pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()  
    
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
d

#JSON 序列化标准格式
import json
d=dict(name='Mary',age=23,score=88)
json.dumps(d)     #dumps()方法返回一个str,内容就是标准的JSON
json_str='{"name": "Mary", "age": 23, "score": 88}'
json.loads(json_str)

#JSON进阶
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Mary',23,88)
#print(json.dumps(s))   #默认情况下，dumps()方法不知道如何将类实例变为一个JSON的{}对象

#转换函数
def student2dict(std):
    return {'name': std.name,
            'age':  std.age,
            'score':std.score
            }     
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象
print(json.dumps(s,default=student2dict))
#通用方法，使用实例的__dict__属性
print(json.dumps(s,default=lambda obj:obj.__dict__))    

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#object_hook函数负责把dict转换为Student实例
print(json.loads(json_str,object_hook=dict2student))

#练习
import json
obj= dict(name='小明',age=23)
s = json.dumps(obj,ensure_ascii=False)
s
#ensure_ascii=True时，中文被转换为ASCII码，ensure_ascii=False时，中文不转换

'''进程和线程'''
#对于操作系统来说，一个任务就是一个进程（Process）,进程内的这些“子任务”称为线程（Thread）

'''多进程'''
import os
print('Process (%s) start...' %os.getpid())
pid=os.fork()      #Only works on Unix/Linux/Mac:
if pid == 0:
    print('I am child process (%s) of father process %s.'%(os.getpid()) %os.getppid)
else:
    print('I (%s) just created a child process (%s).' %(os.getpid(),pid))

#Multiprocessing
from multiprocessing import Process
import os

#子进程执行的代码
def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

#pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

#子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])   #subprocess模块启动一个子进程，然后控制其输入和输出
print('Exit code:', r)

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  #通过communicate()方法实现子进程输入
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#进程间通信
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

'''多线程'''
import time ,threading

#新线程执行的代码:
def loop():
    print('Thread %s is running...' %(threading.current_thread()).name)
    n=0
    while n <5:
        n=n+1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' %threading.current_thread().name)

print('thread %s is running...' %threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)        

#Lock

# 假定这是你的银行存款
balance = 0
def change_it(n):
    #先存后取，结果为0
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(1000000):   #循环次数足够多时，balance值!=0
        change_it(n)
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)   #多线程同时对balance进行操作，容易改乱数值

#使用lock保证balance同时只能被一个线程操作
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(1000000):
        #先要获取锁
        lock.acquire()
        try:
            #放心地改吧
            change_it(n)
        finally:
            #改完之后一定要释放锁!!!!!
            lock.release()
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#多核CPU
import threading,multiprocessing
def loop():
    x=0
    while True:
        x = x ^ 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()    

'''ThreadLocal'''        

import threading
#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student：
    std = local_school.student
    print('Hello,%s(in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student：
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题'''

'''分布式进程'''
#task_master.py
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#发送任务的队列
task_queue = queue.Queue()

#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#windows环境下绑定调用接口不能使用lambda，所以先定义函数
def get_task():
    return task_queue
def get_result():
    return result_queue
def test():
    
    #把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=get_task)
    QueueManager.register('get_result_queue',callable=get_result)
    
    #绑定端口5000，设置验证码’abc‘
    manager = QueueManager(address=('127.0.0.1',5004),authkey=b'123')
    #启动Queue
    manager.start()
    #获得通过网络访问的Queue对象
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        #放几个任务进去
        for i in range(10):
            n = random.randint(0,10000)
            print('Put task %d...' %n)
            task.put(n)
        #从result队列读取结果
        print('Try get result...')
        for i in range(10):
            r = result.get(timeout=10)
            print('Result:%s'%r)
    except:
        print('Manager error')
    finally:   
        #关闭
        manager.shutdown()
        print('master exit.')

#使用freeze缓解多线程爆炸的问题
if __name__ == '__main__':
    freeze_support()
    test()


#task_work.py
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5004), authkey=b'123')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

'''正则表达式'''

#re模块
import re
re.match(r'^\d{3}\-\d{3-8}$','010-12345')
re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

test = input('Please input your phone No.:')
if re.match(r'^\d{3}\-\d{3-8}$', test):
    print('ok')
else:
    print('failed')

#切分字符串
'a b   c'.split(' ')
re.split(r'\s+', 'a b   c')
re.split(r'[\s\,]+', 'a,b, c  d')
re.split(r'[\s\,\;]+', 'a,b;; c  d')

#分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')   #()表示分组
m.group(0)
m.group(1)
m.group(2)

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
m.groups()

#贪婪匹配
re.match(r'^(\d+)(0*)$', '102300').groups()
re.match(r'^(\d+?)(0*)$', '102300').groups()

#编译
import re
re_telephone = re.compile(r'(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()
re_telephone.match('010-4353').groups()

#练习
def is_valid_email(addr):
    if re.match(r'^\w+_?\w*@\w+?.*([.edu]|[.com]|[.org])[.cn]?',addr):
        return True
    else:
        return False


#测试
assert is_valid_email('Clare_bove@china.com.cn')
assert is_valid_email('bove@163.tbsc.edu.cn')
assert is_valid_email('bove114@163.com')
assert is_valid_email('205023323@cmsn.edu.cn')
assert is_valid_email('seft123@animal.org.cn')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

'''常用内建模块'''
#datetime
from datetime import datetime   #datetime模块包含datetime类
now=datetime.now()
print(now)
print(type(now))

dt=datetime(2015,5,1,12,20)   # 用指定日期时间创建datetime
print(dt)
dt.timestamp()            # 把datetime转换为timestamp

t=1429417200.0
print(datetime.fromtimestamp(t))   # 本地时间
print(datetime.utcfromtimestamp(t))  #UTC时间

cday=datetime.strptime('2019-09-03 15:49:00','%Y-%m-%d %H:%M:%S')
print(cday)   #str转换为datetime

now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))  #datetime转换为str
#datetime加减
from datetime import timedelta
now=datetime.now()
now
now+timedelta(hours=10)
now-timedelta(days=1)
now+timedelta(days=2,hours=12)
#本地时间转换为UTC时间
from datetime import timezone
tz_utc_8=timezone(timedelta(hours=8))
now=datetime.now()
now
dt=now.replace(tzinfo=tz_utc_8)
dt
#时区转换

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tk_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tk_dt)
# astimezone()将bj_dt转换时区为东京时间:
tk2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tk2_dt)

#练习
import re
def to_timestamp(dt_str,tz_str):
    str_dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')  #str转时间
    tz=re.match(r'^(UTC)([+|-]\d+):00$',tz_str)           #时区str分组 
    h=int(tz.group(2))                                    #取出时区组并转为int
    utc_dt=str_dt.replace(tzinfo=timezone(timedelta(hours=h)))  #设定时区
    print(utc_dt)
    return utc_dt.timestamp()                             #datetime转化为stamp

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')

'''Collections'''
#namedtuple
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
p.x
p.y
isinstance(p,Point)
isinstance(p,tuple)

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

#deque
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.pop()
q.popleft()
q

#defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
dd['key1']
dd['key2']

#ordereddict
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
d
od=OrderedDict([('a',1),('b',2),('c',3)])
od          #按照插入的顺序排序，并未key值本身
#FIFO dict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity=capacity
        
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self)-constainKey >= self._capacity:
            last=self.popitem(last=False)
            print('Remove:' ,last)
        if containKey:
            del self[key]
            print('Set:',(key,value))
        else:
            print('Add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

#ChainMap
from collections import ChainMap
import os,argparse
#构造缺省参数:
defaults={
        'color':'red',
        'user':'guest'
        }
# 构造命令行参数:
parser=argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args={k:v for k,v in vars(namespace).items() if v}

# 组合成ChainMap:
combined=ChainMap(command_line_args,os.environ,defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

#counter计数器

from collections import Counter
c=Counter()
for ch in 'Programming':
    c[ch]=c[ch]+1
c

'''base64'''

import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')    #结尾有'+'和'/'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')  #把字符+和/分别变成-和_

#练习：请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    r=len(s)%4
    if r==0:
        return base64.urlsafe_b64decode(s)
    else:
        return base64.urlsafe_b64decode(s+(4-r)*b'=')

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

'''struct'''

import struct
struct.pack('>I',10240099)
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
#bytes依次变为I：4字节无符号整数和H：2字节无符号整数
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
struct.unpack('<ccIIIIIIHH',s)
#b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24

#练习
def bmp_info(data):
    t_struct=struct.unpack('<ccIIIIIIHH',data[:30])
    if t_struct[0]==b'B' and t_struct[1]==b'M':
        return {
        'width': t_struct[6],
        'height': t_struct[7],
        'color': t_struct[9]
        }
    else:
        print('It\'s not a bmp file')

# 测试
import base64,struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

'''摘要算法简介'''
import hashlib
md5=hashlib.md5()           #MD5是最常见的摘要算法
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

import hashlib
sha1 = hashlib.sha1()       #另一种常见的摘要算法是SHA1
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())  

#练习：设计一个验证用户登录的函数，根据用户输入的口令是否正确
# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
     }
def login(user, password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    if user in db.keys():
        return md5.hexdigest() == db[user]
    else:
        return False
    
 # 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')       

#加盐练习：根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

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
    return user.password == get_md5(password+user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

'''hmac'''
import hmac
message=b'Hello,world!'
key=b'secret'
h=hmac.new(key,message,digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
h.hexdigest()

#练习

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

'''itertools'''
import itertools
natuals=itertools.count(1)
for n in natuals:
    print(n)

cs=itertools.cycle('ABC')
for n in cs:
    print(n)    

ns=itertools.repeat('A',3)
for n in ns:
    print(n)

nl=itertools.takewhile(lambda x: x <= 10,natuals)
list(nl)

'''Chain'''
for c in itertools.chain('ABC','XYZ'):
    print(c)
'''Groupby'''
for key,group in itertools.groupby('AAABBBCCCAAA'):
    print(key,list(group))
    
for key,group in itertools.groupby('AaBBbCcAAa',lambda c:c.upper()):
    print(key,list(group))

#练习：计算pi的值
import itertools
def pi(N):   
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd=itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    oddn=itertools.takewhile(lambda x:x<=(2*N-1),odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    odd4_n=map(lambda x:(-1)**((x+1)/2+1)*(4/x),oddn)
    # step 4: 求和:
    return sum(odd4_n)

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

'''contextlib'''
from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name=name
        
    def query(self):
        print('Query info about %s:' %self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

#@closing
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

'''urllib'''
from urllib import request

with request.urlopen('http://news-at.zhihu.com/api/4/news/latest') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s'%(k,v))
    print('Data:',data.decode('utf-8'))

req=request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
    
#Post
from urllib import parse

print('Login to weibo.cn...')
phone=input('Phone No.:')
passwd=input('Password:')
login_data=parse.urlencode([
        ('username',phone),
        ('password',passwd),
        ('entry','mweibo'),
        ('client_id',''),
        ('savestate','1'),
        ('ec',''),
        ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
        ])
req=request.Request('https://passport.weibo.cn/sso/login')    
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    print('Data:',f.read().decode('utf-8'))

#Handler   
#proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
#proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
#proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
#opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
#with opener.open('http://www.example.com/login.html') as f:
#    pass

#练习
import json
from urllib import request
def fetch_data(url):
    req=request.Request(url)
    with request.urlopen(req) as f:
        print('Status:',f.status,f.reason)
        data=f.read()
        return json.loads(data.decode('utf-8'))

# 测试
URL = 'http://news-at.zhihu.com/api/4/news/latest'
Data=fetch_data(URL)
print(Data)

#XML
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s,attrs: %s' %(name,str(attrs)))
        
    def end_element(self,name):
        print('sax:end_element: %s'%name)
    
    def char_data(self,text):
        print('sax:char_data: %s' %text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)


#练习
from xml.parsers.expat import ParserCreate
from urllib import request
class WeatherSaxHandler(object):
    def __init__(self):
        self.forecast = list()

    def start_element(self, name, attrs):
        #print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.city = attrs['city']
            print('城市名称：%s' % self.city)
        elif name == 'yweather:forecast':
            self.forecast.append({'date': attrs['date'], 'high': attrs['high'], 'low': attrs['low']})

    def end_element(self, name):
        pass
    def char_data(self, text):
        pass

def parseXml(xml_str):
    # print(xml_str)
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    print(handler.forecast)
    return {
        'city': handler.city,
        'forecast': handler.forecast
    }

#测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'

'''HTMLParser'''
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' % tag)

    def handle_endtag(self,tag):
        print('</%s>' % tag)

    def handle_startendtag(self,tag,attrs):
        print('<%s/>' % tag)
        
    def handle_data(self,data):
        print(data)
    
    def hundle_comment(self,data):
        print('<!---',data,'--->')
    
    def hundle_entityref(self,name):
        print('&%s:' % name)
        
    def hundle_charref(self,name):
        print('&#%s:' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

#练习
from html.parser import HTMLParser
from urllib.request import Request,urlopen
import re

def get_data(url):
   '''
   GET请求到指定的页面
   :return: HTTP响应
   '''

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
      }
   req = Request(url, headers=headers)
   with urlopen(req, timeout=25) as f:
      data = f.read()
      print(f'Status: {f.status} {f.reason}')
      print()
   return data.decode("utf-8")

class MyHTMLParser(HTMLParser):
   def __init__(self):
      super().__init__()
      self.__parsedata='' # 设置一个空的标志位
      self.info = []

   def handle_starttag(self, tag, attrs):
      if ('class', 'event-title') in attrs:
         self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
      if tag == 'time':
         self.__parsedata = 'time'
      if ('class', 'say-no-more') in attrs:
         self.__parsedata = 'year'
      if ('class', 'event-location') in attrs:
         self.__parsedata = 'location'

   def handle_endtag(self, tag):
      self.__parsedata = ''# 在HTML 标签结束时，把标志位清空

   def handle_data(self, data):

      if self.__parsedata == 'name':
         # 通过标志位判断，输出打印标签内容
         self.info.append(f'会议名称:{data}')

      if self.__parsedata == 'time':
         self.info.append(f'会议时间:{data}')

      if self.__parsedata == 'year':
         if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
            self.info.append(f'会议年份:{data.strip()}')

      if self.__parsedata == 'location':
         self.info.append(f'会议地点:{data} \n')

def main():
   parser = MyHTMLParser()
   URL = 'https://www.python.org/events/python-events/'
   data = get_data(URL)
   parser.feed(data)
   for s in parser.info:
      print(s)

if __name__ == '__main__':
   main()


#常见的第三方模块
'''Pillow'''

from PIL import Image

im=Image.open('test.png')
w,h=im.size
print('Orinal image size:%sx%s'%(w,h))
im.thumbnail((w//2,h//2))
print('Resize image to :%sx%s'%(w//2,h//2))
im.save('thumbnail.jpg','png')

#模糊工具
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.png')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.png', 'png')  

#字母验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

'''request'''
import requests
r=requests.get('https://www.douban.com')
r.status_code
r.text
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
r.url
r.encoding
r.content
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r.json
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
r.text
#发送post请求
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#传入JSON
params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params)
#上传文件
upload_files={'file':open('report.xls','rb')}   #务必'rb'二进制读取
r=requests.post('https://accounts.douban.com/login',files=upload_files)
r.headers
r.headers['Date']
r.cookie['ts']
#请求时传入cookie
cs = {'token': '12345', 'status': 'working'}
r=requests.get('https://accounts.douban.com/login',cookies=cs)
#指定超时时间
r=requests.get('https://accounts.douban.com/login',timeout=2.5)

'''chardet'''
#检测编码
import chardet
chardet.detect(b'Hello,world!')

data='离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)

data='离离原上草，一岁一枯荣'.encode('utf-8')
chardet.detect(data)

data = '最新の主要ニュース'.encode('euc-jp')
chardet.detect(data)

data='不灭之刃'.encode('gbk')
chardet.detect(data)

'''psutil'''
import psutil
#获取CPU信息
psutil.cpu_count()
psutil.cpu_count(logical=False)
psutil.cpu_times()
for x in range(10):
    psutil.cpu_percent(interval=1,percpu=True)
#获取内存信息
psutil.virtual_memory()
psutil.swap_memory()
#获取磁盘信息
psutil.disk_partitions()
psutil.disk_usage('/')
psutil.disk_io_counters()
#获取网络信息
psutil.net_io_counters()
psutil.net_if_addrs()
psutil.net_if_stats()
psutil.net_connections()
#获取进程信息
psutil.pids()
p=psutil.Process(8104)
p.name()
p.exe()
p.cwd()
p.cmdline()
p.ppid()
p.parent()
p.children()
p.status()
p.username()
p.create_time()
p.terminal()
p.cpu_times()
p.memory_info()
p.open_files()
p.connections()
p.num_threads()
p.threads()
p.environ()
p.terminate()

psutil.test()

'''图形界面GUI'''
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello,world!')
        self.helloLabel.pack()
        self.quitbutton=Button(self,text='Quit',command=self.quit)
        self.quitbutton.pack()

app=Application()
app.master.title('Hello,world')
app.mainloop()

#输入文本
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' %name)

app=Application()
app.master.title('Hello World')
app.mainloop()

'''海龟绘图'''
#导入turtle包所有内容
from turtle import *
#设置笔刷宽度
width(4)
#前进：
forward(200)
#右转90度
right(90)

#笔刷颜色
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()

#五角星
from turtle import *
def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()

#分形树
from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
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

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()

#导入socket库
import socket
'''客户端'''
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
s.connect(('www.sina.com.cn',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer=[]
while True:
    #每次最多接收1k字节
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
    
data=b''.join(buffer)

#关闭连接
s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#把接收的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)

'''服务端'''
#服务端程序
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#客户端程序
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

'''UDP编程'''
import socket
#SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

#客户端
import socket    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()


'''SMYP发送邮件'''
from mail.mime.text import MIMEText
#plain表示纯文本
msg=MIMEText('hello! send by python...','palin','utf-8')

#输入email地址和密码
from_addr = input('From:')
password = input('Password:')

#输入收件人地址
to_addr=input('To:')
#输入SMTP服务器地址
smtp_server=input('SMTP server:')

import smtplib
server=smtplib.SMTP(smtp_server,25)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


#完整邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib
 
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('From:')
password=input('Password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')

msg=MIMEText('Hello,send by Python...','plain','utf-8')
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'% to_addr)
msg['Subject']=Header('来自SMTP的问候……','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#发送HTML邮件

msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

#包含附件

msg=MIMEMultipart()
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()

msg.attach(MIMEText('Send with file...','plain','utf-8'))

    
    