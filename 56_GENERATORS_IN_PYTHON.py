# l1=[1,2,3,4,5]
# l2=iter(l1)
#
# print (l2)
#
# #Iterating through iterable(l1) using for loop.
# for i in l1:
#     print (i,end=" ")
#
# print (" ")
#
# #Iterating through iterator(l2) using for loop.
# for i in l2:
#     print (i,end=" ")

#GENERATORS IN PYTHON

# def getNum (x):
#     for i in range(x):
#         yield i
#
# seq = getNum (2)
#
# print(seq.__next__())
# print(seq.__next__())
# print(seq.__next__())


def gen(n):
    for i in range(n):
        yield i
#....................................................................................
g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

#....OR....(ABOVE WILL SHOW STOPITERATION ERROR BUT DOWNWARD WILL NOT)

# for i in g:
#     print(i)
#..........................................................................................

# h = "ram"   #only use string not int
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
#OR
# for c in h:
#     print(c)
