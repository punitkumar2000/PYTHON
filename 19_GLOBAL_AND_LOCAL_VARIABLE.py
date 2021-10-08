#GLOBAL AND LOCAL VARIABLE

# x = 10                     #GLOBAL VARIABLE(OUTSIDE THE FUNCTION)
# def abc():
#     x = 20                 #LOCAL VARIABLE(INSIDE THE FUNCTION)
#     print("x:", x)
# abc()
# print("x:", x)


#CREATE A VARIABLE OUTSIDE THE FUNCTOIN AND USE IT INSIDE THE FUNCTION
# x = 20
# def abc():
#     print("x:", x)
# abc()

#THE GLOBAL KEYWORD

# def abc():
#     global x
#     x = 20
# abc()
# print("x:", x)

#TO UPDATE THE GLOBAL VARIABLE INSIDE A FUNCTION WE NEED TI USE THE GLOBAL KEYWORD

# x = 20
# def abc():
#     global x
#     x = x+20
#     print("x:", x)
# abc()

#USING NESTED FUNCTION

# def abc():
#     x = 10
#     def xyz():
#         global x
#         x = 20
#     print("before calling xyz:", x)
#     xyz()
#     print("after calling xyz:", x)
# abc()
# print(x)