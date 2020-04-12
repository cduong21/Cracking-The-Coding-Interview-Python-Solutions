test = "Mr John Smith"
length = 13

def URLify1(string, length):
    return string.replace(" ", "%20")

def URLify2(string, length):
    output = ""
    for c in string:
        if c == " ":
            output += "%20"
        else:
            output += c
    return output

print(URLify1(test, length))
print(URLify2(test, length))