import string


def main(file='randomtext.txt'):
    try:
        with open(file, 'rt') as fileText:
            words = []
            wordDict = dict()
            [[words.append(word.translate(str.maketrans('', '', string.punctuation)).lower())
                for word in line.split()] for line in fileText]
            for word in words:
                if word in wordDict.keys():
                    wordDict[word.lower()] += 1
                else:
                    wordDict[word.lower()] = 1
            highest = max(wordDict.values())
            lowest = min(wordDict.values())
            print(' '.join([k for k, v in wordDict.items() if v == highest]))
            print(' '.join([k for k, v in wordDict.items() if v == lowest]))
    except (IOError, OSError):
        print('invlaid')


if __name__ == "__main__":
    main(file=input())