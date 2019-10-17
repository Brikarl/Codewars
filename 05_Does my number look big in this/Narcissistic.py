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