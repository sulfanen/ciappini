#! /usr/bin/python
# encoding: utf-8
import sys  # interpreter stuff
from subprocess import call
from distances import edit_dist

TRESHOLD = 2

# Invalid chars
invalids = [" ", ",", ";", ".", "+", "!", "?", "£", "$", "%", "&", "(", ")", "[", "]", ":", "'"]
realInvalids = [" ", ",", ";", ".", "+", "!", "?", "£", "$", "%", "&", "(", ")", "[", "]", ":"]
invalidchars = "".join(invalids)


def getData(dataFiles):
    tokens = {}
    numberOfWords = 0.0;
    # For each file, for each word store them in a dictionary alongside the frequency
    for file in dataFiles:
        with open(file) as f:
            for line in f:
                # Separate the word by space, lowercase them
                for word in line.upper().swapcase().split(" "):
                    numberOfWords += 1
                    word = word.translate(None, invalidchars)
                    if tokens.__contains__(word):
                        tokens[word] = (tokens[word]) + 1
                    else:
                        tokens[word] = 1
        f.close()
    # Compute the frequency
    for key in tokens:
        tokens[key] = (tokens[key])/numberOfWords;
    return tokens, numberOfWords;

# Starting from a word w, from a token list t with a number of total analized words nW try to guess the closest match
def guess(t, w):
    out = []
    for key in t.iterkeys():
        dist = edit_dist(key, w)
        if dist <= TRESHOLD:
            out += [(key, t[key], dist)]
    return prettify(out)

# Ordinare? Al momento produce solamente una stringa leggibile (molto brutto)
# TODO: ordinare lista per edit_dis -> probabilità -> altro?
def prettify(out):
    outStr = "[\n"
    for i in range(len(out)):
        outStr += "\t" + str(out[i]) + "\n"
    return outStr + "]"

# Main
if __name__ == "__main__":
    assert(len(sys.argv) >= 2)
    tokens, numberOfWords = getData(sys.argv[1:])
    print("Token found: {}".format(numberOfWords))
    # print(tokens)
    print("Ready to guess\n")
    while True:
        w = raw_input("> ")
        print("{} -> {}".format(w, guess(tokens, w)))
