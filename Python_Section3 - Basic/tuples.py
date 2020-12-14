# Tuple items are ordered, unchangeable, and allow duplicate values.
my_tuple = (1,2,3,4,5)
print(my_tuple[1])

#Check for items in tuple
my_tuple = (1,2,3,4,5,2)
print(4 in my_tuple)

# Python has two built-in methods that you can use on tuples.

# 1. count() --> Returns the number of times a specified value occurs in a tuple
my_tuple2 = (1,2,3,4,5,2)
print(my_tuple.count(2))

# 2. index() --> Searches the tuple for a specified value and returns the position of where it was found
my_tuple3 = (1,2,3,4,5,2)
print(my_tuple.index(3))#Returns value error if the value is not present

# Updates tuple
# 1. convert the tuple to  list
# 2. Make the desire updates
# 3. Change the list back to tuple

update_tuple = ('Ankit', 'Soham', 'Saptarshi')
list1 = list(update_tuple)
list1[1] = 'Thomas'
updated_tuple = tuple(list1)
print(updated_tuple)

# Remove items from tuple
# 1. convert the tuple to  list
# 2. Make the desire removal
# 3. Change the list back to tuple

delete_tuple = ('Ankit', 'Soham', 'Saptarshi')
list2 = list(delete_tuple)
list2.remove('Saptarshi')
deleted_tuple = tuple(list2)
print(deleted_tuple)


# done!