import os
import sys


def check_comment(lines: dict, fileName: str) -> list:
    for key, val in lines.items():
        val = val.split()
        if 'def' in val and lines[key-1].find('#'):
            return [key, val[val.index('def')+1], fileName]


def main():
    with open(os.path.join(sys.path[0], 'python.py'), 'r') as pyFile:
        dictLine = {k+1:v for k,v in enumerate(pyFile)}
        print(check_comment(dictLine, pyFile.name))

if __name__ == "__main__":
    main()