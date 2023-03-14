# get 2 cards, add them, do you want another card?, get third card add it , stand or hit again, if over 21 lose
#! Funkcija za deljenje karata igracima, jedan igrac treba da dobije 2 karte, prvo jedan pa drugi, punimo jednu pa drugu promenljivu
#! 
"""
 p1 dobije kartu k 
 p2 dobije kartu k
 p1 dobije kartu k   
 p2 dobije kartu k  
 upit: da li zelis da dobijes jos jednu kartu ili da stanemo
 upit: odogovr ako je daj, prosledi kartu, ako je rezultat veci od 21 odmah zaustavi
 ako je stani, uporedi 2 vrednosti
 
"""


import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


player1 = 0
player2 = 0



# def Choice():
#     if p1Choice == 'hit':
#         player1 += cards[random.randint(1,11)]
#     elif p1Choice == 'stand':
#         return
        


def startGame():
    # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    global player1
    global player2
    for count in range(0,2):
        player1 += cards[random.randint(1,11)]
        player2 += cards[random.randint(1,11)]
        p1Choice = input("Would you like another card? 'yes' or 'no'").lower()       
        if p1Choice == 'yes':
            player1 += cards[random.randint(1,11)]
            print(player1)
            print(player2)
        else:
            break
            if player1 > 21:
                break
           
            
            
        
        
startGame()   
       
print(player1)
print(player2)        

# player1 += cards[random.randint(0,12)]
# player1 += cards[random.randint(0,12)]
# print(player1)

# for card in cards:
#     # print(i)
#     player1_input = input("Choose 'hit' or 'stand'").lower()
#     print(player1_input)
#     if player1_input == "hit":
#         player1 += cards[random.randint(0,12)]
#         print(player1)
#     elif player1_input == 'stand':
#         print(player1)
#         break    
#     # elif player1 < 21:
#     elif player1 > 21:
#         print(f"You have lost, with {player1}")
#         break
    
        
    

# print(player1)
# def hit()


# def stand()


