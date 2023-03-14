wall_height = int(input("What is the wall height?"))
wall_width = int(input("What is the wall width?"))
can_coverage = 5
import math


def number_of_cans(wall_height, wall_width):
    print(f"You need {math.ceil((wall_height * wall_width) / can_coverage)} cans of paint")
    
number_of_cans(wall_width, wall_height)


#! Paint area calculator

# 1 can of paint can cover 5 square meters of wall
# random height, random width
# how many cans of paint will i need to buy?
# number of cans = (wall height x wall width) / coverage per can

def area_calculator(height, width, coverage_per_can = 5):
    cans_needed = math.ceil((height*width) / coverage_per_can)
    print(f"We will need {cans_needed} to paint the wall")
    
area_calculator(height=int(input("What is the height of the wall?")), width=int(input("What is the width of the wall?")) )

