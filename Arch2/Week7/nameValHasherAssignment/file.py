hashmap_key_value = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, key: str = None) -> str:
    return ''.join([key[str] for str in data.upper()])


def decode_string(data: str, key: str = None) -> str:
    return ''.join([''.join([i for i in key if key[i] == str]) for str in data.upper()])


def encode_list(data: list, key: str = None) -> list:
    return list(map(lambda x: encode_string(x, key), data))


def decode_list(data: list, key: str = None) -> list:
    return list(map(lambda x: decode_string(x, key), data))

def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    enc = True
    dec = True
    for char in decoded:
        if char not in key.keys():
            enc = False
            break
    for char in encoded:
        if char not in key.values():
            dec = False
            break
    return 'true' if True is enc and dec else 'false'

def set_hashmap(key: str) -> None:
    if len(key.replace(' ', ''))%2 == 0:
        return {i: key[key.index(i)+1] for i in key[0:len(key):2]}
    else:
        print('Invalid hashvalue input')
        return 
    


def main():
    exit = False
    hash = set_hashmap(input('hashmap'))
    while exit is False and hash is not None:
        inp = input('''[E] Encode value to hashed value
[D] Decode hashed value to normal value
[P] Print all encoded/decoded values
[V] Validate 2 values against eachother
[Q] Quit program''').lower()
        if inp == 'e':
            text = input('your string').split(', ')
            if len(text) > 1:
                for x in encode_list(text, hash):
                    print(x)
            else:
                print(encode_string(text[0], hash))
        elif inp == 'd':
            text = input('your string').split(', ')
            if len(text) > 1:
                for x in decode_list(text, hash):
                    print(x)
            else:
                print(decode_string(text[0], hash))
        elif inp == 'p':
            for dec, enc in encode_string(input('your string'), hash):
                print(dec)
        elif inp == 'v':
            inp1 = input('encoded')
            inp2 = input('decoded')
            print(validate_values(inp1, inp2, hash))
        elif inp == 'q':
            exit = True
        break


if __name__ == "__main__":
    main()