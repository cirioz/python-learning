
#! LEAP YEAR CHECKER
# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.
# The reason why we have leap years is really fascinating, this video does it more justice:


year_input = int(input("Please provide us with the year you would like us to check."))


if year_input % 4 == 0 and year_input % 100 == 0 and year_input % 400 == 0:
    print(f"Year {year_input} is a leap year")
elif year_input % 4 == 0 and year_input % 100 == 0 and year_input % 400 != 0:
    print(f"Year {year_input} is not a leap year")
elif year_input % 4 == 0 and year_input % 100 == 0:
    print(f"Year {year_input} is a leap year")
elif year_input % 4 == 0 and year_input % 100 != 0:
    print(f"Year {year_input} is not a leap year")
elif year_input % 4 != 0:
    print(f"Year {year_input} is not a leap year")

# if year_input % 4 == 0:
#     if year_input % 100 == 0:
#         if year_input % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")
    
    
    
            

            

