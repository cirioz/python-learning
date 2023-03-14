
#! BMI CALCULATOR

print("Welcome to the BMI calculator")

while True:
    try:
        weight = int(input("Please provide us with your weight in kg"))
        if weight < 1:
            print("Please enter a valid number.")
        height_in_cm = int(input("Please provide us with your height in cm"))
        if height_in_cm < 1:
            print("Please enter a valid number.")
        height_in_m = (height_in_cm / 100)
        print(height_in_m)
        
        bmi = (weight/(height_in_m*height_in_m))
        print(bmi)
        print(type(bmi))
        bmi_format = (bmi)
        print(type(bmi_format))
        # bmi_format = int(bmi_format)
        print(type(bmi_format))
        
        
        if bmi_format < 18.5:
            
            bmi_format = "{:.2f}".format(bmi_format)
            print(f"Your are underwight because your BMI is {bmi_format}" )
        elif bmi_format > 18.5 and bmi_format < 25:
            print("You are of normal weight")
        elif bmi_format > 25 and bmi_format < 30:
            print("You are overweight")
        elif bmi_format > 30 and bmi_format < 35:
            print("You are obese")
        else:
            print("You are clinically obese")
        break
    except ValueError:
        print("Please enter your weight using numbers in kg")
        continue
    
# Work on getting more precise values
    

             