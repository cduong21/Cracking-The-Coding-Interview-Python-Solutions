import unittest
# given two strings, write a mthod to decide if one is a permutation of the other

'''
sort the two strings and check if they are equal 
runtime:O(nlogn) 
'''
def check_permutation(string1, string2):
    s1_sort = sorted(string1)
    s2_sort = sorted(string2)
    if s1_sort == s2_sort: 
        return True 
    else: 
        return False 

'''
for the first pass: 
for each character
    if not in set add it with 1 
    if it is in set then increase the counter 
for second pass: 
    if it is in set subtract/ remove it 
'''
def check_permutation1(string1, string2):
    if len(string1) != len(string2):
        return False 
    freq = {} 
    for i in string1:
        if i not in freq: 
            freq[i] = 1
        else:
            freq[i] += 1
    for x in string2: 
        if x in freq: 
            freq[x] -= 1
            if freq[x] == 0:
                del freq[x]
        else: 
            return False 
    if len(freq) == 0:
        return True
    else:
        return False 

class TestStrings(unittest.TestCase):
    def test_isUnique(self):
        s1 = "cat"
        s2 = "tac"
        s3 = "catyy" 
        self.assertTrue(check_permutation1(s1, s2))
        self.assertFalse(check_permutation1(s1, s3))


unittest.main()