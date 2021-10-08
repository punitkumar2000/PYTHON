#DICTIONARY

mydict = {"name":"punit", "branch":"cse", "sem":7, "address":{"state":"delhi","distt":"narela"}}

# print(type(mydict))
# print(mydict["name"])
# print(mydict["address"]["state"])

#TO ADD MORE ELEMENTS
# mydict["roll_no"] = 100
# print(mydict)

#TO DELETE THE ELEMENTS
# del mydict["sem"]
# print(mydict)

#TO COPY THE ELEMENTS
# d = mydict
# del d["name"]
# print(mydict)

# d = mydict.copy()     #copy the values of 1 dict into other dict
# del d["name"]
# print(mydict)
# print(d)

# print(mydict.get("name")) #print the particular value
# mydict.update({"sem":8})  #update the value
# print(mydict)

# mydict.pop("name")    #will pop/delete the particular element form the dictionary
# print(mydict)

# print(mydict.keys())  #print all the keys
# print(mydict.values())  #print all the values of the dictionary