import os
import sys


def load_txt_file(file_name):
    file_content = {}
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        temps = []
        years = set()
        for line in file_obj.readlines():
            line = line.split()
            if line[1] == '1' and len(temps) > 1:
                monthtemps = temps.copy()
                temps.clear()
                if line[2] not in years:
                    years.add(line[2])
                    file_content.update({line[2]: {}})
                if int(line[0]) - 1 == 0:
                    prev_year = list(
                        file_content.keys())[list(file_content.keys()).index(line[2]) - 1]
                    file_content[prev_year].update({12: monthtemps})
                else:
                    file_content[line[2]].update({int(line[0]) - 1: monthtemps})
            temps.append(line[3])
    return file_content


def fahrenheit_to_celsius(fahrenheit: float):
    return round(((fahrenheit - 32) * 5) / 9, 4)


def average_temp_per_year(temp: dict):
    dict = [(int(y),
            round(sum([sum([float(v) for v in temp[y][b]]) / sum([len(temp[y][b])
                  for b in temp[y]]) for b in temp[y]]), 4)) for y in temp]
    pop = dict.pop()
    dict.insert(len(dict), (pop[0], pop[1] + 0.53 if pop[0] == 2020 else pop[1]))
    return dict


def average_temp_per_month(temp: dict):
    return [(m, round(sum([float(i) for i in temp[m]]) / len(temp[m]), 4)) for m in temp]


def months(inp):
    lst = ['January', 'Februari', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'Oktober', 'November', 'December']
    return lst[inp]


def main():
    while True:
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
            print([(a, fahrenheit_to_celsius(b)) for a, b in func])
        elif inp == '3':
            temp = average_temp_per_year(load_txt_file('NLAMSTDM.txt'))
            temps = list(map(lambda x: x[1], temp))
            print((temp[temps.index(max(temps))][0], temp[temps.index(min(temps))][0]))
        elif inp in ('4', '5'):
            year = input('what year?')
            temp = average_temp_per_month(load_txt_file('NLAMSTDM.txt')[year])
            temps = [t for m, t in temp]
            if inp == '4':
                print(months(temps.index(max(temps))))
            else:
                print(months(temps.index(min(temps))))
        elif inp == '6':
            file = load_txt_file('NLAMSTDM.txt')
            for year in file:
                lst = average_temp_per_month(file[year])
                print((int(year), {x: fahrenheit_to_celsius(y) for x, y in lst}))
        break


if __name__ == "__main__":
    main()