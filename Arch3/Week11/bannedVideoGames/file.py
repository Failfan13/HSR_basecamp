import sys
import os
import csv

headers = ['Id', 'Game', 'Series', 'Country', 'Details', 'Ban Category', 'Ban Status', 
'Wikipedia Profile', 'Image', 'Summary', 'Developer', 'Publisher', 'Genre', 'Homepage']


class BannedGames():
    def __init__(self, file: str = 'bannedvideogames.csv', headers=headers) -> None:
        self.file = file
        self.data = readCsv(self.file)
        self.listCountry = [data.get('Country') for data in self.data]
        self.headers = headers

    def assignmentsRead(self) -> None:
        listCountry = []
        isIsrael = 0
        isMostBanned = ''
        isBannedGermany = []
        isAssasinsCreed = 0
        isRedDeadCountry = []
        for data in self.data:
            if data.get('Country') == 'Israel':
                isIsrael += 1
            if data.get('Country') == 'Germany':
                isBannedGermany.append((data.get('Game'), data.get('Details')))
            if data.get('Series').find('Assasins Creed') >= 0:
                if not data.get('Series') in isAssasinsCreed:
                    isAssasinsCreed += 1
            if data.get('Series').find('Red Dead Redemption') >= 0:
                isRedDeadCountry.append(data.get('Country'))
        listCountry = self.listCountry
        isMostBanned = max(set(listCountry), key=listCountry.count)
        print(f"({isIsrael}) ({isMostBanned}) ({isAssasinsCreed}) {tuple(isBannedGermany)} ({isRedDeadCountry})")
            
    def assignmentsWrite(self) -> None:
        for i, data in enumerate(self.data):
            if data.get('Series').find('Silent Hill VI') >= 0:
                self.data[i]['Series'].replace('Silent Hill VI', 'Silent Hill Remastered')
            if data.get('Series').find('Bully') >= 0:
                self.data[i]['Ban Status'] = 'Ban Lifted'
            if data.get('Series').find('Manhunt II') >= 0:
                self.data[i]['Genre'] = 'Action'

        self.data = [data for data in self.data if not data.get('Country') == 'Germany']
        writeCsv(self.file, self.data)
            
    def addGame(self) -> None:
        newDict = {k.title():input(f'fill in: {k}') for k in self.headers}
        self.data.append(newDict)
        writeCsv(self.file, self.data)

    def listGame(self) -> None:
        singleCountry = set(self.listCountry)
        print(''.join(str(f'({c} - {self.listCountry.count(c)})') for c in singleCountry))

    def searchGame(self, inp) -> None:
        details = ''
        for data in self.data:
            if data.get('Country') == inp:
                details += f"{data.get('Game')} - {data.get('Details')}\n"
        print(details)


def writeCsv(file, data) -> None:
    with open(os.path.join(sys.path[0], file), mode='w', newline='', encoding='UTF-8') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for dict in data:
            writer.writerow(dict)


def readCsv(file) -> None:
    with open(os.path.join(sys.path[0], file), mode='r', encoding='UTF-8') as csvFile:
        dna = list(csv.DictReader(csvFile))
        return dna


def main() -> None:
    banGames = BannedGames()
    print("[I] Print request info from assignment")
    print("[M] Make modification based on assignment")
    print("[A] Add new game to list")
    print("[O] Overview of banned games per country")
    print("[S] Search the dataset by country")
    print("[Q] Quit program")
    while True:
        questInp = input('Your Choice?').upper()
        if questInp == 'I':
            banGames.assignmentsRead()
        elif questInp == 'M':
            banGames.assignmentsWrite()
        elif questInp == 'A':
            banGames.addGame()
        elif questInp == 'O':
            banGames.listGame()
        elif questInp == 'S':
            banGames.searchGame(input('search for country?'))
        elif questInp == 'Q':
            break
        else:
            print('Invalid')
    

if __name__ == "__main__":
    main()