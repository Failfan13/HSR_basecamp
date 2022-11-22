def check_comment(lines: dict, fileName: str) -> str:
    textFile = ''
    for key, val in lines.items():
        if val.find('#') >= 0:
            textFile += ''
        else:
            textFile += val
    return textFile


def main(newFile='testfile.txt', file='python1.py'):
    try:
        with open(file, 'rt') as pyFile:
            dictLine = {k + 1: v for k, v in enumerate(pyFile)}
        with open(newFile, 'wt') as newPyFile:
            newPyFile.writelines(check_comment(dictLine, pyFile.name))
    except (OSError, IOError):
        print('invalid')


if __name__ == "__main__":
    main(file=input(), newFile=input())