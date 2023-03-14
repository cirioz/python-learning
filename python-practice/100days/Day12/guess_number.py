#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

number = random.randint(1,100)
print(number)

guess_count = 0
# 



def guess_game():
    
    
    
    # guess = int(input("What number do you think it is?"))
    guess = int(input("What number do you think it is?"))
    
    global guess_count
    
    
    
    
    while True:
        guess_count += 1
    
        guess != number
        
        if guess_count == 10:
            print(f"You have guessed {guess_count } number of times")
            print("You exceeded your guess limit")
            break 
        elif guess < number:
                print("The guess is lower than the number")
                # guess_count += 1
                print(f"You have guessed {guess_count } number of times")
                return guess_game()
        elif guess > number:
                print("The guess is higher than the number")
                # guess_count += 1
                print(f"You have guessed {guess_count } number of times")
                return guess_game()
        
        if guess == number:
            print("Good job!")
            break
               
        
            # else:
                
        # if guess_count > 10:
            
       
            
    
    # if guess_count > 10:
    #     print("You have lost")

guess_game()
        
# end_game()
    
        
    
    

