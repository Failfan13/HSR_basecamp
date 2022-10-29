import os
from re import search
import sys
import csv

def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))
        '''for line in file_content:
            pos = file_content.index(line)
            file_content.pop(pos)
            file_content.insert(pos, [detail for detail in line if detail != ''])'''
        file_content.pop(0)
    return file_content


def get_headers(file : list):
    return [l[0] for l in file]

def search_by_type(file:list, type):
    return list(filter(lambda x: (x[1].lower() == type) ,file))

def search_by_director(file:list, director):
    return list(filter(lambda x: (x[3].lower().find(director.lower()) >= 0) ,file))

def get_directors(file:list):
    return [{l[3]} for l in file if l[3] != '']

def alphabetic_director():
    print('bruh')
    return

def main():
    exit = False
    while exit == False:
        inp = input('''[1] Print the amount of TV Shows
[2] Print the amount of Movies
[3] Print the (full) names of directors in alphabetical order who lead both tv shows and movies.
    (for example, search the name David Ayer. He is the director of three movies and one tv show)
[4] Print the name of each director in alphabetical order, 
    the number of movies and the number of tv shows (s)he was the director of. 
    Use a tuple with format: (director name, number of movies, number of tv shows) to print.
''')
        if inp == '1':
            print(len(search_by_type(load_csv_file('netflix_titles.csv'), 'tv show')))
        elif inp == '2':
            print(len(search_by_type(load_csv_file('netflix_titles.csv'), 'movie')))
        elif inp == '3':
            print(search_by_director(load_csv_file('netflix_titles.csv'), 'david ayer'))
        elif inp == '4':
            print(alphabetic_director())
        exit = True


if __name__ == "__main__":
    main()
    