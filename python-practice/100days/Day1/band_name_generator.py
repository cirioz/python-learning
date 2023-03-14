
# ! BAND NAME GENERATOR

import random



cities = ["Novi Sad", "Beograd", "Zrenjanin", "Subotica", "Nis", "Kragujevac", "Kraljevo", "Valjevo", "Sremska Mitrovica"]

city_name = input("What is your city name?") # Defining variable "city_name" using user input
print(city_name) # Prints to console variable "city_name" 
pet_name = input("What is your first pets name?") # Defining variable "pet_name", with user input
print(pet_name) # Prints to console variable "pet_name"
band_name = city_name + " " + pet_name
print(f"Your bands name is {city_name} {pet_name}")
print(band_name)




# print(random_value)


def band_name_gen():
    random_value = random.randint(0,9)
    band = cities[random_value] + cities[random_value]
    print(band)

band_name_gen()