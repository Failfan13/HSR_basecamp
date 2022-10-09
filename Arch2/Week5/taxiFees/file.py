

def calculate_fare(kilometers):
    base = 4
    plus = (kilometers / 0.14) * 0.25
    if base + round(plus, 2) > round((base + round(plus, 2)) * 4) / 4:
        base = round((base + round(plus, 2)) * 4) / 4 + 0.25

    return base


if __name__ == '__main__':
    inp = float(input('in kilometers'))
    print(calculate_fare(inp))
