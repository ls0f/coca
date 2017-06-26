#! coding:utf-8

import json

words = {}
with open("20000.txt") as f:
    for line in f:
        i, word = line.split()
        words[word.decode('latin-1')] = int(i)

with open("static/20000.js", "w") as f:
    f.write("var WORDS=%s" % json.dumps(words))
