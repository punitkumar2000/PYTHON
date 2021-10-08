#STRING SLICING

# mystr1 = "punit mann"
# mystr2 = "PUNITMANN"

# print(mystr1[4])     #For single char slice
# print(mystr1[0:4])   #For multiple char slice
# print(mystr1[0:10:2])#For skipping any char with multiple char
# print(mystr1[:])     #Default for string slicing
#
# # NEGATIVE SLICING
#
# print(mystr1[-10:-1])
# print(mystr1[::-1])  #For reverse the whole string
# print(mystr1[::-2])

#SOME TYPES OF FUNCTIONS

# print(type(mystr1))  #Check which string is there
# print(len(mystr1))   #Check length of a string
#
# print(mystr1.isalnum()) #Check the string is alpha-numneric or not
# print(mystr2.isalnum())
#
# print(mystr1.isalpha()) #Check the string is alphabet or not
# print(mystr2.isalpha())
#
# print(mystr1.endswith("mann"))#Check the string ends with given string or not
# print(mystr1.count("n")) #count the no of words or char
# print(mystr1.capitalize()) #Capitalize the initial letter of the string
# print(mystr1.find("mann")) #Check string present at what index value
#
# print(mystr2.lower())   #To convert the whole string into lower case
# print(mystr2.casefold())
# print(mystr1.upper())   #To convert the whole string in the upper case
#
# print(mystr1.replace("mann","kumar"))
# print(mystr1.swapcase()) #To convert the lower case of string to the upper case or vice versa
# print(mystr1.title())   #Capitalize the title