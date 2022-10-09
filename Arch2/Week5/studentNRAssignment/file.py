
import os
import sys

valid_lines = []
corrupt_lines = []


def validate_data(line):
    invalid = []
    corrupt = False
    data = line.split(',')
    studentNr = validate_studentNr(data[0])
    name = validate_name(data[1], data[2])
    date = validate_date(data[3])
    program = validate_program(data[4])
    func = [studentNr, name, date, program]
    for var in func:
        if var is not None:
            invalid.append(var)
            corrupt = True
    if corrupt is not True:
        valid_lines.append(line)
    else:
        text = ' => INVALID DATA: '
        corrupt_lines.append(line + text + str(invalid))


def validate_name(first, last):
    name = [first, last]
    for name in name:
        if len(name) < 1:
            return name
        else:
            for char in name:
                if (
                    char.isalpha() is not True
                        and char.isspace() is not True):
                    return name


def validate_studentNr(num):
    if len(num) != 7:
        return num
    elif num[:2] not in ('08', '09'):
        return num


def validate_date(date):
    try:
        datum = date.split('-')
        if int(datum[0]) not in range(1960, 2005):
            return date
        if int(datum[1]) not in range(1, 13):
            return date
        if int(datum[2]) not in range(1, 32):
            return date
    except ValueError:
        return date


def validate_program(val):
    if val not in ('INF', 'TINF', 'CMD', 'AI'):
        return val


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')
