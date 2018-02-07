'''
    If you have a group that you want to repeat a specific number of times, follow the group in
    your regex with a number in curly brackets.
    ex. (Ha){3} will match the string 'HaHaHa'
'''

import re
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('HaHaHa')
print(mo.group())

mo2 = haRegex.search('HaHaHaHaHaHaHa')
print(mo2.group())