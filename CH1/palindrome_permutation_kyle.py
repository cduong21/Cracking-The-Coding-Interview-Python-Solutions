import collections
test = "Tact Coa"

def palindrome_permutation(string):
    string = string.lower().replace(" ", "")
    n = len(string)

    print(string)
    print(n)

    char_count = collections.defaultdict(int)
    for c in string:
        char_count[c] += 1

    print(char_count)
    #If our string is even
    if n % 2 == 0:
        for char in char_count:
            if char_count[char] % 2 != 0:
                return False
    # If our string is odd
    else:
        odd_flag = False 
        for char in char_count:
            if char_count[char] % 2 != 0:
                if odd_flag == True:
                    return False
                else:
                    odd_flag = True

    return(True)

print(palindrome_permutation(test))
