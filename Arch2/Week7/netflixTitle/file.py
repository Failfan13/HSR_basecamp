import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))
    return file_content


def get_headers(file: list):
    return file[0]


def search_by_type(file: list, type):
    return list(filter(lambda x: (x[1].lower() == type.lower()), file))


def search_by_director(file: list, director):
    return list(filter(lambda x: (x[3].lower().find(director.lower()) >= 0), file))


def get_directors(file: list):
    return [dir[3] for dir in file if dir[3] != '']


def all_directors(inp):
    lst = []
    lst2 = []
    file = load_csv_file('netflix_titles.csv')
    for dir in get_directors(load_csv_file('netflix_titles.csv')):
        for dir in dir.split(', '):
            has_tv = 0
            has_movie = 0
            for job in file:
                if dir in job:
                    if job[1] == 'Movie':
                        has_movie += 1
                    if job[1] == 'TV Show':
                        has_tv += 1
            if inp == '3':
                if (0 != has_tv and has_movie) and dir not in lst:
                    lst.append(dir)
            else:
                if dir not in lst and (0 != has_tv or has_movie):
                    lst.append(dir)
                    lst2.append((dir, has_movie, has_tv))
    if inp == '4':
        lst2.sort(key=lambda x: x[0])
        return lst2
    else:
        lst.sort()
        return lst


def main():
    while True:
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
            print(all_directors(inp))
        elif inp == '4':
            print(all_directors(inp))
        break


if __name__ == "__main__":
    main()