# inputs
dictionary = dict({chr(key): 0 for key in range(32, 127)})

set = set({chr(key) for key in range(32, 127)})

# processor


def unique_chars_dict(inp):
    for char in inp:
        if char in dictionary.keys():
            dictionary[char] = 1
        unique_dict = 0
    for value in dictionary.values():
        if value != 0:
            unique_dict += 1
    print(unique_dict)
    return unique_dict


def unique_chars_set(inp):
    for char in inp:
        if char in set:
            set.remove(char)
    print(95 - len(set))
    return 95 - len(set)


def total_unique(dict, set):
    print(lendict)
    print(lenset)


# printer
if __name__ == "__main__":
    inp = input('choose a word')
    lendict = unique_chars_dict(inp)
    lenset = unique_chars_set(inp)

    total_unique(lendict, lenset)
