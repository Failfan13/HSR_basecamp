def next_verse(day):
    verse_order = []
    repeat_text = (
        'A partridge in a pear tree',
        'Two turtledoves',
        'Three french hens',
        'Four calling birds',
        'five gold rings (five golden rings)',
        'Six geese a-laying',
        'Seven swans a-swimming',
        'Eight maids a-milking',
        'Nine ladies dancing',
        'Ten lords a-leaping',
        'Eleven pipers piping',
        'Twelve drummers drumming')
    for i in range(day):
        verse = repeat_text[i]
        if i == 1:
            day = 'nd'
            verse += ' And '
        elif i == 0:
            day = 'st'
        else:
            verse += ', '
            day = 'nd'
        verse_order.insert(0, verse)
        text = f'on the {i+1}{day} day of christmas, my true love sent to me '
    return text + ''.join(verse_order)


if __name__ == '__main__':
    for i in range(1, 13):
        print(next_verse(i))
