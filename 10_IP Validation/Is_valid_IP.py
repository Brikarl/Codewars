'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
'''


# My solution
def is_valid_IP(strng):
    IPlist = strng.split(".")
    if  len(IPlist) != 4:
        return False
    for str in IPlist:
        if str.isdigit() == False:
            return False
        i = int(str)
        if str.find('0') == 0 and i != 0:
            return False
        if i < 0 or i > 255:
            return False
    return True


# Best solution
def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4
    