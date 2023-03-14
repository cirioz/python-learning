# ################## Scope ##################

# enemies = 1

# def increase_enemies():
    
#     enemies = 2
#     print(f"enemies inside function: {enemies}?")
    
# increase_enemies()
# print(f"enemies outisde function: {enemies}")


# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strength)

# Global Scope

# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
    
#     drink_potion()
# print(player_health)


# # There is no Block Scope

# if 3 > 2:
#     a_variable = 10


# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
        
#     print(new_enemy)


# Modifying Global Scope

# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f'enemies outside function; {enemies}')

#Global constantns

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@ozren_cirkovic"


