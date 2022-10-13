import random
symbols=[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
         '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}']

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to Password Generator!")
n_letters=int(input("How many letters you would like in your password?"))
n_symbols=int(input("How many symbols you would like in your password?"))
n_numbers=int(input("How many numbers you would like in your password?"))

password_list=[]

for i in range(0,n_letters + 1):
    password_list.append(random.choice(letters))
for j in range(0,n_symbols + 1):
    password_list.append(random.choice(symbols))
for k in range(0,n_numbers + 1):
    password_list.append(random.choice(numbers))

password=""
for char in password_list:
    password+=char 
print(f'Here is your password :{password}')
