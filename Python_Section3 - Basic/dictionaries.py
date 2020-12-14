# A dictionary is a data structure like lists, dictionaries can store multiple types of data at once
# Dictionaries has a key and a value, they are undordered, and we cannot slice dictionary

dictionary = {
    'a' : 'Hello World',
    'b' : [1,2,3],
    'c' : True
}

# # print(dictionary)# prints the whole dictionary 
# print(dictionary['a']) #Returns the value of key a
# print(dictionary['b']) #Returns the value of key b
# print(dictionary['c']) #Returns the value of key c
# print(dictionary['x']) #Returns KeyError

# get method in dictionaries

dictionary = {
    'a' : 'Hello World',
    'b' : [1,2,3],
    'c' : True
}

# print(dictionary.get('d'))# Will show none because key does not exists
print(dictionary.get('d',22)) # We can give a default value of the key if the key does not exist
print(dictionary.get('a')) # Expected output Hello World, because the key does exist


# Another way to create dictionary but not so popular
# Using dict function

dictionary2 = dict(name='Ankit', age=9, is_noob= True)
print(dictionary2)