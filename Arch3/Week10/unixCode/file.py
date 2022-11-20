import sys


def main(file=sys.argv[1]):
    try:
        with open(file, 'rt') as fileText:
            fileText = [line for line in fileText if line != '\n']
            print(''.join([l for i, l in enumerate(fileText) if i <= 10]))
    except (OSError, IOError):
        print('invalid')


if __name__ == "__main__":
    main()
