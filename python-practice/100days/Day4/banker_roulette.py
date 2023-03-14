
#! Banker Roulet

import random

people_at_dinner = ["Marko", "Stojan", "Leposav", "Savoljub", "Stevomir"]

who_pays = random.randint(0, 4)

print(f"{people_at_dinner[who_pays]} will pay for the bill")


#! Angelas solution


names_string = input("Give me everybody's names, seperated by a comma.")
names = names_string.split(", ")

print(names)

num_items = len(names)
print(num_items)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = random.choice(names)


print(person_who_will_pay + " is going to buy the meal today.")

