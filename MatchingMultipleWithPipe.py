'''
    use the | char to match one of many expressions.
    ex. r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'
    if both match...first occurrence is returned.
'''

import re
text = 'some text with Batman and some more with Tina Fay'
heroRegex = re.compile(r'Batman|Tina Fay')
mo = heroRegex.search(text)
print(mo.group())

mo_all = heroRegex.findall(text)
print(mo_all)