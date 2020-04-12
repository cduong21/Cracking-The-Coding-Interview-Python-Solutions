import unittest

def one_away(string1, string2):
    n1, n2 = len(string1), len(string2)

    # If our strings differ in length greater than one, they are not one away
    if abs(n1 - n2) > 1:
        return False

    # If our strings are 1 length apart, we either remove or insert
    elif abs(n1 - n2) == 1:
        itr1, itr2 = 0, 0
        shorter = min(string1, string2, key=len)
        longer = max(string1, string2, key=len)
        edit = False

        # We iterate through both strings and simulate an insert/removal by moving\
        # our iterator on the longer string forward when we find a mismatch
        while itr1 < len(shorter) and itr2 < len(longer):
            if shorter[itr1] != longer[itr2]:
                if edit == True:
                    return False 
                edit = True
                itr2 += 1
                if shorter[itr1] != longer[itr2]:
                    return False
            itr1 += 1
            itr2 += 1

        return True
    # If our strings are the same length, we only allow one character replacement
    else:
        replace = False

        for i in range(n1):
            if string1[i] != string2[i]:
                if replace == False:
                    replace = True 
                else:
                    return False 

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