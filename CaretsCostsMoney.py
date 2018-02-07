'''
    use the ^ at the start of a regex to indicate that a match must occur at the beginning of the searched text.
    use the $ at the end of a regex to indicate that a match must occur at the end of the searched text.
'''


import re
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo.group())

mo2 = beginsWithHello.search('world Hello')
print(mo2 is None)

#  r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters

