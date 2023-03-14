#For Loop with Range

# for number in range(1, 100, 2):
#     print(number)
    
total = 0
for number in range(1,101):
    total += number
    
print(total)

#! Adding even numbers

# total_evens = 0
# for number in range(1,101):
#     if number%2 == 0:
#         total_evens += number
#     else:
#         total_evens = total_evens
# print(total_evens)

#? Angelas Solution

total = 0
for number in range(2,101,2):
    total +=  number

print(total)