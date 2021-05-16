import sys
from helper import *


language_count = { language: 0 for language in languages } 

# Looping trough all the input lines and reducing it into a dictionary
for line in sys.stdin:
    line = line.strip()
    word_key, word_value = line.split('\t', 1)
    language_count[word_value] += 1

print(language_count)
