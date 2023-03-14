
# #! All 8 digit combinations

# combo_numbers = [1,2,3,4,5,6,7,8]

# def combo(L):

#     for i in combo_numbers:
#         for j in combo_numbers:
#             for k in combo_numbers:
#                 for l in combo_numbers:
#                     for m in combo_numbers:
#                         for o in combo_numbers:
#                             for p in combo_numbers:
#                                 for q in combo_numbers:
#                                     if (i!=j and j!=)


# Python program to print all
# the possible combinations

from itertools import permutations

# Get all combination of [1, 2, 3]
# of length 3
comb = permutations(["K", "P", "D","S"], 4)

for i in comb:
   print(i)