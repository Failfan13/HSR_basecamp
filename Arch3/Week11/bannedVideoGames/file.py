import sys
import os
import csv

class BannedGames():
    def __init__(self, file: str = 'bannedvideogames.csv') -> None:
        self.file = file
        self.data = readCsv(self.file)


def readCsv(file):
    with open(os.path.join(sys.path[0], file), mode='r', encoding='UTF-8') as csvFile:
        dna = list(csv.DictReader(csvFile))
        print(dna[0])

# {'Id': '50 Cent: Bulletproof - Australia', 'Game': '50 Cent: Bulletproof', 
# 'Series': '50 Cent: Bulletproof', 'Country': 'Australia', 'Details': 
# 'Banned due to high impact gory violence.\nA censored version was later released.', 
# 'Ban Category': 'Graphic Violence and Cruelty', 'Ban Status': 'Censored Version Released', 
# 'Wikipedia Profile': 'https://en.wikipedia.org/wiki/50_Cent:_Bulletproof', 
# 'Image': '//upload.wikimedia.org/wikipedia/en/2/28/50_Cent_Bulletproof.jpg', 
# 'Summary': '50 Cent: Bulletproof is a video game for the PlayStation 2 and Xbox consoles. 
# 50 Cent: Bulletproof was reworked into a PlayStation Portable version and titled 50 Cent: Bulletproof G Unit Edition, 
# with a top-down perspective. A sequel, 50 Cent: Blood on the Sand, was released on February 24, 2009 for PlayStation 3 
# and Xbox 360.The story revolves around protagonist hip hop musician 50 Cent\'s search for vengeance against the hitmen 
# who attempted to murder him. The game features members of the G-Unit rap crew as a gang. Dr. Dre plays an arms dealer, 
# Eminem plays a corrupt police officer, and DJ Whoo Kid plays himself as a person selling "bootlegged" music (of the G-Unit camp) 
# out of his trunk. A soundtrack album titled, Bulletproof, was released by DJ Red Heat\'s Shadyville Entertainment. It won "Best Original Song" 
# in the 2005 Spike TV Video Game Awards.', 
# 'Developer': 'Interscope Records|High Voltage|Genuine Games', 
# 'Publisher': 'Sierra|Vivendi Games', 
# 'Genre': 'Action', 'Homepage': ''}

def main() -> None:
    banGames = BannedGames()
    print(banGames.data)
    # print("[I] Print request info")
    # print("[M] Make modification")
    # print("[A] Add game")
    # print("[O] Overview of banned games per country")
    # print("[Q] Quit program")
    # questInp = input('Your Choice?').upper()
    # while True:
    #     if questInp == 'I':
    #         ...
    #     elif questInp == 'M':
    #         ...
    #     elif questInp == 'A':
    #         ...
    #     elif questInp == 'O':
    #         ...
    #     elif questInp == 'Q':
    #         break
    #     else:
    #         print('Invalid')
    


if __name__ == "__main__":
    main()