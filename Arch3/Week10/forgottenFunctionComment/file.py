def check_comment(lines: dict, fileName: str) -> str:
    textFile = ''
    for key, val in lines.items():
        if 'def' in val.split() and (lines[key - 1].find('#') if key != 1 else key == 1):
            textFile += '# todo: add comment to this function \n'
        textFile += val
    return textFile


def main(newFile='testfile.txt', file='python1.py'):
    try:
        with open(file, 'rt') as pyFile:
            dictLine = {k + 1: v for k, v in enumerate(pyFile)}
        with open(newFile, 'w') as newPyFile:
            newPyFile.writelines(check_comment(dictLine, pyFile.name))
    except (OSError, IOError):
        print('invalid')


if __name__ == "__main__":
    main(newFile=input(), file=input())