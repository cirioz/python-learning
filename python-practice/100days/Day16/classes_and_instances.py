# Python Object-Oriented Programming

# Reause Functions - Benefit

class Employee: #no atributes and method
    
    def __init__(self, first, last, pay): #initialize or constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)



#class vs instance of a class

#!class is a blueprint for class-instances
#

emp1 = Employee("Corey", "Schafer", 50000) #unique instances of Employee class
emp2 = Employee("Suzana", "Mandic", 90000) #

emp1.fullname()
Employee.fullname(emp1)

print(emp1) #both unique objects
print(emp2)

#instance variable vs class variable 

# instance variable contains data that is unique for each instance

# emp1.first = "Corey"
# emp1.last = "Schafer"
# emp1.email = "Corey_Schafer@company.com"
# emp1.pay = 60000


# emp2.first = "Suzana"
# emp2.last = "Mandic"
# emp2.email = "Suzana_Mandic@company.com"
# emp2.pay = 90000

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())

print(emp1.fullname())

emp1.fullname()
print(Employee.fullname(emp1))

Employee.fullname(emp1)



#! Instead of manually





