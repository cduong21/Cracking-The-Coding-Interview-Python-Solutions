import unittest

# Replace all spaces in the string with %20 

'''
runtime: O(N)
'''

def URLify(string, length):
    s1 = string.replace(" ", "%20")
    return s1 

test = "Mr John Smith"
length = 13

'''
loop thru every char, if you see " ", then append %20 
rebuild the string 
'''
def URLify1(string, length): 
    final_string = ""
    for i in range(length):
        if string[i] == " ":
            final_string += "%20"
        else: 
            final_string += string[i]
    return final_string

print(URLify1(test, length))
