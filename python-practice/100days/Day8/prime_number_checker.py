#prime number checker

number = int(input("Give a number"))

def is_it_prime(number):
    if number % 2 == 0:
        print("not prime")
    elif number % 1 == 0 and number % number == 0:
        print("it is prime")

is_it_prime(number)



#Angela Solution

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
       if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")
            #Not a prime
    #is a prime number
n = int(input("Check this number: "))
prime_checker(number=n)