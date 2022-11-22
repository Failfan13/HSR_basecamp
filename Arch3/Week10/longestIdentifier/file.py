def main(file='randomtext.txt'):
    try:
        with open(file, 'rt') as text:
            longestWord = []
            for line in text:
                longestWord.append(max(line.split(), key=lambda x: (len(x), x), default=''))
            print(' '.join([i for i in longestWord if len(i) == len(max(longestWord, key=len))]))
    except (IOError, OSError):
        print('invalid')


if __name__ == "__main__":
    main(file=input())