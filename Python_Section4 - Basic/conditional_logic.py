# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.
a = 10
b = 8

if b > a:
    print('b is greater than a')

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".    
elif a == b:
    print('a is equal to b')

else:
    print('I am sure a is greater than b')
    
print('Program ended and I am outside the if-else block, I will run always no matter what the conditions are :)')
    
    
# More Example

# is_18 = True
# is_licensce = True

# if is_18 and is_licensce: # this block of code executes if is_18 is true
#     print('You can drive and you have your licenset too') # Wondering the space before the print statement it is because of indentation
    
# else: # if none of the conditions are true then run this at last
#     print('Do you want to go behind the bars?')

# print('I am outside of the if-else block, because I have no indentation and I will run always no matter what the above conditions are')

# Indentation in python

# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
# Other programming languages often use curly-brackets for this purpose

# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error

# Ternatory operator

is_friend = True
can_message = 'you can message because we are friends' if is_friend else 'not allowed to message'
print(can_message)