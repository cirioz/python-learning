#Object from blueprint 

# import another_module
# import prettytable
# # import tkinter as tk  
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# # print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() #kreiranje objekta iz klase PrettyTable
print(table)

table.add_column("Ozren", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])

table.align = "l"
print(table)




