# Python time.time()
#The time() function returns the number of seconds passed since epoch.

import time
seconds = time.time()
print("Seconds since epoch =", seconds)


# Python time.ctime()
# The time.ctime() function takes seconds passed since epoch as an argument and returns a string representing local time

# import time
# seconds = 1631022017.7457445
# local_time = time.ctime(seconds)
# print("Local time:", local_time)

# Python time.sleep()
# The sleep() function suspends (delays) execution of the current thread for the given number of seconds.

# import time
# print("This is printed immediately.")
# time.sleep(2.4)
# print("This is printed after 2.4 seconds.")

# Python time.localtime()
# The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.

# import time
# result = time.localtime(1631022239)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# Python time.gmtime()
# The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.

# import time
# result = time.gmtime(1631022319)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

#Python time.mktime()
# The mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns the seconds passed since epoch in local time. Basically, it's the inverse function of localtime().

# import time
# t = (2021, 9, 7, 7, 24, 4, 4, 250, 0)
# local_time = time.mktime(t)
# print("Local time:", local_time)

#THIS PROGRAM IS COMMON FOR BOTH LOCAL TIME AND MKTIME

# import time
# seconds = 1631022319
# # returns struct_time
# t = time.localtime(seconds)
# print("T: ", t)
# # returns seconds from struct_time
# s = time.mktime(t)
# print("S:", seconds)

# Python time.asctime()
# The asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns a string representing it.

# import time
# t = (2021, 9, 7, 7, 30, 4, 4, 250, 0)
# result = time.asctime(t)
# print("Result:", result)

# Python time.strftime()
# The strftime() function takes struct_time (or tuple corresponding to it) as an argument and returns a string representing it based on the format code used.

# import time
# named_tuple = time.localtime() # get struct_time
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# print(time_string)

# Python time.strptime()
# The strptime() function parses a string representing time and returns struct_time.

# import time
# time_string = "7 september, 2021"
# result = time.strptime(time_string, "%d %B, %Y")
# print(result)