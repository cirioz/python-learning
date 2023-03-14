student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
#? Moje resenje
for key in student_scores:
    
    if student_scores[key] < 70:
        print(f"{key} did not pass, with the grade of FAIL")
        student_grades[key] = " did not pass, with the grade of FAIL"
    elif student_scores[key] > 70 and student_scores[key] < 80:
        student_grades[key] = " passed with the grade of Acceptable"
        print(f"{key} passed with the grade of Acceptable")
    elif student_scores[key] > 80 and student_scores[key] < 90:
        student_grades[key] = "result Exceeds Expectations"
        print(f"{key} result Exceeds Expectations ")
    else:
        student_grades[key] = "grade is Outstanding!"
        print(f"{key} grade is Outstanding!")
        
        #? Andjelino resenje
for key in student_scores:
    score = student_scores[key]
    if score < 70:
        print(f"{key} did not pass, with the grade of FAIL")
        student_grades[key] = " did not pass, with the grade of FAIL"
    elif score > 70 and score < 80:
        student_grades[key] = " passed with the grade of Acceptable"
        print(f"{key} passed with the grade of Acceptable")
    elif score > 80 and score < 90:
        student_grades[key] = "result Exceeds Expectations"
        print(f"{key} result Exceeds Expectations ")
    else:
        student_grades[key] = "grade is Outstanding!"
        print(f"{key} grade is Outstanding!")
# student_grades = 
    

# 🚨 Don't change the code below 👇
print(student_grades)