# #lists

# list1 = [1,3,4,5,6]

# #Adding
# list1.append(100) # list.append(object), Append object to the end of the list.
# new_list = list1

# print(list1)
# print(new_list)


# #Inserting 
# list2 = [1,2,3,4,6]
#         #0 1 2 3 4 --> Index
# list2.insert(4,5) # list.insert(index, object), Insert object before index.
# print(list2)

# # Removing
# list3 = [1,2,3,4,6]

# list3.remove(6)#Remove first occurrence of value.Raises ValueError if the value is not present.
# print(list3)
# list3.remove(4)
# print(list3)

# # Poping
# list4 = [1,2,3,4,6]

# list4.pop()#Remove the last value by default
# list4.pop(2)# Removes the item at index 2
# print(list4)

# #Extending
# list5 = [1,2,3,4,6]
# list5.extend([8,9,10])
# print(list5)

# Index value
# list6= ['a','b','c','d','e']
# print(list6.index('e'))# FInds the index of the given value

# In keyword
list7 = [1,2,3,4,6]
print(1 in list7)# Returns True 
print(10 in list7)# Return False

#Also applicable to strings
Word = 'I am a cool boy'
print('I am' in Word) # True

# Count 
list3 = [1,2,3,4,2,6]
print(list3.count(2))# Shows 2 because 2 is two times in the list

