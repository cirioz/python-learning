class Employee: #class called employee, takes first name and last name
    def __init__(self, first_name, last_name): #class initializer, storing first and last name in it
        self.first_name = first_name
        self.last_name = last_name


    def get_full_name(self): #second method called get full name, get full name gets self as only paramater
        return f"{self.first_name} {self.last_name}" #it returns first name + last name

e = Employee("Vera", "Schmidt") # employee object 
print(e.get_full_name()) #we print the full name

#self 

#each method in a class takes self as paramater

# code recreation if python does not have a class

def get_full_name(employee):
    return f'{employee["first_name"]} {employeelast_name["last_name"]}'


def create_employee(first_name, last_name, get_full_name_func):
    d = {"first_name": first_name, "last_name":last_name, "get_full_name": get_full_name_func}
    return d

e = create_employee("Vera", "Schmidt", get_full_name)
print(e["get_full_name"](e))



