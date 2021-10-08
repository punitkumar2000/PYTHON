# ARGS AND KWARGS

# def adder(x, y, z):
#     print("sum:",x+y+z)
# adder(10, 20, 30)

#IF WE WANT TO ADD MORE PARAMETERS WE WILL GET AN ERROR
# def adder(x, y, z):
#     print("sum:",x+y+z)
# adder(10, 20, 30, 40)


# *ARGS

# def adder(*num):
#     sum = 0
#
#     for n in num:
#         sum = sum+n
#     print("sum:", sum)
#
# adder(3,4)
# adder(1,2,3,4)
# adder(10,20,30,40,50)

# def myfunc(*kids):
#     print("The youngest child is:" + kids[2])
#
# myfunc("Emele","Tobis","lene")

# **KWARGS

# def myfunc(**kids):
#     print("His last name is:"+kids["lname"])
#
# myfunc(fname="Tobias", lname="Reffes")

