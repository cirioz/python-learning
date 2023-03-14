
#! Highest Score

student_scores = input("Input a list of students score: ").split()

for n in range(0, len(student_scores)):
   student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for n in student_scores:
    if n > highest_score:
        highest_score = n

print(highest_score)    

