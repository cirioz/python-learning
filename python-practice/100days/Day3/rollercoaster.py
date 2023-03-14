print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))
answer = ["Y", "N"]
bill = 0



if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif (age < 55 or age > 45) and (age > 45 and age < 55):
        print("You can ride for free")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        print("The photo cost is 3$")
        bill = bill + 3
        print(f"Your total cost is {bill}$")
    else:
        print(f"Your total cost will be{bill}$")
        

else:
    print("You can't ride the rollercoaster. Sorry, you have to grow taller before you can ride.")
    
    
if height == 120:
    print("You are 120cm tall!")
