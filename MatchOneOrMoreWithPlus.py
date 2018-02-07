'''
    use + to mean "match one or more". The group preceding the plus must appear at least once.
    It is not optional.
'''

import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)  # mo3 will be none because wo must be in between Bat and man at least once.
