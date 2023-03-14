# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hi")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
    
# greet()

#Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Are you ok {name}?")

# greet_with_name("Bela")    


#Function with more than 1 input


# def greet_with(day, location, hour):
#     print(f"It is {hour}, you are at {location}")
#     print(f"{location} bas je lepo")
#     print(f"What why when {day}")
# greet_with("Sreda", "Novi Sad")
# greet_with(location = "Sto ja imam s tim", day = "Sreda", hour = "20h")


#!!! Second pass

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code

# def greet_2():
#     print("Hello there!")
#     print("Oh what a nice day.")
#     print("That is nice of you.")

# greet_2()

#! Inputs



def greet_with_name(name):
    print(f"Hello there {name}!")
    print("Oh what a nice day.")
    print("That is nice of you.")

greet_with_name("Suzuki")


#! Arbitrary positional arguments (*args)
# a simple function that takes only 3 arguments:
def percentage(sub1, sub2, sub3):
    avg = (sub1 + sub2 + sub3) / 3
    print("Average", avg)
    
percentage(56, 61, 73)

# a function that could calculate the average of all subjects no matther how many there are

def percentage(*args):
    sum = 0
    for i in args:
        # get total
        sum = sum + i
    # calculate average
    avg = sum / len(args)
    print("Average =", avg)
    
percentage(56, 61, 73)

# for loop practice 
lista = [22,65,32,55,2,2,44]
zbir = 0
for i in lista:
    zbir = zbir + i
avg2 = zbir / len(lista)
print(avg2)
print(zbir)


#! Functions with more than one input

name = input("What is your name?")
location = input("Where are you from?")

def greet_with(name, location):
    print(f"{name} is from {location}")
greet_with(name, location)

greet_with("Nowhere", "Jack Bauer")

greet_with(name=input("So what is your name?"), location=input("What is your location?"))

