#Homework #4
#Write a program to lazily rewrap text from the filename passed so that it fits an 80
#column window without breaking any words. Use a generator that yields the next lines of
# text, each containing as many words as possible

import sys
import re
#READ THE PASSED FILE
with open(sys.argv[1], 'r') as f:
    file = f.read()
text=re.split('[\s\n]+',file)

def lines(t):
    str=""
    for i in t:
        if (len(str)+len(i))<=80: #IF  NEWS TRING + ELEMENT "STR" IS LESS THEN 80, KEEP ADDING ELEMENTS
            str+=i+" "
        else:#IF NEW STRING+ ELEMENT MORE THEN 80, PRINT NEW STRING
            yield str
            str=i+" "
    yield str

for value in lines(text):
   print(value)


