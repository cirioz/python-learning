def my_function():
    result = 3*2
    return result


#!Functions with Outputs

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"

print(format_name("oZren", "ciRkovic"))

output = len("Angela")


print(output)