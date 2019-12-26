#!/usr/bin/env python3
#
# Read the file 'guardian-puzzlewords.txt' and produce two files with
# only the words (i.e., without the clues).            
#
# One file is a textual file 'puzzlewords.txt', and the other is 
# 'puzzlewords.js' which can be included in a web page or JavaScript
# program.

import codecs
import random

words = set()

for line in codecs.open("guardian-puzzlewords.txt", "rb", "utf8"):
    line = line.rstrip()
    if not line:
        continue
    if line[0] == " ":
        continue
    words.add(line.strip().upper())

with codecs.open("puzzlewords.txt", "wb", "utf8") as f:
    for word in sorted(words):
        f.write(word + "\n")

words = list(words)
random.shuffle(words)
with codecs.open("puzzlewords.js", "wb", "utf8") as f:
    f.write("puzzlewords = [")
    for word in words:
        f.write("\n\"" + word + "\",")
    f.seek(-1, 1) # Erase the last written comma.
    f.write("\n];\n")
