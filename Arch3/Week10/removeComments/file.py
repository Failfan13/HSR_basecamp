def main(fileName: str) -> None:
    for file in fileName.split(', '):
        try:
            with open(file, 'rt') as fileText:
                text = []
                for index, line in enumerate(fileText):
                    if ((line.split()[0] if len(line.split()) != 0 else '') == 'def'):
                        if (text[index - 1].find('#') if index != 0 else True):
                            print(f'''File: {file} contains a function [{line.split()[1][:-1]}]
on line [{index + 1}] without a preceding comment.''')
                    text.append(line)
        except (IOError, OSError):
            print('invalid')


if __name__ == "__main__":
    main(fileName=input())
