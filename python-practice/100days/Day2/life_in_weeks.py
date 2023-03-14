
#! LIFE IN WEEKS CALCULATOR UNTILL THE AGE OF 90
#? How many days do you have left?

print("Hi, please provide us with your age, and we will tell you how many days you have left untill you turn 90")

life_expectancy = 35

while True:
    try:
        your_age = int(input("Please provide us with your age"))
        if your_age < 1:
            print("Please provide us with a valid number")
        if your_age > 90:
            print("Are you sure you are alive?")
        else:
            your_weeks = your_age * 48
            your_months = your_age * 12
            your_days = your_age * 356
            days_left = (life_expectancy * 356) - your_days
            months_left =  (life_expectancy * 12) - your_months
            weeks_left = (life_expectancy * 48) - your_weeks
            print(f"You have {days_left} days, {months_left} months, or {life_expectancy - your_age} years left to live, depending how you want to look at it")
            break
        
            
    except ValueError:
        print("Please enter a valid age number")
        continue
            