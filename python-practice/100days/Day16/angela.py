# import another_module_angela
# print(another_module_angela.another_variable)
# import turtle

# ---------------------------------

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# ----------------------------------

# import prettytable

from prettytable import PrettyTable
table = PrettyTable()

#adding row by row
table.field_names = ["Pokemon Name", "Type", "Attack", "Rarity"]
table.add_rows(
    [
        ["Pikachu", "Electric", 333333, "Rare"],
        ["Mochop", "Ground", 333333, "Very Rare"],
        ["Dragonite", "Flying", 333333, "Common"],

       
    ]
)

print(x)

