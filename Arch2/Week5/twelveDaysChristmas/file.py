def christmas_verse(day):
    verse_order = []
    repeat_text = (
        'A partridge in a pear tree',
        'Two turtle doves',
        'Three french hens',
        'Four calling birds',
        'Five golden rings',
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
            verse += ', and'
        verse += '\n'
        verse_order.insert(0, verse)
    return ''.join(verse_order)

if __name__=='__main__':
    for i in range(1, 13):
        print(christmas_verse(i))
        