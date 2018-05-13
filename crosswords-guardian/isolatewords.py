import codecs

words = set()

for line in codecs.open("guardian-puzzlewords.txt", "rb", "utf8"):
    line = line.rstrip()
    if not line:
        continue
    if line[0] == " ":
        continue
    words.add(line.strip().upper())

if 0:
    with codecs.open("puzzlewords.txt", "wb", "utf8") as f:
        for word in sorted(words):
            f.write(word + "\n")

if 1:
    import random
    words = list(words)
    random.shuffle(words)
    with codecs.open("puzzlewords.js", "wb", "utf8") as f:
        f.write("puzzlewords = [")
        for word in words:
            f.write("\n\"" + word + "\",")
        f.seek(-1, 1)
        f.write("\n];\n")
