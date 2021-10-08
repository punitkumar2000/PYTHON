#VARIABLES

v1="hello world"
v2=" punit "
v3=10
v4=20.3
v5="10"
v6="20"

print(v1+v2)    #STRING CONCATINATION
print(v5+v6)

#IMPLICIT CONVERSION
print(v3+v4)    #Automatically convert one data tyoe to another data type

#EXPLICIT CONVERSION
print(int(v5)+int(v6))  #FIRST IT WILL TYPE CAST INTO INTEGER
print(str(v3)+str(v4))
print(float(v3)+(v4))

#HOW TO PRINT ANY THING MULTIPLE TIMES
print(5*"punit\t")

#TAKING INPUT FROM THE INPUT
print("enter your name:")
inp_name = input()
print("your name is:", inp_name)