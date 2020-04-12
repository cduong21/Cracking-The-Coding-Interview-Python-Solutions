import unittest
import collections

# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words
# Tact Coa
# True ('taco cat', 'atco cta')

"""
strip the string and make sure all lowercase 
use default dictionary 
loop through char in string and add to the dictionary (keeps track of freq) 
    if the value is 2 delete -> accounts for longer strings with more chars! 
if it's even 
    set len == 0
if it's odd
    set len == 1

runtime: O(n) 
"""


def palindrome_permutation(string):
    s1 = string.lower().replace(" ", "")
    n = len(s1)
    count = collections.defaultdict(int)

    for i in range(n): 
        count[s1[i]] += 1 
        if count[s1[i]] == 2:
            del count[s1[i]]
    fincount = len(count)
    if n % 2 == 0 and fincount == 0:
        return True 
    if n % 2 == 1 and fincount == 1:
        return True
    else: 
        return False

test = "tactcoapapa"
print(palindrome_permutation(test))

