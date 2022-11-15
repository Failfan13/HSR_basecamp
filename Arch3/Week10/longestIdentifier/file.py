import sys
import os
import re

def main():
    with open(os.path.join(sys.path[0], 'randomtext.txt'), 'rt') as text:
        lines = text.readlines()
        text.close()
        longestWord = []
        for line in lines:
            line = re.compile('[,*\.!?]').sub('', line)
            longestWord.append(max(line.split(), key=lambda x: (len(x), x), default=''))
        print('The longest word is: ' + str(len(max(longestWord, key=len))))
        [print(i) for i in longestWord if len(i) == len(max(longestWord, key=len))]
        


if __name__ == "__main__":
    main()