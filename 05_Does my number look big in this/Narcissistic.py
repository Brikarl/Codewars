'''
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
'''


# My solution
def narcissistic( value ):
    # Code away
    number_of_digits = len(str(value))
    sum_result = 0
    for digit in str(value):
        sum_result += int(digit)**number_of_digits
    if sum_result == value:
        return True
    else:
        return False


# Best solution
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
    