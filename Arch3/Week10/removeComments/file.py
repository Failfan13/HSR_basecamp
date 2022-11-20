def main(fileName: str) -> None:
    with open(fileName, 'rt') as fileText:
        text = []
        for index, line in enumerate(fileText):
            if ((line.split()[0] if len(line.split()) != 0 else '') == 'def' and 
                    (text[index - 1].find('#') if index != 0 else True)):
                print(f'''File: {fileName} contains a function [{line.split()[1][:-1]}] 
on line [{index + 1}] without a preceding comment.''')
            text.append(line)

# split input ', ' for loop each file.

# try catch error IO OS


if __name__ == "__main__":
    main(fileName='randomtext.txt')