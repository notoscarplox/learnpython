import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# finds the first coincidence // returns a match object
mo = phoneNumRegex.search('My number is 415-565-4242, and 234-234-8765')

# finds all coincidences // Returns a list of strings as long as there are no groups in the regular expression
mo2 = phoneNumRegex.findall('My number is 415-565-4242, and 234-234-8765')

print('Phone number found: ' + mo.group())
print(f'Phones are: {mo2}')
