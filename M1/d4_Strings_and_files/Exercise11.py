

# read contents of blakepoems.txt
# read line by line 
# splits the text into words
# word boundary everything that is not a letter
# everything that is lower case
# build a dictionary with every word
# counts how many time is the word occuring in the text


import os
import string
from collections import Counter

# load text
filename = "text-files\\blakepoems.txt"
file = open(filename, 'rt')
text = file.read()
file.close()

# split into words by white space
words = text.split()

# convert to lower case
words = [word.lower() for word in words]
# remove punctuation from each word

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
vals = Counter(stripped)

print(newDic)
