"""Simple hello."""

print("Hello world!", end="")

maximum = int(input(" Please Enter the Maximum Value : "))

Oddtotal = 0
number = 1

while number <= maximum:
    if (number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
    number = number + 1

print("The Sum of Odd Numbers from 0 to {0} = {1}".format(maximum, Oddtotal))