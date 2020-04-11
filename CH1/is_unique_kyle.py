# Implement an alg to determine if a string has all unique charactes. 
# What if you cannot use additional data structures? 
import unittest

# Solution using set. O(n) Time Complexity. O(n) Space Complexity.
def isUnique1(input):
    if not input:
        return True

    s = set()
    for c in input:
        if c not in s:
            s.add(c)
        else:
            return False
            
    return True

# Solution using sort. O(nlogn) Time Complexity. O(1) Space Complexity
def isUnique2(string):
    string = sorted(string)
    n = len(string)

    for i in range(1, n):
        if string[i] == string[i - 1]:
            return False 
            
    return True

class TestStrings(unittest.TestCase):

    def test_isUnique(self):
        test1 = "abcde"
        test2 = "abbcde"
        test3 = ""
        test4 = "aaaaa"
        test5 = "efazck"
        self.assertTrue(isUnique2(test1))
        self.assertFalse(isUnique2(test2))
        self.assertTrue(isUnique2(test3))
        self.assertFalse(isUnique2(test4))
        self.assertTrue(isUnique2(test5))

unittest.main()







    