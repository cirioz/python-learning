
#! Higher or lower - Moje resenje

import random 
import game_data 
def random_number():
    return (random.randrange(1,50))
    
game_running = True
score = 0
while game_running == True:
    person1 = game_data.data[random_number()] #osoba 1 iz game data
    person2 = game_data.data[random_number()] #osoba 2 iz game data
    person1_name = person1["name"] #ime osobe 1
    person2_name = person2["name"] #ime osobe 2
    person1_followers = person1['follower_count'] #broj pratilaca osobe 1
    person2_followers = person2['follower_count'] #broj pratilaca osobe 2
    result1 = person1_followers > person2_followers
    result2 = person2_followers > person1_followers
    guess = int(input(f"Who has more followers? {person1_name} or {person2_name} Chose 1 for A and 2 for B "))
    if guess == 2 and result2 == True:
        print("1",result1, guess,person1_followers)
        person1_followers = person2_followers
        score += 1
        print(f"Your score is {score}")
        print(person1_followers)
    elif guess == 1 and result1 == True:
        print("2",result2, guess,person2_followers)
        person1_followers = person1_followers
        score +=1
        print(f"Your score is {score}")
        print(person1_followers)
    else:
        print(guess,person1_followers, person2_followers)
        print("You have lost")
        break

