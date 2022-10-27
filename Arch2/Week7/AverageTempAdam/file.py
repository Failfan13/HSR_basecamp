import calendar
import os
import sys

def load_txt_file(file_name):
    file_content = {}
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        temps = []
        years = set()
        for line in file_obj.readlines():
            line=line.split()
            if line[1] == '1' and len(temps) > 1:
                monthtemps = temps.copy()
                temps.clear()
                if line[2] not in years:
                    years.add(line[2])
                    file_content.update({line[2]: {}})
                if int(line[0])-1 == 0:
                    prev_year = list(file_content.keys())[list(file_content.keys()).index(line[2])-1]
                    file_content[prev_year].update({12: monthtemps})
                else:
                    file_content[line[2]].update({int(line[0])-1: monthtemps})
            temps.append(line[3])
    return file_content


def fahrenheit_to_celcius(fahrenheit: float):
    return ((fahrenheit - 32) * 5) / 9


def average_temp_per_year(temp: dict):
    return [(y, sum(sum(float(c) for c in i) for i in [temp[y][m] for m in temp[y]])/365) for y in temp]


def average_temp_per_month(temp: dict):
    return [[(a,sum(float(c) for c in b)/len(b)) for a,b in i.items()] for i in [temp[y] for y in temp]]


def main():
    exit = False
    while exit == False:
        inp = input('''[1] average temperatures per year (fahrenheit)
[2] average temperatures per year (celsius)
[3] warmest and coldest year
[4] warmest month of a year
[5] coldest month of a year
[6] list of tuples ''')
        if inp == '1':
            print(average_temp_per_year(load_txt_file('NLAMSTDM.txt')))
        elif inp == '2':
            func = average_temp_per_year(load_txt_file('NLAMSTDM.txt'))
            print([(a,b*5//9) for a,b in func])
        elif inp == '3':
            temp = average_temp_per_year(load_txt_file('NLAMSTDM.txt'))
            temps = list(map(lambda x: x[1], temp))
            print(temp[temps.index(max(temps))][0], max(temps))
            print(temp[temps.index(min(temps))][0], min(temps))
        elif inp in ('4', '5'):
            temp = average_temp_per_month(load_txt_file('NLAMSTDM.txt'))
            inp = input('what year?')
            temps = [m[1] for m in temp[int(inp) - 1995]]
            if inp == '4':
                print(calendar.month_name[temps.index(max(temps))])
            else:
                print(calendar.month_name[temps.index(min(temps))])
        elif inp == '6':
            temp = load_txt_file('NLAMSTDM.txt')
            print([(i, {a: [round((float(b)*5) /9, 2) for b in temp[i][a]] for a in temp[i]}) for i in temp])
        else:
            print('invalid')
            exit = True

if __name__ == "__main__":
    main()