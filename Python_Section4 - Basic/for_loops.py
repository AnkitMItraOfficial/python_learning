# Python For Loops
# A for loop is used for iterating over a sequence (examples- list, a tuple, a dictionary, a set, or a string).

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Looping through a string

for item in 'Hello World':
    print(item)
    
# Nested looping through strings

# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

for words in 'Goodbye World':
    for symbol in '!':
        print(words, symbol)    


# Looping through a list

list1 = [1,2,3,4,5]

for nums in list1:
    print(nums)
    

# Nested looping through list 

fruits = ['apple','banana','pear']
specs = ['is great','is tasty','is healthy']

for fruit in fruits:
    for spec in specs:
        print(fruit, specs)
    
    
# Some fun
list2 = ['Ankit', 'Soham','Saptarshi', 'Sayan']

for items in list2:
    if items == 'Saptarshi':
        continue
    print(items)
    
#tricky Counter
my_list = [1,2,3,4,5,6,7,8,9,10] # Task add all the numbers in the list

counter = 0
for nums in my_list:
    counter = counter + nums
    
print(counter)

# range
# We will see the usage of range function mostly in for loops

for _ in range(0, 11,2):#START, STOP, STEPOVER(DEFAULT - 1)
    print(_) # we use underscore (_) when we don't want to decrale any variable or the var is not that important

# Reverse printing

for i in range(10, 0, -1): # We can reverse the way like how the numbers are printed
    print(i)

# Enumerate

for i,chars in enumerate(list(range(100))):
    if chars == 89:
        print(f'the index of 89 is {i}')
        





