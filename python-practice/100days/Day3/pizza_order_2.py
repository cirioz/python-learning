
#!  AUTOMATIC PIZZA ORDER PROGRAM
# Based on the user's order, work out their final bill
# Small Pizza: 15$
# Medium Pizza: 20$
# Large Pizza: 25$
# Pepperoni for Small Pizza: +2$
# Pepperoni for Medium or Large Pizza: +3$ 
# Extra cheese for any size pizza: +1$
size = ["S", "M", "L"]
pepperoni = ["Yes", "No"]
cheese = ["Yes", "No"]
bill = 0

while True:
    try:
        order_size = input("What pizza size would you like?(S,M or L) ")

        
        
        if order_size == size[0]:
            bill += 15
        elif order_size == size[1]:
            bill += 20
        elif order_size == size[2]:
            bill += 25
        elif order_size not in size:
            print("We only can agree on the provided size")
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid size")
        

while True:
    try:
        add_cheese = input("Would you like to add some cheese? (Yes or No)")
        
    
        
        
        if add_cheese == cheese[0]:
            bill += 1
        elif add_cheese == cheese[1]:
            bill = bill
        elif add_cheese not in cheese:
            print("We cant take this input")
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid value")  
                
while True:
    try:
        add_pepperoni = input("Would you like pepperoni. (Yes or No)") 
        
            
        
        if add_pepperoni == pepperoni[0] and order_size == size[0]:
            bill += 2
            print(f"Your bill is ${bill}")
        elif add_pepperoni == pepperoni[0] and (order_size == size[1] or order_size == size[2]):
            bill += 3
            print(f"Your bill is ${bill}")
        elif add_pepperoni == pepperoni[1]:
            bill = bill
            print(f"Your bill is ${bill}")
        elif add_pepperoni not in pepperoni:
            print("We cant take this value")
            raise ValueError
        break
    
        
    except ValueError:
        print("Please enter a valid value")
        
print(f"Your bill is ${bill}")        