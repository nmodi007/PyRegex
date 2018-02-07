'''
    If you want to match only optionally. The regex should find a match whether or not the bit of text
    is there.
    The ? char flags the group that precedes it as an optional part of the pattern.
'''

import re
text = 'The Adventures of Batman'
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search(text)
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

#  regex that do or do not have an area code

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 382-184-8583')
print(mo1.group())

mo2 = phoneRegex.search('My number is 484-2839')
print(mo2.group())