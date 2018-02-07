'''
    The Search() will return the Match object of the first matched text in the searched string.
    the findall() will return the strings of every match in the searched string.
'''
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_numbsers_in_text = phoneNumRegex.findall('Cell: 384-758-2833 Work: 489-584-9123')
print(phone_numbsers_in_text)

phoneNumRegex_area_code = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone_numbers = phoneNumRegex_area_code.findall('Cell: 384-758-2833 Work: 489-584-9123')
print(phone_numbers)