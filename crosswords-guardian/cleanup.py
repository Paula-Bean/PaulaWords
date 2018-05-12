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

'''
for word in sorted(words):
    # if len(words[word]) == 4:
    print word
    for clue in words[word]:
        print " ", clue
    print
'''


if 1:
    with codecs.open("guardian-puzzlewords.txt", "wb", "utf8") as f:
        for word in sorted(words):
            f.write(word + "\n")
            for clue in sorted(words[word]):
                f.write("  " + clue + "\n")
            f.write("\n")
