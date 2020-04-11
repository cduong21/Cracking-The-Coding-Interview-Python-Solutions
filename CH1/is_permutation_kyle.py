""" Given two strings, write a method to decide if one is a permutation of the other. """
import collections, unittest

def is_permutation(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 != n2:
        return False

    chars = collections.defaultdict(int)
    for i in range(n1):
        chars[s1[i]] += 1
        chars[s2[i]] -= 1

        if chars[s1[i]] == 0:
            del chars[s1[i]]
        if chars[s2[i]] == 0:
            del chars[s2[i]]

    if len(chars) == 0:
        return True

    return False


class TestStrings(unittest.TestCase):
    def test_isUnique(self):
        s1 = "cat"
        s2 = "tac"
        s3 = "catyy" 
        s4, s5 = "", ""
        s6, s7 = "rats", "star"
        s8, s9 = "doggy", "gogdy"
        s10, s11 = "kitten", "cat"
        self.assertTrue(is_permutation(s1, s2))
        self.assertFalse(is_permutation(s1, s3))
        self.assertTrue(is_permutation(s4,s5))
        self.assertTrue(is_permutation(s6, s7))
        self.assertTrue(is_permutation(s8, s9))
        self.assertFalse(is_permutation(s10, s11))


unittest.main()