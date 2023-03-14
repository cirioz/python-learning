
#! TIP CALCULATOR

print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?"))
print(f"${total_bill}")
bill_split = int(input("How many people to split the bill?"))
tip_options = [10, 12, 15]

while True:
    try:
        tip_percentage = int(input('What percentage would you like to give? You can give a 10, 12 or 15 percent tip. '))
        # print(tip_percentage)
        
        if tip_percentage not in tip_options:
            print("We only can agree on the provided tip options")
            raise ValueError 
        
        break
    except ValueError:
        print("Please enter a number")

if tip_percentage == 10:
    tip = total_bill*(tip_percentage/100)
    final_amount_per_person = round(total_bill/bill_split) + (tip/bill_split)
    final_amount_per_person = "{:.2f}".format(final_amount_per_person)
    print(f"The tip should be ${tip}, per person we should give ${tip/bill_split} ")
    print(f"Each person should give ${final_amount_per_person}")
elif tip_percentage == 12:
    tip = total_bill*(tip_percentage/100)
    final_amount_per_person = round(total_bill/bill_split) + (tip/bill_split)
    final_amount_per_person = "{:.2f}".format(final_amount_per_person)
    print(f"The tip should be ${tip}, per person we should give ${tip/bill_split} ")
    print(f"Each person should give ${final_amount_per_person}")
else:
    tip = total_bill*(tip_percentage/100)
    final_amount_per_person = round(total_bill/bill_split) + (tip/bill_split)
    final_amount_per_person = "{:.2f}".format(final_amount_per_person)
    print(f"The tip should be ${tip}, per person we should give ${tip/bill_split} ")
    print(f"Each person should give ${final_amount_per_person}")
    

