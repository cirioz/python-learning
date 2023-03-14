
#!  AUTOMATIC PIZZA ORDER PROGRAM
# Based on the user's order, work out their final bill
# Small Pizza: 15$
# Medium Pizza: 20$
# Large Pizza: 25$
# Pepperoni for Small Pizza: +2$
# Pepperoni for Medium or Large Pizza: +3$ 
# Extra cheese for any size pizza: +1$

#? Small Pizza or Medium or Large, if small do you want pepperoni, do you want extra cheese, your order is
#? if medium or large, do you want extra chese

bill = 0
pizza_sizes = ["Small", "Medium", "Large"]
pepperoni = ["Yes","No"]
extra_cheese = ["Yes", "No"]


pizza_order = input("What Pizza Size Would you like? Small, Medium or Large")


if pizza_order == pizza_sizes[0]:
    bill = 15
    pepperoni_order = input("Would you like a pepperoni?")
    if pepperoni_order == pepperoni[0]:
        bill += 2
    else:
        bill = bill
    cheese_order = input("Would you like extra cheese?")
    if cheese_order == extra_cheese[0]:
        bill += 1
        print(f"That will be ${bill}")
    else:
        print(f"That will be ${bill}")  
        
elif pizza_order == pizza_sizes[1]:
    bill = 20
    pepperoni_order = input("Would you like a pepperoni?")
    if pepperoni_order == pepperoni[0]:
       bill += 3
    else:
       bill = bill
    cheese_order = input("Would you like extra cheese?")
    if cheese_order == extra_cheese[0]:
       bill += 1
       print(f"That will be ${bill}")
    else:
       print(f"That will be ${bill}")   
              
else:
    bill = 25
    pepperoni_order = input("Would you like a pepperoni?")
    if pepperoni_order == pepperoni[0]:
       bill += 3
    else:
       bill = bill
    cheese_order = input("Would you like extra cheese?")
    if cheese_order == extra_cheese[0]:
       bill += 1
       print(f"That will be ${bill}")
    else:
       print(f"That will be ${bill}")   
        
        
        
