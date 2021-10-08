#CURRENT WORKING DIRECTORY

# import os
# print(os.getcwd())

#CREATE A DIRECTORY

#By using mkdir
# import os
# os.mkdir("abcd")

#By using makedirs for making more than 1 directories
# import os
# os.makedirs("abc/xyz")

#Changing the current working directory
# import os
# print(os.getcwd())
# os.chdir("C:\Program Files\Git")
# print(os.getcwd())

#Changing cwd to parent

# import os
# os.chdir("C:\Program Files")
# print(os.getcwd())
#
# os.chdir("..")
# print(os.getcwd())

#Removing/Deleting a directory

# import os
# os.rmdir("C:\Program Files\Git")

# import os
# os.remove("C:\Program Files\Git")

#ListFiles and Sub-directories

# import os
# print(os.listdir("C:\Program Files\Git"))

# import os
# print(os.listdir())

#All the experiment we can able to do with the os module

# import os
# print(dir(os))

#To rename the directory

# import os
# os.rename("abc", "aaa")

#To join the path of directories

# import os
# print(os.path.join("D://", "GATE 2022"))
# print(os.getcwd())

#To check wheather the path is there or not

# import os
# print(os.path.exists("E:\GATE 2022"))

# import os
# print(os.path.isdir("C:\Program Files"))