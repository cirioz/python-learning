# 3 hot flavors
# coins operate
# automatic cup dispenser
# counting cup selling

# Makes 3 hot flavours
# 1. Espresso (50ml Water, 18g Coffee), 2. Latte (24g Coffee, 150ml Milk) 3. Cappuccino (250ml Water, 24g Coffee, 100ml Milk)
# 300ml Water in tank
# 200ml Milk in tank
# 100g of Coffee

# Coin Operated
# Penny (1 cent, 0,01$), Dime (10 cents, 0,1$), Nickel (5 cents, 0,05$), Quarter (25 cents, 0,25$)

# Program requirements
# 1. Print report of all the resuources that the machine has.
# 2. Check if there are sufficient resources?
# 3. When requesting coffee, machine wants coins, get change back.
# 4. Check transaction successful?
# 5. Make Coffee (deduct resources)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}




resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#! Coffee Cost
espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]


profit = 0
machine_fed = 0
change = 0
penny = 0.01 
dime = 0.1 
nickel = 0.05 
quarter = 0.25

#! Buyer change
espresso_change = machine_fed - espresso_cost
latte_change = machine_fed - latte_cost
cappuccino_change = machine_fed - cappuccino_cost



#! Resources
machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources ["coffee"]
print(machine_coffee)


#! Espresso ingredints
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]




#! Late ingredients
latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]


#! Cappucino ingredients
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

print(cappuccino_water)

#TODO Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
#? a) Check the user's input to decide what to do next.
#? b) The prompt shold show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.



while machine_water > 50: 
    user_choice = input("What would you like? Choose: A)Espresso, B)Latte, C)Cappuccino").lower()
    if user_choice == "a":
        print(f"Please provide ${espresso_cost}")
        amount_in_penny = int(input("How many pennys will you use?"))
        amount_in_dime = int(input("How many dimes will you use?"))
        amount_in_nickle = int(input("How many nickles will you use?"))
        amount_in_quarter = int(input("How many quarters will you use?"))
        p_amount = amount_in_penny * penny #entered penny
        d_amount = amount_in_dime * dime #entered dime
        n_amount = amount_in_nickle * nickel #entered nickel
        q_amount = amount_in_quarter * quarter #entered quarter

        machine_fed = q_amount + d_amount + n_amount + p_amount
        
        print(p_amount) 
        print(q_amount)
        print(machine_fed)
        
        if machine_fed >= espresso_cost:
            machine_water = machine_water - espresso_water
            machine_coffee = machine_coffee - espresso_coffee
            print(machine_water)
            print("Here you go!")
        
        elif machine_fed < espresso_cost:
            amount_in_penny = int(input("How many pennys will you use?"))
            amount_in_dime = int(input("How many dimes will you use?"))
            amount_in_nickle = int(input("How many nickles will you use?"))
            amount_in_quarter = int(input("How many quarters will you use?"))
            if machine_fed > espresso_cost:
                espresso_change = machine_fed - espresso_cost
                print(f"Here is your change {espresso_change}")
        
        elif machine_fed > espresso_cost:
            espresso_change = machine_fed - espresso_cost
            print(f"Here is your change {espresso_change}")
    elif user_choice == "b":
        print(f"Please provide ${latte_cost}")
        amount_in_penny = int(input("How many pennys will you use?"))
        amount_in_dime = int(input("How many dimes will you use?"))
        amount_in_nickle = int(input("How many nickles will you use?"))
        amount_in_quarter = int(input("How many quarters will you use?"))
        p_amount = amount_in_penny * penny #entered penny
        d_amount = amount_in_dime * dime #entered dime
        n_amount = amount_in_nickle * nickel #entered nickel
        q_amount = amount_in_quarter * quarter #entered quarter

        machine_fed = q_amount + d_amount + n_amount + p_amount
        
        print(p_amount) 
        print(q_amount)
        print(machine_fed)
        
        if machine_fed >= latte_cost:
            machine_water = machine_water - latte_water
            machine_coffee = machine_coffee - latte_coffee
            machine_milk = machine_milk - latte_milk
            print(machine_water)
            print("Here you go!")
        
        elif machine_fed < latte_cost:
            print(f"You only entered {machine_fed}")
            amount_in_penny = int(input("How many pennys will you use?"))
            amount_in_dime = int(input("How many dimes will you use?"))
            amount_in_nickle = int(input("How many nickles will you use?"))
            amount_in_quarter = int(input("How many quarters will you use?"))
        
        elif machine_fed > latte_cost:
            latte_change = machine_fed - latte_cost
            print(f"Here is your change {latte_change}")
    elif user_choice == "report":
        print(f"Amount of water in the machin {machine_water}, coffee {machine_coffee}, milk {machine_milk}, cash in machine {machine_fed}")
    elif user_choice == "off":
        break
    else:
        print(f"Please provide ${cappuccino_cost}")
        amount_in_penny = int(input("How many pennys will you use?"))
        amount_in_dime = int(input("How many dimes will you use?"))
        amount_in_nickle = int(input("How many nickles will you use?"))
        amount_in_quarter = int(input("How many quarters will you use?"))
        p_amount = amount_in_penny * penny #entered penny
        d_amount = amount_in_dime * dime #entered dime
        n_amount = amount_in_nickle * nickel #entered nickel
        q_amount = amount_in_quarter * quarter #entered quarter

        machine_fed = q_amount + d_amount + n_amount + p_amount
        
        print(p_amount) 
        print(q_amount)
        print(machine_fed)
        
        if machine_fed >= cappuccino_cost:
            machine_water = machine_water - cappuccino_water
            machine_coffee = machine_coffee - cappuccino_coffee
            machine_milk = machine_milk - cappuccino_milk
            print(machine_water)
            print("Here you go!")
        
        elif machine_fed < cappuccino_cost:
            print(f"You only entered {machine_fed}")
            amount_in_penny = int(input("How many pennys will you use?"))
            amount_in_dime = int(input("How many dimes will you use?"))
            amount_in_nickle = int(input("How many nickles will you use?"))
            amount_in_quarter = int(input("How many quarters will you use?"))
        
        elif machine_fed > latte_cost:
            cappuccino_change = machine_fed - cappuccino_cost
            print(f"Here is your change {cappuccino_change}")

            





#TODO Turn off the Coffee Machine by entering "off" to the prompt/
#? a) For maintaners of the coffee machine, they can use "off" as the secret word to turn off the machine. Your code should end execution when this happens.



#TODO Print report.
#? a) When the user enters "report" to the promp, a report should be generated that shows the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

#TODO Check resources sufficient?
#? a) When the user chooses a drink, the program should check if there are enough resources to make that drink.
#? b) E.G. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#? not continue to make the drink but print: “Sorry there is not enough water.”
#? c) The same should happen if another resrouce is depleted, e.g. milk or coffee

#TODO Process coins.
#? a) If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#? b) Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#? c) Calculate the monetary value of the coins inserted. E.G. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

#TODO Check transaction succesfful?
#? a) Check that the user has inserted enough money to purchase the drink they selected. 
#? E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins theprogram should say 
#? “Sorry that's not enough money. Money refunded.”.

#? b) But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

#? c) If the user has inserted too much money, the machine should offer change. E.G. "Here is $2.45 dollars in change." The change should be rounded to 2 decimal places.

#TODO Make Coffee
#? If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.

#? Report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee