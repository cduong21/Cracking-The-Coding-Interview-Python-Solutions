import collections
import unittest

# There are three types of edits that can be performed 
# on strings: (1) insert a char, (2) remove a char (3) replace a char 
# Given two strings, check if they are 1 or 0 edits away
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false 

'''
runtime: 
''' 

def one_away(s1, s2):
    n1 = len(s1) 
    n2 = len(s2)
    tracker = collections.defaultdict(int)
    longer = max(n1, n2)

    if abs(n1-n2) > 1:
        return False 

    for i in range(longer):
        if abs(n1-n2) == 1:
            tracker[s1[i]] += 1 
            tracker[s2[i]] -= 1
            if tracker[i] == 0:
                del tracker[i]
        if len(tracker) == 1:
            return True 
        else: 
            return False 
        
        if n1 == n2:
            tracker[s1[i]] += 1
            tracker[s2[i]] -= 1
            if tracker[i] == 0:
                del tracker[i]
            print(len(tracker))
        if len(tracker) == 2:
            return False
        else: 
            return True

class TestStrings(unittest.TestCase):
    def test_isUnique(self):
        s1 = "pale"
        s2 = "ple"
        s3 = "pales"
        s4 = "bale"
        s5 = "bake"
        self.assertTrue(one_away(s1, s2))
        self.assertTrue(one_away(s3, s1))
        self.assertTrue(one_away(s1, s4))
        self.assertFalse(one_away(s1, s5))

unittest.main()