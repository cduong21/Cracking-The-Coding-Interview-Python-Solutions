import unittest

# Implement an alg to determine if a string has all unique charactes.
# What if you cannot use additional data structures?

"""
using additonal data structure: 
    for loop through each of the chars 
    if its not in the hashset then add it
    if it in the set -> return false! 
    runtime: O(n) 
"""


def isUnique1(string):
    s = set()
    for i in string:
        if i in s:
            return False
        else:
            s.add(i)
    return True

"""
without additional data structure
    sort the string and then use pointers to check 
    runtime: O(nlogn)
"""


def isUnique2(string):
    sort_string = sorted(string)
    for i in range(len(string) - 1):
        if sort_string[i] == sort_string[i + 1]:
            return False
    return True


def isUnique3(string):
    string = sorted(string)
    n = len(string)
    for i in range(1, n):
        if string[i] == string[i - 1]:
            return False
    return True


"""
without additional data structure
    brute force: 2 runners 
"""


def isUnique4(string):
    n = len(string)
    for i in range(1, n):
        for x in range(i + 1, n):
            if string[i] == string[x]:
                return False
    return True


class TestStrings(unittest.TestCase):
    def test_isUnique(self):
        test1 = "abcde"
        test2 = "abbcde"
        test3 = ""
        test4 = "aaaaa"
        test5 = "efazck"
        self.assertTrue(isUnique4(test1))
        self.assertFalse(isUnique4(test2))
        self.assertTrue(isUnique4(test3))
        self.assertFalse(isUnique4(test4))
        self.assertTrue(isUnique4(test5))


unittest.main()
