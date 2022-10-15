def pass_check():
    password = set({})
    valid = False
    tries = 0
    while valid is False and tries <= 3:
        inp = input('your password?')
        for char in inp:
            password.add(char)

        upp = False
        low = False
        num = False
        spe = False

        for char in password:
            if char in ('*', '@', '!', '?'):
                spe = True
            elif ord(char) in range(65, 91):
                upp = True
            elif ord(char) in range(97, 123):
                low = True
            elif ord(char) in range(48, 58):
                num = True

        if True is upp and low and num and spe:
            valid = True
            return print('valid')
        else:
            valid = False
            tries += 1
            print('invalid')
    return


if __name__ == '__main__':
    pass_check()
