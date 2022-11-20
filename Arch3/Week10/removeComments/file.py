def main(fileName: str, file='randomtext.txt') -> None:
    try:
        with open(file, 'rt') as textFile:
            text = ''
            for line in textFile:
                if bool(line.find('#')):
                    text += line

        with open(fileName, 'w') as writeFile:
            writeFile.writelines(text)
    except (IOError, OSError):
        print('invalid')


if __name__ == "__main__":
    main(fileName=input(), file=input())