# 1.	Unix-based operating systems usually include a tool named head. It displays the first 10 lines of a file whose name is provided as a command line parameter. 
# Write a Python program that provides the same behavior. Display an appropriate error message if the file requested by the user does not exist or if the command line parameter is omitted.
import sys
import os

def main():
    with open(os.path.join(sys.path[0], 'randomtext.txt'), 'rt') as ft:
        ft = ft.readlines()
    #try: 
    #    ft = open(os.path.join(sys.path[0], 'randomtext.txt'), newline='', encoding='utf8').readlines()
    #except (IOError, OSError):
    #    print('invalid')
        count = 0
        while (count <= 10):
            if not ft[count] in ('\r', '\n', '\r\n'):
                print(ft[count])
            count+=1

if __name__ == "__main__":
    main()