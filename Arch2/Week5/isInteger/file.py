

def is_integer(str):
    for i in str:
        if i.isdigit() is False:
            return False
    if len(str) < 1:
        return False
    return True


def remove_non_integer(str):
    num = ''
    for i in str:
        if ord(i) in range(48, 58) or ord(i) == 45:
            num += i
    if num[0] == '-' and num[1] == '0':
        num = num.replace('0', '')
    return num


if __name__ == '__main__':
    inp = input('enter a number')
    if is_integer(inp.replace(' ', '')) is not True:
        print('invalid')
    else:
        print('valid')

    print(remove_non_integer(inp))
