import sys
import os
import re

def main():
    with open(os.path.join(sys.path[0], 'randomtext.txt'), 'rt') as file:
        textFile = file.readlines()
        file.close()
        words = []
        wordDict = dict()
        [[words.append(w) for w in re.compile('[/.?@!*]').sub('', l).split()] for l in textFile]
        wordslist = {k:0 for k in words}
        print(wordslist)

if __name__ == "__main__":
    main()