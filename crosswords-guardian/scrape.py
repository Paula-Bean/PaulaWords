#!/usr/bin/env python3
# encoding: utf8

# Harvest 'Quick Crossword' puzzle words (and clues) from The Guardian
#
# On Dec 26, 2019, Puzzle 14979 was current:
#
#   https://www.theguardian.com/crosswords/quick/15486
#
# Puzzles lower than 9093 don't seem to exist.
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
                    
# Which range of puzzles you want to scrape. Currently this can range from
# 9093 to 15486, though you might want to limit these numbers when testing
# and developing, because scraping them all takes a long time.

first = 9093
last = 15486
    
# first, last = 9093, 9095
# first, last = 15484, 15486
  

if not os.path.exists("pages"):
    os.mkdir("pages")


print("Downloading...")
for nr in range(first, last + 1):
    url = "https://www.theguardian.com/crosswords/quick/%d" % nr
    try:
        with urllib.request.urlopen(url) as resp:
           html = resp.read()
    except urllib.error.HTTPError:
        print(f"    {nr} doesn't seem to exist")
        continue
    fn = "pages/%d" % nr
    if not os.path.exists(fn):
        with open(fn, "wb") as f:
            f.write(html)
            print(f"    {nr} downloaded")
    else:
        print(f"    {nr} already exists")
            

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
