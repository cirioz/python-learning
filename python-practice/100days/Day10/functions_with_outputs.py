def my_function():
    result = 3*2
    return result


#!Functions with Outputs

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    # print(f"{formated_f_name} {formated_l_name}")
    return f"Result: {formated_f_name} {formated_l_name}" #it tells the computer that is the end of a function
    print("This got printed")
print(format_name(input("What is your first name?"),input( "What is your last name?")))

output = len("Angela")




print(output)