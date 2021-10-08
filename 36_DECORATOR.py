def outerfunc(func):
    def innerfunc():
        print("Before function execution")
        func()
        print("After function execution")
    return innerfunc()

@outerfunc
def function_to_be_used():
    print("This is inside the function")

# function_to_be_used = outerfunc(function_to_be_used)
# function_to_be_used