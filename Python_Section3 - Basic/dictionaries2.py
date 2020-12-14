
dictionary = {
    'a' : 'Hello World',
    'b' : [1,2,3],
    'c' : True
}

# Check wether keys exists in the dictionary
# Return True if key exists and False if key not exists

# print('a' in dictionary.keys())# Returns True 
# print('x' in dictionary.keys())# Returns False

# Check wether values exists in the dictionary
# Return True if value exists and False if value not exists

# print(True in dictionary.values())# Returns True 
# print('x' in dictionary.values())# Returns False

#Clearing dictionaries

dictionary = {
    'a' : 'Hello World',
    'b' : [1,2,3],
    'c' : True
}

dictionary.clear() # Clears the dictionary not deletes it 
print(dictionary)

# Updates the Clear dictionary
print(dictionary.update(age=55))#Updates the dictionary
print(dictionary.update(age=15))# we can also update the value of the key
print(dictionary)
