# Task: Write a program that demonstrates a generator yielding
# one timestamp at a time from access_log

import re

for x in [i for i in set(re.split('[\s\[\]]+',open("access_log").read()))
          if re.findall(r"\d{2}/\w{3}/\d{4}", i)]:
    print(x)




