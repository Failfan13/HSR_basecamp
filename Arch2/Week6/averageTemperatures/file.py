temperature = [
    ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5',
                   '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5', '42.0', '46.5', '46.2',
                   '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2',
                   '38.5', '40.5', '47.0']),
    ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2',
                   '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7', '42.6', '44.8', '50.3',
                   '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2',
                   '49.6', '50.1', '43.6']),
    ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9',
                   '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9', '45.3', '46.6', '49.7',
                   '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5',
                   '40.7', '39.5', '40.6']),
]


def temp_check(temps):
    day = 0
    averageTot = [0]
    highestYear = [0]
    average9510 = 0
    average9520 = 0
    while day < len(temps[0][2]):
        if round(float(temps[0][2][day]) - float(temps[1][2][day])) in range(-4, 4):
            average9510 += 1
        if round(float(temps[0][2][day]) - float(temps[2][2][day])) in range(-5, 6):
            average9520 += 1
        day += 1
    for year in temps:
        warmth = 0
        for days in year[2]:
            if float(days) > highestYear[0]:
                highestYear = [float(days), year[0]]
            warmth += float(days)
        if warmth > averageTot[0]:
            averageTot = [warmth, year[0]]

    print(average9510)
    print(average9520)
    print(highestYear[1])
    print(averageTot[1])
    return


if __name__ == "__main__":
    temp_check(temperature)
