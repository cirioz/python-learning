numbers = [1,2,3]
numbers = numbers.append(4)
print(numbers)

import math


def square_root(numbers):
    result = []
    for number in numbers:
        result.append(math.sqrt(number))
    return result

numbers = [1,4,9,16,25,36,39,54,65]
print(square_root(numbers))