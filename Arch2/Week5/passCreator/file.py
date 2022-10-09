from random import randint


def generate_random_password():
    randLen = randint(7, 10)
    password = []
    for _ in range(0, randLen+1):
        char = chr(randint(33, 127))
        password.append(char)
    return ''.join(password)


if __name__ == '__main__':
    print(generate_random_password())
