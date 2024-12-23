# -*- coding: utf-8 -*-
"""list.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ay-nGD8lqJ2wRO4pmFnfcrq_geAKjtbE
"""

# Python collection
# List
# tuple
# dictionary
# set

# # list
# -Indexed
# -Ordered
# -Multiple and duplicate data
# -Mutable

# list
a = ["Apple","Ball","Cat","Dog","Fish"]
l = len(a)
print(l)
print(a)
print(type(a))

a = ["Apple","Ball","Cat","Dog","Fish"]
print(a[1])
print(a[0:4])
print(a[0:4:2])

a = ["Apple","Ball","Cat","Dog","Fish"]
b = [1,2,3,4,5]
c = b+a
print(c)

a = ["Apple","Ball","Cat","Dog","Fish"]
print(a*2)

a = [1, 2, 3, 4, 5, 'Apple', 'Ball', 'Cat', 'Dog', 'Fish',1,2]
l = len(a)
l

a = ["Apple","Ball","Cat","Dog","Fish"]
a[0] = "Ant"
a

l = list()
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
    l.append(x)

print(l)

# max min sum

a = [324, 234, 34, 32, 34]
print(max(a))
print(min(a))
print(sum(a))

a.sort()
print(a)

a = ["apple","Xray","zbera","Ball","Fish"]
a.sort()
print(a)

a = ["apple","Xray","zbera","Ball","Fish"]
for i in a:
    print(i)

a = ["apple","Xray","zbera","Ball","Fish"]
if "apple" in a:
    print("Yes")
    print(a.count("apple"))

# append() insert() extend()

a =[]
a.append("Apple")
print(a)

a = ["apple","Xray","zbera","Ball","Fish"]
a.insert(1,"Ant")
print(a)

a = ["apple","Xray","zbera","Ball","Fish"]
b = [1,2,3,4,5]
a.extend(b)
print(a)

# remove() del pop()
a = ['apple', 'Ant', 'Xray', 'zbera', 'Ball', 'Fish']
a.remove('apple')
a

a = ['apple', 'Ant', 'Xray', 'zbera', 'Ball', 'Fish']
del a[0]
a

a = ['apple', 'Ant', 'Xray', 'zbera', 'Ball', 'Fish']
del a[0:3]
a

a = ['apple', 'Ant', 'Xray', 'zebra', 'Ball', 'Fish']
a.index("apple")

a = ['apple','apple', 'Ant', 'Xray', 'zbera','apple','Ball', 'Fish']
for i in a:
    if i == "apple":
        a.remove("apple")
a

a = ['apple', 'Ant', 'Xray', 'zbera','apple','Ball', 'Fish']
l = a.count('apple')

for i in range(l):
    if a[i] == "apple":
        a.remove(a[i])
a

b = []
a = ['apple','apple', 'Ant', 'Xray', 'zbera','apple','Ball', 'Fish']
for i in a:
    if i != "apple":
        b.append(i)
print(b)

# WAP to detect index of same value
a = ['apple','apple', 'Ant', 'Xray', 'zbera','apple','Ball', 'Fish']
for i in range(len(a)):
    if a[i] == 'apple':
        print(i)

# list inside list
a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print(len(a))

print(a[2])

a = [['Ram',34,'Kathmandu'],
    ['Shyam',23,'Patan'],
    ['Hari',54,'Bhaktapur']]
a

a[0][2]

name = input("Enter name = ")
for i in a:
    if name in i:
        print(i)

# a = [['Ram', 34, 'Kathmandu'],
#      ['Shyam', 23, 'Patan'],
#      ['Hari', 54, 'Bhaktapur']]

info =[]
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    data = [name,age,add]
    info.append(data)

print(info)

a = [['Ram', 34, 'Kathmandu'], ['Shyam', 23, 'Patan'], ['Hari', 54, 'Bhaktapur']]
del a[0]
a

a = [['Ram', 34, 'Kathmandu'], ['Shyam', 23, 'Patan'], ['Hari', 54, 'Bhaktapur']]
a[0][0] = "Ram Prasad"
a

a =[['Shyam', 23, 'Patan'], ['Hari', 54, 'Bhaktapur']]
a.append(['Ram',34,'Baluwatar'])
a

a = [['Ram', 34, 'Kathmandu'], ['Shyam', 23, 'Patan'], ['Hari', 54, 'Bhaktapur']]

name = input("Enter name = ")
for i in a:
    if name in i:
        a.remove(i)
a

# WAP to create a matrix by taking row and column