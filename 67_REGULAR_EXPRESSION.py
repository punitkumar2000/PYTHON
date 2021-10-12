#REGULAR EXPRESSION

# import re
# mystr = '''Tata Limited
# Dr. David Landsman, executive director
# 18, Grosvenor Place
# London SW1X 7HSc
# Phone: +44 (20) 7235 8281
# Fax: +44 (20) 7235 8727
# Email: tata@tata.co.uk
# Website: www.europe.tata.com
# Directions: View map
#
# Tata Sons, North America
# 1700 North Moore St, Suite 1520
# Arlington, VA 22209-1911
# USA
# Phone: +1 (703) 243 9787
# Fax: +1 (703) 243 9791
# 66-66
# 455-4545
# Email: northamerica@tata.com
# Website: www.northamerica.tata.com
# Directions: View map fass
# harry bhi lekin
# 123456--12
# bahut hi badia aadmi aiaiiiiiii abcde'''


# pattern = re.compile(r'fass')
# pattern = re.compile(r'.north')
# pattern = re.compile(r'^Tata')
# pattern = re.compile(r'ii$')
# pattern = re.compile(r'ai{2}')
# pattern = re.compile(r'(ai){1}')
# pattern = re.compile(r'ai{1}|Fax')
# pattern = re.compile(r'ai*')
# pattern = re.compile(r'ai+')


# Special Sequences
# pattern = re.compile(r'\ATata')
# pattern = re.compile(r'abc\Z')
# pattern = re.compile(r'\bFax')
# pattern = re.compile(r'27\b')
# pattern = re.compile(r'97\B')
# pattern = re.compile(r'\d{6}--\d{2}')
# pattern = re.compile(r'Tata\D')
# pattern = re.compile(r'abcde\s')
# pattern = re.compile(r'\Sabcde')
# pattern = re.compile(r'\wabcde')
# pattern = re.compile(r'\Wabcde')

# matches = pattern.finditer(mystr)
# for match in matches:
#     print(match)

# Given a string with a lot of indian phone numbers starting from +91

import re
mystring = '''
+91-1234567890
+88-1234567890
+44-5555545445
+66-4445221156
+91-5555456624
+91-5544226555
+78-5441115124
+44-5551145212
+66-24425511
+99-4444521155
'''

pattern = re.compile(r'.+91-\d{10}')

matches = pattern.finditer(mystring)
for match in matches:
    print(match)