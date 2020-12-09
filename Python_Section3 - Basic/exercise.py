name = input('Enter your name \n')
password = input('Enter a password \n')

password_length = len(password)

password = password_length * '*'

# print(f'{name}, your {password} length is {password_length}')

print(name + ' your ' + str(password) + ' length is ' + str(password_length))
