import sys


def main(file=sys.argv[1]):
    try:
        with open(file, 'rt') as fileText:
            [print(line) for line in fileText.readlines()[-10:]]

            for index, line in enumerate(fileText):
                if index > len(fileText.readlines()) - 10:
                    print(line)

            print(''.join([line for line in fileText.readlines()[-10:]]))

    except (IOError, OSError):
        print('invalid')


if __name__ == "__main__":
    main()