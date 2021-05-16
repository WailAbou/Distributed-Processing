import sys
from helper import *


previous_word_key = None
previous_word_value = None  
language_count = { language: 0 for language in languages } 

for line in sys.stdin:
    line = line.strip()
    word_key, word_value = line.split('\t', 1)
    language_count[word_value] += 1

print(language_count)
