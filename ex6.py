import string
import re
from sys import argv
from operator import itemgetter
script, file_input = argv

target = open(file_input)
text = target.read()
target.close()

text = text.lower()

text = string.translate(text, None, string.punctuation)

text = string.strip(text)

text = text.split()

dictionaryText = {}

for item in text: 
   if item not in dictionaryText:
   	dictionaryText[item]=1 
   else:
   	dictionaryText[item]+=1

dictionarySorted = sorted(dictionaryText.items(), key=lambda x: (-x[1],x[0]) )

print dictionarySorted
 