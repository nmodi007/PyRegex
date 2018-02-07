'''
    use * to match zero or more - the group that precedes the star can occur any number of times in the text.
    It can be completely absent or repeated over and over again.
'''

import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())