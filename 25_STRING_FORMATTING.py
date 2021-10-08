#STRING FORMATTING/ F-STRING

# STRING FORMATTING
#To use 1 value
# price = 49
# txt = "The Price is {} Dollars"
# print(txt.format(price))

#To use more than 2 values
# quantity = 3
# item_no = 200
# price = 1000
# myorder = "I Want {} Pieces of Item no {} for {:.2f} Dollars."
# print(myorder.format(quantity, item_no, price))

#Index Number
# quantity = 3
# item_no = 200
# price = 1000
# myorder = "I Want {0} Pieces of Item no {1} for {2:.2f} Dollars."
# print(myorder.format(quantity, item_no, price))

#Name Indexes
# myorder = "I Have a {carname}, It is a {model}"
# print(myorder.format(carname = "FORD", model = "MUSTANG"))

#F-STRING

# me = "Punit"
# you = "Ram"
# a = "This is %s & %s"%(me, you)
# print(a)

# me = "Punit"
# you = "Ram"
# a = f"This is {you} & {me}"
# print(a)

# import math
# a = f"The value of cos30 is {math.cos(60)}"
# b = f"The value of pi is {math.pi}"
# print(a)
# print(b)