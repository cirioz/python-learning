import random


#dobijam koliko slova, koliko simbola, koliko brojeva
# imam listu svih
# random iz liste izvlaci i cuva u varijablu


letters = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input(f"How man letters would you like in your password?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# for n in range(random.randint(0,6), len(letters)):
#     letters[n] = int(letters[n])

    
# for n in range(random.randint(0,6), len(numbers)):
#     numbers[n] = int(numbers[n])
    
    
    
# for n in range(random.randint(0,6), len(symbols)):
#     symbols[n] = int(symbols[n])
    
    
    
# password = ''

#nr_letters = 4
# for char in range(1, nr_letters+1):
#     random_char = random.choice(letters)
#     password += random.choice(letters)
    

# for char in range(1, nr_symbols+1):
#     random_char = random.choice(symbols)
#     password += random.choice(symbols)
    

# for char in range(1, nr_numbers+1):
#     random_char = random.choice(numbers)
#     password += random.choice(numbers)
    
# print(password)



#! Hard Level

password_list = []

for char in range(1, nr_letters+1):
    random_char = random.choice(letters)
    password_list += random.choice(letters)
    

for char in range(1, nr_symbols+1):
    random_char = random.choice(symbols)
    password_list += random.choice(symbols)
    

for char in range(1, nr_numbers+1):
    random_char = random.choice(numbers)
    password_list += random.choice(numbers)
    
print(password_list)

random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char
    
print(password)