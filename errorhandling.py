import numbers
from unittest import result


try:
    number = int(input("Enter a number: "))
    divisor =int(input("Enter a divisor: "))
    result = number / divisor
    print (result)
except Exception as e:
    print("An exception occurred during the division: ", e)