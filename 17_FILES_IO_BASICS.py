#OPEN FILE

#To open a file we use in-built function open()

# f = open("17_abc.txt")
# print(f.read())
# f.close()

#If the file is located at a particular location

# f = open("C:\ Users\ punit\ Desktop\ abc.txt ", "r")
# print(f.read())
# f.close()

#Only read some parts of file

# f = open("17_abc.txt")
# print(f.read(28))
# f.close()

#print the file content in different parts

# f = open("17_abc.txt")
# content = f.read(12)
# print("1", content, end="")
#
# content = f.read(21)
# print("2", content, end="")
# f.close()

#can be used for printing 1 line and readlines can pring many lines

# f = open("17_abc.txt")
# print(f.readline())
# f.close()

#Through looping you can read the content of file line by line

# f = open("17_abc.txt")
# for x in f:
#     print(x, end="")
# f.close()

#USING WITH TO OPEN THE FILE
# with open("17_abc.txt") as f:
#     print(f.read(11))


#FILE APPEND

#To write into an existing file

# f = open("17_abc.txt", "a")
# x = f.write("Are you ready\n")
# f.close()

#To check how many character do we have

# f = open("17_abc.txt", "a")
# x = f.write("Are you ready")
# print(x)
# f.close()

#File write

#Opent the file and read the content
# f = open("17_abc.txt", "w")
# f.write("WORLD.\n")
# f.write("Are you ready.")
# f.close()

#Create a file called "17_xyz.txt"
# f = open("17_xyz.txt", "x")

#DELETE FILE
# import os       #It will delete the existing files
# os.remove("17_xyz.txt")

# import os       #Check if file exists or not
# if os.path.exists("abc.txt"):
#     os.remove("abc.txt")
# else:
#     print("the file doesn't exists")

# import os       #here we can only delete empty folder
# os.rmdir("abc")
