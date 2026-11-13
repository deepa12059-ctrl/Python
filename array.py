import array
x=array.array('i',[12,7,5,34,65])
print('Array value is:',x)
print(type(x))
import array as ar
res=ar.array('d',(23,4,6,8,13))
print('Result is:',res)
import array as ar
res=ar.array('I',(5,7,9,12,14))
print('Result is:',res)
#String - unicode character - collection of characters or numbers enclosed 
#within a single,double or triple quotation 
res=ar.array('u',('12345'))
print('Result is:',res)
res=ar.array('u',('C,C++,Java,Python'))
print('Result is:',res)
#Array Operations 
a=ar.array('I',(5,7,9,12,14))
print('Result is:',a)
a.append(12)
print('After Appending:',a)
a.extend([13,45,60,90])
print(a)
a.insert(3,10)
print(a)
print(max(a))
print(min(a))
print(sum(a))
#print(a.sort())
a.reverse()
print(a)
print(a[-1])
print(a[1:9])
print(a[::-1])
import array as ar
a=ar.array('f', [60, 45, 13, 12, 14, 12, 10, 9])
print('Array Element is:',a)
print(len(a))
a=ar.array('h', [60, 45, 13, 12, 14, 12, 10, 9])
print('Array Element is:',a)
import array as ar
x=ar.array('i',[60, 45, 13, 12, 14, 12, 10, 9])
y=ar.array('i',[45,90,60,25])
#z=ar.array('L')
z=x+y #Concatenation - +
print('Array of z is:',z)
#Removing/Deleting elements of an array
del a[0]
print('After deleting the array:',a)
a.pop()
print('After removing the last element:',a)
a.pop(2)
print('After removing the last element:',a)
a.remove(13)
print('After removing the last element:',a)
#Looping through an array
a=ar.array('f',[1.2,2.2,3.3,4.4,5.5,6.6])
print('All Values:')
for x in a:
    print(x) 
print('Specific Values:')
for x in a[1:5]:
    print(x)
#Looping through an array
a=ar.array('d',[1.2,2.2,3.3,4.4,5.5,6.6])
print('All Values:')
for x in a:
    print(x)
print('Specific Values:')
for x in a[1:5]:
    print(x)
    #Difference Between Global and Local Variable
def func(x):
    print('Inside the function',x) #Local Variable
x=input('Enter the String')
func(x)
print('Outside the Function:',x) #Global Variable
y=5 #Global Variable
def fun():
    x=10 #Local Variable
    print('Local Variable x is:',x)
fun()
print('Global Value of x is:',y)
#How to access the global value inside the function
x="Global"
def func():
    global x
    y="Local"
    x=x*2
    print('Global Value of x is:',x)
    print('Local Value of y is:',y)
func()
def first(msg):
    print(msg)
first('Hello')
second=first
second('Good Morning')
def first(msg):
    print(msg)
first('Hello')
second=first
second('Good Morning')
third=second
third('Welcome to Python Class')
def inc(x):
    return x+1
def dec(x):
    return x-1
def operate(func,x):
    result=func(x)
    return result
print('Increment value is:',operate(inc,5))
print('Decrement value is:',operate(dec,6))
#A Python Program to Search for the Position of an element in an array 
#using index() method
from array import *
x=array('i',[])
#store the elements into the array x
print('How many Elements?', end='')
n=int(input()) #Accept input into n
for i in range(n):
    print('Enter The Element:', end='')
    x.append(int(input())) #add the element to the array x using append
print('Original Array:',x)
print('Enter the Element to Search:',end='')
s=int(input()) #Accept element to be searched
try:
    pos=x.index(s)
    print('Found at Position:',pos)
except ValueError:
    print('Not found in the array')
