'''
    Adding parentheses will create groups in the regex.
    (\d\d\d)-(\d\d\d-\d\d\d\d) --> group area code and the rest of the phone number.
'''
import re
text = 'My number is 432-432-8753'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(text)
print(f'area code: {mo.group(1)}')
print(f'phone number: {mo.group(2)}')
print(f'entire matched text: {mo.group()}')
print(f'all groups at once: {mo.groups()}')