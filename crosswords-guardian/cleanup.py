#!/usr/bin/env python3
#
# Reads the file 'guardian-puzzlewords-withsees.txt' and removes unwanted
# material from it, combines clues when multiple clues for a word are
# present, and writes the result to 'guardian-puzzlewords.txt'.
#
# Words can have one or more clues:
#
# ACCREDITATION
#   Granting of recognition (13)
#
# ACCREDITED
#   Certified officially (10)
#
# ACCRUE
#   Accumulate (6)
#   Gather (6)
#   Grow by addition (6)
#

import codecs
import collections
import re

resee = re.compile(".*See \d")
words = collections.defaultdict(set)

currentword = ""

for line in codecs.open("guardian-puzzlewords-withsees.txt", "rb", "utf8"):
    line = line.rstrip()
    if not line:
        continue
    if resee.match(line): # Skip clues like "See 1 down"
        continue
    if line[0] == " ":
        clue = line.strip()
        words[currentword].add(clue)
    else:
        currentword = line.strip()

with codecs.open("guardian-puzzlewords.txt", "wb", "utf8") as f:
    for word in sorted(words):
        f.write(word + "\n")
        for clue in sorted(words[word]):
            f.write("  " + clue + "\n")
        f.write("\n")
