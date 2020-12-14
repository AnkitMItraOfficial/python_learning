# Introduction 
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.


# We create a set by using curly brackets
my_set = {1,2,3,4,5,5}
print(my_set)# Removes any dublicate value and prints the set
print(len(my_set)) # Returns the length of the unique values and does not counts the duplicate values

# Casting of a set to list
my_set = {1,2,3,4,5,5}
print(list(my_set)) # But does not prints the duplicate values because the duplicate value was never added to the set

# Alternative
my_set = {1,2,3,4,5,5}
new_list = list(my_set)
print(new_list)

# Copying a set
my_set = {1,2,3,4,5,5}
new_set = my_set.copy() # The copy method copies the entire set but duplicates are again not allowed, how evil!
print(new_set) 