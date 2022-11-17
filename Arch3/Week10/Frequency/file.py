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
        for word in words:
            if word in wordDict.keys():
                wordDict[word.lower()] += 1
            else:
                wordDict[word.lower()] = 1
        
        print(wordDict)

if __name__ == "__main__":
    main()