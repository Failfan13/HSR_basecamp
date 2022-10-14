book_list = []
options = ['a', 's', 'e', 'add', 'search', 'exit']


def choices():
    inp = input('A = add book, S = Search book, E = Exit').lower()
    if inp in (options[0], options[3]):
        enter = input('please enter: title, author, publisher, date')
        return print(add_book(enter))
    elif inp in (options[1], options[4]):
        enter = input('please search term')
        return print(search_book(book_list, enter))
    elif inp in (options[2], options[5]):
        print('exit')
        return False
    else:
        print('invalid')
        return False


def add_book(book):
    book = book.replace(' ', '').split(',')
    if search_book(book_list, book[0]) is True:
        return 'invalid'
    book_list.append(
        {'title': book[0],
         'author': book[1],
         'publisher': book[2],
         'pub_date': book[3]})


def search_book(books, term):
    for dicts in books:
        if term in dicts.values():
            return True
    return False


if __name__ == "__main__":
    while choices() is None:
        i = 0
