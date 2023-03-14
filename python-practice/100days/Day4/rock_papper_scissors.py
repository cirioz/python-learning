import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# choices = [rock, paper, scissors]
# print(choices[1])

# while True:
#     try:
#         user_choice = choices[int(input("What do you choose, 1 for rock, 2 for paper or 3 for scissors?"))]
#         print(type(input))
#         if user_choice not in choices:
            
#             print("This is not a part of suggested options")
#             raise ValueError
#     except ValueError:
#         print("Please enter a valid number between 1 - 3")
#         continue
#     if user_choice in choices: 
#         print(f'You entered: {user_choice - 1}')
       
choices = [0,1,2]   
# user_choice = int(input("Rock 0, Paper 1, Scissosr 2"))


# print(f"Computer chose {computer_choice}")

game_images = [rock, paper, scissors]
while True:
    try:
        user_choice = int(input("Rock 0, Paper 1, Scissosr 2"))
        computer_choice  = random.randint(0,2)
        if user_choice == computer_choice:
            print("It's a tie")
            print(f"Computer choice {game_images[computer_choice]}")
            print(f"Your choice {game_images[user_choice]}")
            break
        elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
            print("You have lost")
            print(f"Computer choice {game_images[computer_choice]}")
            print(f"Your choice {game_images[user_choice]}")
            break
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
            print("You have won")
            print(f"Computer choice {game_images[computer_choice]}")
            print(f"Your choice {game_images[user_choice]}")
            break
        if user_choice not in choices:
            
            print("This is not a part of suggested options")
            raise ValueError
    except ValueError:
        print("Please enter a valid number between 0 - 2")
        continue
    
   