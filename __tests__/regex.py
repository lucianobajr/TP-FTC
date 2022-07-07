import re
pattern = r'^[A-Za-z0-9]{1,7}$'

print(bool(re.match(pattern,'ABCDE')))