#divisible by three fizz, if divisible by five print buzz, if divisible by both fizzbuzz


for number in range(0,1260):
    if (number % 5 == 0) and (number % 3 == 0):
        print("fizzbuzz")
    elif  number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)