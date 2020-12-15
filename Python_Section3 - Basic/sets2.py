# Difference method in sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) 

print(set3) # Returns banana and cherry because banana and cherry is not present in the set2

# Remove items from a set
new_set = {1,2,3,4,5}
new_set.remove(5) # Specify the element which you want to remove
print(new_set) # 5 is removed from the set

# Note - We can't aceess a tuple by index as a set is unordered and unindexed
# new_set = {1,2,3,4,5}
# print(new_set[1]) # Returns TypeError

# difference_update

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9}
my_set.difference_update(your_set) # Remove all elements of another set from this set.
print (my_set)

# Join sets
print(my_set.union(your_set))