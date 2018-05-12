#!/usr/bin/env python3
# encoding: utf8

# Harvest 'Quick Crossword' puzzle words (and clues) from The Guardian
#
# Fri 11 May 2018, Puzzle 14979 is current:
#
#   https://www.theguardian.com/crosswords/quick/14979
#
# Puzzles lower than 10000 don't seem to exist.
#
# There are also other puzzle types, ex. https://www.theguardian.com/crosswords/cryptic/27506


from bs4 import BeautifulSoup
import json
import re
import os
import glob
import collections
import urllib.request, urllib.error
import codecs
   
if not os.path.exists("pages"):
    os.mkdir("pages")
    
# Download phase
if 0:
    print("Downloading...")
    for nr in range(14979, 15000):
        print(f"    {nr}")
        url = "https://www.theguardian.com/crosswords/quick/%d" % nr
        try:
            with urllib.request.urlopen(url) as resp:
               html = resp.read()
        except urllib.error.HTTPError:
            print("not found")
            continue
        fn = "pages/%d" % nr
        if not os.path.exists(fn):
            with open(fn, "wb") as f:
                f.write(html)

# Parse & collect
words = collections.defaultdict(set) # Mapping from word -> set of clues

reparentheses = re.compile("(.*) \((.*)\)")

print("Parsing...")
for fn in glob.glob("pages/*"):
    print(fn)
    data = open(fn, "rb").read()
    soup = BeautifulSoup(data, "html.parser")
    div = soup.find("div", "js-crossword")
    data = div["data-crossword-data"]
    d = json.loads(data)
    for entry in d["entries"]:
        word = entry["solution"].strip()
        clue = entry["clue"].strip()
        '''
        # TODO: Some clues also contain HTML tags: cleanup        
        # TODO: multiword clues/word skip?
        # TODO: anagram skip?
        # TODO: some words contain only spaces?
        # TODO: clues like 'See 12' can be skipped
        # TODO: some words only have a clue like 'See 13'
        # All the above things can also be done by the consumer of the output file.
        
        m = reparentheses.match(clue)
        if m:
            clue = m.group(1)
            lengts = m.group(2)
            if "-" in lengths or "," in lengths: ...
            if "(anag)" in clue:
        '''
        words[word].add(clue)

with codecs.open("guardian-puzzlewords-withsees.txt", "wb", "utf8") as f:
    for word in sorted(words):
        f.write(word + "\n")
        for clue in words[word]:
            f.write("  " + clue + "\n")
        f.write("\n")
    

