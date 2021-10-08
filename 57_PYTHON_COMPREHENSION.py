#IN CASE OF LIST

# listA = []
# for a in range(50):
#     if a % 5 == 0:
#         listA.append(a)
#         print(a)

# listA = [a for a in range(50) if a%5==0]
# print(listA)

#IN CASE OF SET
# setA = {"a", "a", "b", "c", "d", "d"}
# for alpha in setA:
#     print(alpha)
#
# alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}
# print(alpha)

#IN CASE OF DICTIONARY

# Normaldict = {
#   0 : "item0",
#   1 : "item1",
#   2 : "item2",
#   3 : "item3",
#   4 : "item4",
# }
# for y,x in Normaldict.items():
#     print(y,x)


# dict1 = {i:f"item {i}" for i in range(1000) if i%100==0}
# print(dict1)

#IN CASE OF REVERSE DICTIONARY
# dict2 = {value:key for key,value in dict1.items()}
# print(dict2)

#IN CASE OF GENERATORS
def gener(n):
    for i in range(n):
        if i%2==0:
            yield i

a = gener(20)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

# evens = (i for i in range(20) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())


