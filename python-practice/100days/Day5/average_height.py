
#! Average Height

student_heights = input("Input a list of student heights.").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# print(len(student_heights))


total_height = 0
for h in student_heights:
    total_height += h
print(total_height)

number_of_students = 0
for s in student_heights:
    number_of_students += 1
    print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)

# for n in student_heights:
#     number_of_students = n
#     print(n)
#     total_height = n + total_height
   


# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)
