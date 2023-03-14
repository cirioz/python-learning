import random

number = random.randint(1,100)

if number%2 == 0:
    number = "Heads"
else:
    number = "Tails"
    
print(number)


#! Tails or Heads

random_side = random.randint(0,1)

if random_side == 0:
    random_side = "Heads"
else:
    random_side = "Tails"
    
print(random_side)