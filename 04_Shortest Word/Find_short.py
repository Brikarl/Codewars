'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''


# My solution
def find_short(s):
    # your code here
    
    list = s.split()
    a = list[0]
    
    for str in list:
        if len(str) < len(a):
            a = str
    
    l = len(a)
    
    return l # l: shortest word length


# Best solution
def find_short(s):
    return min(len(x) for x in s.split())
    