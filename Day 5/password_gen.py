import random

letters = 'q w e r t y u i o p l k j h g f d s a z x c v b n m Q W E R T Y U I O P L K J H G F D S A Z X C V B N M '.split()
nums = '1 2 3 4 5 6 7 8 9 0'.split( )
sym = '! @ # $ % ^ & * ( ) / ? { }'.split( )


num_let = int(input("No of Letters: "))
num_num = int(input('Number of Numbers: '))
num_sym = int(input("Number of Symbols: "))

password_list = []

for char in range(1, num_let + 1):
    password_list += random.choice(letters)

for char in range(1, num_num + 1):
    password_list += random.choice(nums)

for char in range(1, num_sym + 1):
    password_list += random.choice(sym)    

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(password)