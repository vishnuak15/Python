# 
# Example file for variables
f=0

# Declare a variable and initialize it
# f="abc"
# print(f)


# re-declaring the variable works
# print("This is a string " +str(123))


# ERROR: variables of different types cannot be combined



# Global vs. local variables in functions
def someFunction():
    global f #global variable inside a function
    f="def"
    print(f)

someFunction()#local variable
print(f)#global variable

print(f)