
Scripts to scrape puzzlewords from The Guardian.

First, run `scrape.py` to download a set of puzzle pages and extract the puzzleworlds from them into 'guardian-puzzlewords-withsees.txt'. A puzzle which has been downloaded earlier will not be downloaded again.

Next, run `cleanup.py` to remove unwanted stuff from that file and produce 'guardian-puzzlewords.txt'.

Last, run `isolatewords.py` to digest the words into 'puzzlewords.txt' and 'puzzlewords.js', which can be included in the web page with the interactive crossword designer.

