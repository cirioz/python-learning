
#? Write a program that works out whether if a given number is an odd or even number
#? Even numbers can be divided by 2 with no remainder



while True:
    try:
        user_number_input = int(input("Please give us a number of your choosing 1-100"))
        if user_number_input < 1 or user_number_input > 100:
            print("Please enter a valid integer bigger than 1 and lesser than 100")
    except ValueError:
        print("Please enter a valid integer 1-100")
        continue
    if user_number_input >= 1 and user_number_input <= 100:
        print(f'You entered: {user_number_input}')
        if user_number_input%2 == 0:
            print(f"{user_number_input} is an even number.")
            break
        else:
            print(f"{user_number_input} is an odd number.")
            break
           
        
        
 
# Broj je definisan, odradjena je provera da li je unesen broj
# 
#, ako jeste, proveri se da li je deljiv ili ne sa 2, 
# ako je deljiv sa 2 ispisuje se na konzoli da je broj deljiv sa 2 i da je paran, 
# ako broj nije deljiv sa 2 ispisuje se da je broj neparan i da ispise se da je broj ne paran