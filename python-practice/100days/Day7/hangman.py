
import random
import hangman_words
import hangman_art

from hangman_words import word_list


chosen_word = random.choice(word_list)

lives = 6
from hangman_art import logo, stages
print(logo)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False 
stage = 0


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        else:
            print("No match")
    #TODO-2: - If guess is not a letter in the chosen_word, then reduce 'lives' by 1.add()
    #If lives goes down to 0, then the game should stop and it should print "You lose."
    # if guess not in chosen_word:
    
    #Join all the elements in the list and turn it into a String
    print(f"{''.join(display)}")
    #Check if user has got all letters.
    
        # elif letter != guess:
        #     stage += 1 
        #     if stage > 0:
        #         print("Stage1")
        #         if stage > 1:
        #             print("Stage2")
        #             if stage > 2: 
        #                 print("Stage3")
        #                 if stage > 3:
        #                     print("Stage4")
        #                     if stage > 4:
        #                         print("Stage5")
        #                         if stage > 5:
        #                             print("Stage6")
        #                             if stage > 6:
        #                                 print("You lose!")
        #                                 break
    # print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining
    from hangman_art import stages
    print(stages[lives])
# Program chose word
# User input
#? If user input correct, add letter to print statement "Print congradulations and guess another letter or try the whole sentence"



