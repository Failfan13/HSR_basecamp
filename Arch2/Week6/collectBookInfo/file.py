book_list = []
options = ['a', 's', 'e', 'add', 'search', 'exit']


def choices():
    inp = input('A = add book, S = Search book, E = Exit').lower()
    if inp in (options[0], options[3]):
        enter = input('please enter: title, author, publisher, date')
        add_book(enter)
        return
    elif inp in (options[1], options[4]):
        enter = input('please search term')
        search_book(book_list, enter)
    elif inp in (options[2], options[5]):
        print('exit')
        return False
    else:
        print('invalid')
        return False


def add_book(book):
    book = book.split(',')
    if search_book(book_list, book[0]) is True:
        return 'invalid'
    book_list.append(
        {'title': book[0],
         'author': book[1],
         'publisher': book[2],
         'pub_date': book[3]})
    for books in book_list:
        print(books)
    return book_list


def search_book(books, term):
    for dicts in books:
        if term in dicts.values():
            print('yes')
            return print('True')
    print('no')
    return print('False')


if __name__ == "__main__":
    while choices() is None:
        i = 0
