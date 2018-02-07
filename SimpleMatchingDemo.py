'''
    Review of regular expression matching
    1. Import the regex module with import re
    2. Create a Regex object with the re.complie(r'') function.
    3. Pass the string you want to search into the Regex object's search() method.
    4 Call the Match object's group() method to return a string of the actual matched text.
'''
import re

text = 'My number is 415-555-8374'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(text)
print(f'phone number found: {mo.group()}')
