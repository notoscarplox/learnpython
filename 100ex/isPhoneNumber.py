def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False

    for i in range(8, 11):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

"""
Regular expressions, called regexes for short, are descriptions for a pat-
tern of text. For example, a \d in a regex stands for a digit character—that
is, any single numeral from 0 to 9. The regex \d\d\d-\d\d\d-\d\d\d\d is used
by Python to match the same text pattern the previous isPhoneNumber()
function did: a string of three numbers, a hyphen, three more numbers,
another hyphen, and four numbers. Any other string would not match the
\d\d\d-\d\d\d-\d\d\d\d regex.
But regular expressions can be much more sophisticated. For example,
adding a 3 in braces ({3}) after a pattern is like saying, “Match this pattern
three times.” So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches the
correct phone number format.
"""
