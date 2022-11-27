import sys
import os
import json

class Movies:
    def __init__(self, file: str = 'movies.json') -> None:
        self.file = file
        self.list = readJson(self.file)


    def showInfo(self) -> None:
        line = ''
        movie2004 = 0
        movieScience = 0
        movieKeau = ''
        movieSylve = ''
        for dict in self.list:
            #text = f"(title= {dict.get('title')}, year= {dict.get('year')}, cast= {dict.get('cast')}, genres= {dict.get('genres')})"
            text = f"(title: {dict.get('title')})"
            line += text
            if dict.get('year') == 2004:
                movie2004 += 1
            if str(dict.get('genres')).find('Science Fiction') >= 0:
                movieScience += 1
            if str(dict.get('cast')).find('Keanu Reeves') >= 0:
                movieKeau += text
            if str(dict.get('cast')).find('Sylvester') >= 0 and int(dict.get('year')) in range(1995, 2006):
                movieSylve += text
                
        print(movie2004, movieScience, movieKeau, movieSylve)


    def modification(self) -> None:
        lowest = min(self.list, key=lambda x: x.get('year')).get('year')
        for i, dict in enumerate(self.list):
            if dict.get('title') == "Gladiator":
                self.list[i]['year'] = 2001
            if dict.get('year') == lowest:
                self.list[i]['year'] = self.list[i]['year'] - 1
            if str(dict.get('cast')).find('Natalie Portman') >= 0:
                self.list[i]['cast'] = list(map(lambda x: x.replace('Natalie Portman', 'Nat Portman'), self.list[i]['cast']))
            if str(dict.get('cast')).find('Kevin Spacey') >= 0:
                self.list[i]['cast'].remove('Kevin Spacey')
        
        writeJson(self.file, self.list)

    
    def change(self, inp) -> None:
        nameInp = input('New movie name')
        dateInp = input('New release year')
        for i, dict in enumerate(self.list):
            if dict.get('title') == inp:
                if not nameInp.replace(' ', '') == '':
                    self.list[i]['title'] = nameInp.title()
                if not dateInp.replace(' ', '') == '':
                    self.list[i]['year'] = int(dateInp)
        
        writeJson(self.file, self.list)


    def search(self, inp) -> dict:
        for dict in self.list:
            if inp in dict.values():
                return dict


def readJson(file) -> list:
    with open(os.path.join(sys.path[0], file), mode='r',encoding='UTF-8') as file:
        return json.load(file)


def writeJson(file, text) -> None:
    with open(os.path.join(sys.path[0], file), mode='w') as file:
        json.dump(text, file, indent=4)


def main() -> None:
    MList = Movies()
    while True:
        print("[I] Movie information overview")
        print("[M] Make modification based on assignment")
        print("[S] Search a movie title ")
        print("[C] Change title and/or release year by search on title")
        print("[Q] Quit program")
        inp = input().upper()

        if inp == 'I':
            MList.showInfo()
        elif inp == 'M':
            MList.modification()
        elif inp == 'S':
            inp = input('search')
            print(MList.search(inp=inp))
        elif inp == 'C':
            inp = input('Movie name')
            MList.change(inp=inp)
        elif inp == 'Q':
            break
        else:
            print('Invalid')


if __name__ == '__main__':
    main()