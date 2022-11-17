import sys
import os

def main(fileName: str) -> None:
    with open(os.path.join(sys.path[0], 'randomtext.txt'), 'r') as textFile:
        text = ''
        for line in textFile:
            if bool(line.find('#')):
                text += line

    with open(os.path.join(sys.path[0], fileName + '.txt'), 'w') as writeFile:
        writeFile.writelines(text)
        
if __name__ == "__main__":
    inp = input('new file name')
    main(inp)