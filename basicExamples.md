

```python
#Python Program to Find the Square Root
print('Python Program to Find the Square Root :')
print("For positive numbers using exponent ** : ")
num = int(input('\tEnter a number : '))
#print('\tThe square root of %d is %.2f' %(num,num**0.5))
print('\tThe square root of {} is {}\n'.format(num,num**(1/2)))
print("For real or complex numbers using cmath module :")
import cmath as cm
z = eval(input('\tEnter a complex number : (format a+bj)'))
print('\tThe square root of {} is {}\n'.format(z,cm.sqrt(z)))


```

    Python Program to Find the Square Root :
    For positive numbers using exponent ** : 
    	Enter a number : 6
    	The square root of 6 is 2.449489742783178
    
    For real or complex numbers using cmath module :	Enter a complex number : (format a+bj)6+5j
    	The square root of (6+5j) is (2.6277604224802014+0.9513804906310237j)
    



```python
#Python Program to Calculate the Area of a Triangle
'''If a, b and c are three sides of a triangle. Then,
    s = (a+b+c)/2
    area = √(s*(s-a)*(s-b)*(s-c))'''
print('Python Program to Calculate the Area of a Triangle :')
a = eval(input('\tEnter fisrt side :'))
b = eval(input('\tEnter second side :'))
c = eval(input('\tEnter third side :'))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('\tThe area of the triangle is : {}'.format(area))
```

    Python Program to Calculate the Area of a Triangle :
    	Enter fisrt side :152
    	Enter second side :326
    	Enter third side :32
    	The area of the triangle is : (1.2486800252870225e-12+20392.49236851641j)



```python
#Python Program to Solve Quadratic Equation
'''ax^2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0'''
print('Python Program to Solve Quadratic Equation :')

a = eval(input('Enter the first coefficient (>0) :'))
b = eval(input('Enter the second coefficient : '))
c = eval(input('Enter the third coefficient : '))

import cmath
delta = b**2 - 4*a*c
sol1 = (-b-cmath.sqrt(delta))/(2*a)
sol2 = (-b+cmath.sqrt(delta))/(2*a)

if(delta == 0):
    print('The equation has unique solution : %.2f' %sol1.real)
elif(delta > 0):
    print('The equation has two real solutions {} and {}'.format(sol1.real,sol2.real))
else:
    print('The equation has two complex solutions {} and {}'.format(sol1,sol2))
```

    Python Program to Solve Quadratic Equation :
    Enter the first coefficient (>0) :1
    Enter the second coefficient : 5
    Enter the third coefficient : 6
    The equation has two real solutions -3.0 and -2.0



```python
#Python Program to Swap Two Variables
print('Python Program to Swap Two Variables :')
a = eval(input('Enter the first value a : '))
b = eval(input('Enter the second value b : '))
print('Before swaping  a = {} and b = {} '.format(a,b))
# temp = a 
# a = b
# b = temp
#Without Using Temporary Variable : a,b = b,a
a,b = b,a
print('After swaping  a = {} and b = {} '.format(a,b))


```

    Python Program to Swap Two Variables :
    Enter the first value a : 1
    Enter the second value b : 2
    Before swaping  a = 1 and b = 2 
    After swaping  a = 2 and b = 1 



```python
#Python Program to Generate a Random Number
print('Python Program to Generate a Random Number : ')
# To generate random number in Python, randint() function is used. This function is defined in random module.
import random
print('Generate an integer number between 0 and 9')
x = random.randint(0,9)
print(x)
print('Generate a floating number between 0 and 9')
x = random.uniform(0,9)
print(x)
```

    Python Program to Generate a Random Number : 
    Generate an integer number between 0 and 9
    6
    Generate a floating number between 0 and 9
    8.64424603005601



```python
# pow2 = []
# for x in range(10):
#     pow2.append(2**x)
pow2 = [2 ** i for i in range(10)]
print(pow2)
```

    [2, 4, 8, 16, 32, 64, 128, 256, 512]



```python
i = 0
while i < 5:
    print(i)
    i += 1

```

    0
    1
    2
    3
    4



```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4



```python
sum = lambda a,b,c,p : ((a + b)*c)**2
print(sum(1,1,2,2))
```

    16



```python
def f(x):
    return lambda a : a * x
d = f(3)
print(d(2))
```

    6



```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
```

    John
    36



```python
class module:
  def __init__(slef, name, note):
        slef.name = name
        slef.note = note
        
n = module('math',19)

listOfClass = list()
```

    19



```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
# print(next(myit))
print(next(myit))
```

    apple
    banana



```python
import platform

x = platform.system()
print(x)
x = dir(platform)
print(x) 
```

    Linux
    ['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_parse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']



```python
ages = [5, 12, 17, 18, 24, 32]

def testAge(age):
    if age > 18:
        return age
    
adults = list(filter(testAge,ages))

print(adults)
        
```

    [24, 32]



```python
chd = list(filter(lambda x : x < 18 ,ages))
print(chd)
```

    [5, 12, 17]



```python
odd = list(filter(lambda x : x % 2 == 0,ages))
print(odd)
even = list(filter(lambda x : x % 2 != 0,ages))
print(even)
```

    [12, 18, 24, 32]
    [5, 17]



```python
fName = ['emin','joe']
lName = ['amaach','doe']

fullName = list(map(lambda f,l : f + ' ' + l,fName,lName))

print(fullName)
```

    ['emin amaach', 'joe doe']



```python
from functools import reduce
sum = reduce(lambda x,y : x + y,range(1,10))
print(sum)
```

    45



```python
x = [1,2]
y = x
print(x,y,sep = ' # ')
x[0] = 2
print(x,y,sep = ' # ')
x = [4,3]
print(x,y,sep = ' # ')

```

    [1, 2] # [1, 2]
    [2, 2] # [2, 2]
    [4, 3] # [2, 2]



```python
generato = (i * i for i in range(2,8))
for x in generato:
    print(x)
print(type(generato))

```

    4
    9
    16
    25
    36
    49
    <class 'generator'>



```python
x ,y = 0,'l'
if x is not y:
    print('have diffrent types')

```

    have diffrent types



```python

type(divmod(7,2))
```




    tuple




```python
import pymongo
```


```python
import mysql.connector

```
