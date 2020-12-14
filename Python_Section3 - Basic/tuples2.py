# Tuples packing and unpacking

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")
print(fruits)# Prints the whole tuple

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow, red) = fruits
# |       |      |
#apple  banana cherry

print(green)#apple
print(yellow)#banana
print(red)#cherry


# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to
# collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
# |       |       |
#apple  banana rest of tuple

print(green)
print(yellow)
print(red)

# Join Two Tuples
# To join two or more tuples you can use the + operator:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3) # Returns the joint version of the tuple


# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

tuple1 = ("apple", "banana", "cherry")
my_tuple = tuple1 * 2
print(my_tuple)

# Woo tuples are finally over :)




