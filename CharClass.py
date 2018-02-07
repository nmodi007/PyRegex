'''
    short hand char classes:
    /d  any numeric digit 0-9
    /D  not numeric didgit
    /w  Any "word" characters
    /W  Any not "word" characters
    /s  Any space, tab, newline char. "space" chars.
'''

import re
#  match text that has one or more numeric digits (\d+), followed by a whitespace char (\s),
#  followed by one or more letter/digit/underscore chars (\w+)

text = '4 bananas, 3 apples 2 pineapples 1 strawberry'
xmasRegex = re.compile(r'\d+\s\w+')
results = xmasRegex.findall(text)
print(results)


'''
    you can make your own char class by using []
    ex. [aeiou] = will match any lowercase vowel
    You can include ranges of letters or numbers by using hyphen.
    ex [a-zA-Z0-9]
'''
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('The lazy fox jumped over the rivEr'))