import os
import sys


def check_comment(lines: dict, fileName: str) -> str:
    textFile = ''
    for key, val in lines.items():
        if 'def' in val.split() and lines[key-1].find('#'):
            textFile += '# todo: add comment to this function \n'
        textFile += val
    return textFile


def main():
    try:
        with open(os.path.join(sys.path[0], 'python1.py'), 'r') as pyFile:
            dictLine = {k+1:v for k,v in enumerate(pyFile)}

        with open(os.path.join(sys.path[0], 'new.py'), 'x') as newPyFile:
            newPyFile.writelines(check_comment(dictLine, pyFile.name))

    except (OSError, IOError):
        print('invalid file')

if __name__ == "__main__":
    main()