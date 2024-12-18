# -*- coding: utf-8 -*-
"""tuple.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mUDokmqtjKeDifWTpMTh2g0L7GaSgtlw
"""

# # tuple
# -Indexed
# -Ordered
# -Multiple and duplicate data
# -IMutable

a = tuple()
a = (1,2,3,4,5,6,)
print(a)
print(type(a))

a = (1,)
b = ("Apple",)
print(type(a))
print(type(b))

a = ("Apple","Ball","Cat","Dog")
print(a[0])
print(a[0:4])
print(a[0:4:2])

a = ("Apple","Ball","Cat","Dog")
b = ("Fish",)
c = a+b
print(c)

a = ("Apple","Ball","Cat","Dog")
a*2

# no append() insert() extend()
# no update
# no del remove() pop()

t = tuple()
n = int(input("Enter n = "))
for i in range(n):
    x = input("Enter x = ")
    t = t + (x,)

print(t)

def cal():
    a = 10
    v = 12
    return a,v

cal()

a = 10,11,12
a

a = ('Apple', 'Ball', 'Cat', 'Dog', 'Apple', 'Ball', 'Cat', 'Dog')
b = list(a)
del b[0]
a = tuple(b)
a

# tuple inside tuple
a = (('Ram',34,'Kathmandu'),
    ('Shyam',23,'Patan'),
    ('Hari',54,'Bhaktapur'))
a

# tuple inside tuple
a = (('Ram',34,'Kathmandu'),
    ('Shyam',23,'Patan'),
    ('Hari',54,'Bhaktapur'))
b = (('Nabin',34,'Chitwan'),)
print(a+b)

a = (('Ram',34,'Kathmandu'),
    ('Shyam',23,'Patan'),
    ('Hari',54,'Bhaktapur'))
b = list(a)
b

del b[0]
b

b.append(('Nabin',67,"Bara"))
b

b[0]

# WAP to convert tuple inside tuple to list inside list and vice versa
# WAP to perform CRUD list inside tuple
# (['Shyam', 23, 'Patan'], ['Hari', 54, 'Bhaktapur'], ['Nabin', 67, 'Bara'])