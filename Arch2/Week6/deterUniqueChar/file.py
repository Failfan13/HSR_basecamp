# inputs
dictionary = {chr(key): 0 for key in range(32, 127)}

set = {chr(key) for key in range(32, 127)}

# processor


def unique_chars_dict(inp, dict):
    if inp in dict.keys():
        dict[inp] = 1


def unique_chars_set(inp, set):
    if inp in set:
        set.remove(inp)


def total_unique(dict):
    unique_dict = 0
    for value in dict.values():
        if value != 0:
            unique_dict += 1

    print(unique_dict)
    print(95 - len(set))


# printer
if __name__ == "__main__":
    inp = input('choose a word')
    for char in inp:
        unique_chars_dict(char, dictionary)
        unique_chars_set(char, set)

total_unique(dictionary)
