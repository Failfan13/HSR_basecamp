MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', ' ': '  '}


def message_to_morse(inp):
    message = ''
    for char in inp:
        if char.upper() in MORSE_CODE_DICT.keys():
            message += MORSE_CODE_DICT[char.upper()]+' '
        else:
            message = f"Can't convert char [{char.upper()}] if there is no mapping for specific characters."
    return message


def morse_to_message(inp):
    message = ''
    inp = inp.split(' ')
    for char in inp:
        is_text = True
        for key, val in MORSE_CODE_DICT.items():
            if char == val:
                is_text = False
                message += key
        if is_text is True:
            message = f"Can't convert char [{char}] if there is no mapping for specific characters."
    return message


def translate_text(inp):
    is_morse = True
    for char in inp:
        if char not in ('-', '.', ' '):
            is_morse = False
    if is_morse is True:
        return morse_to_message(inp)
    else:
        return message_to_morse(inp)


if __name__ == "__main__":
    inp = input('Type your message')
    print(message_to_morse(inp))
    inp = input('Type your message')
    print(morse_to_message(inp))
    inp = input('Type your message')
    print(translate_text(inp))
