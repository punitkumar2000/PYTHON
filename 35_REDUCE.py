# import functools
# lis = [1, 3, 5, 6, 2, ]
#
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))
#
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

# python code to demonstrate working of reduce()
# using operator functions




import functools
import operator

lis = [1, 3, 5, 6, 2, ]

# print("The sum of the list elements is : ", end="")
# print(functools.reduce(operator.add, lis))

# print("The product of list elements is : ", end="")
# print(functools.reduce(operator.mul, lis))

# print("The concatenated product is : ", end="")
# print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))


#reduce() V/S accumulate()

# import itertools
# import functools
#
# lis = [1, 3, 4, 10, 4]
#
# print("The summation of list using accumulate is :", end="")
# print(list(itertools.accumulate(lis, lambda x, y: x+y)))
#
# # printing summation using reduce()
# print("The summation of list using reduce is :", end="")
# print(functools.reduce(lambda x, y: x+y, lis))

