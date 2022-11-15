import sys
import os
import time

def main():
    ft = open(os.path.join(sys.path[0], 'randomtext.txt'), newline='', encoding='utf-8').readlines()
    #while '\r\n' in ft:
        #ft.remove('\r\n')
    '''
    start1 = time.time()
    for line in ft[-10:]:
        print(line)
    end1 = time.time()
    print(end1 - start1)
    '''
    '''
    start2 = time.time()
    count = 0
    for line in ft:
        if count >= len(ft)-10:
            print(line)
        count +=1
    end2 = time.time()
    print(end2 - start2)
    '''


if __name__ == "__main__":
    main()