chars = ['g','c','d','a','b','e','f']
chars.sort()#Sorts thes list
chars.reverse()#reverse the list
# or
# print(chars[::-1])
print(chars)


# To create a quick list
# print(list(range(1,101)))# starting point and ending point :)

# Joining lists 

symbol = ', '

sentence = symbol.join(['Ankit', 'Anurag','Soham', 'Saptarshi'])
print(sentence)

#List Unpacking

a,b,c, *other,x = [1,2,3,4,5,6,7,8,9]
# variables , other is remainig list and x is the last value of the list 
print(a)
print(b)
print(c)
print(other)