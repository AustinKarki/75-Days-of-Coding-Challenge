# -*- coding: utf-8 -*-
"""loop.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tYey1rHpQTmpy6pxGTu8i0YtIiVCaYPa
"""

# for loop
# while loop

# range(5) 0,1,2,3,4   for(i=0; i<5 i++)
# range(1,5) 1,2,3,4  for(i = 1; i<5 i++)
# range(0,10,2) 0,2,4,6,8 for(i = 0; i<10; i = i+2)

for i in range(5):
    print("hello world")

for i in range(1,5):
    print(i,"Hello World")

for i in range(0,10,2):
    print(i,"Hello World")

x = input("Enter x = ")
for i in range(5):
    print(x)

n = int(input("Enter n = "))
for i in range(1,11):
    print(i*n)

n = int(input("Enter n = "))
for i in range(1,11):
    print(n,"*",i,"=",i*n)

for i in range(2):
    x = input("Enter x =")

s = 0
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
#     print(s,"+",x,"=",s+x)
    s = s+x

print(s)

s = str()
n = int(input("Enter n = "))
for i in range(n):
    x = input("Enter x = ")
#     print(s,"+",x,"=",s+x)
    s = s+x+"\n"

print(s)

s = str()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    phone = int(input("Enter phone = "))
#     print(s,"+",x,"=",s+x)
    s = s+name+" " +str(phone)+"\n"

    print(s)

# range(10,0,-1)
for i in range(10,-1,-1):
    print(i)

# 5 = 1*2*3*4*5
fac = 1
n = int(input("Enter n = "))
for i in range(1,n+1):
    fac = fac*i

print(fac)

# 5 = 1*2*3*4*5

n = int(input("Enter n = "))
fac = n
for i in range(n-1,1,-1):
    fac = fac*i

print(fac)

# control statements
# while loop

# break
# continue
# pass

# break
for i in range(10):
    if i == 5:
        break
    else:
        print(i)

# continue
for i in range(10):
    if i == 5:
        continue

    print(i)

a = "Hello World"
for i in a:
    if i == " ":
        continue

    print(i,end = "")

a = "Hello"
for i in a:
    print(i)

a = "Hello World"
for i in a:
    print("Python")

a = "Python"
l = len(a)
for i in range(l):
    print(a[i],end = "")

a = "Python"
a[2]

a = 10
b = 2
if a>b:
    pass
elif b>a:
    pass

for i in range(5):
    pass

# WAP to develop a billing system
# name
# price
# quantity
# total

# grand_total

s = str()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    phone = int(input("Enter phone = "))
#     print(s,"+",x,"=",s+x)
    s = s+name+" " +str(phone)+"\n"

    print(s)

# While loop