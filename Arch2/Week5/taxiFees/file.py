def calculate_fare(kilometers):
    base = 4
    plus =  (kilometers / 0.14) * 0.25
    return (base + round(plus, 2))

if __name__=='__main__':
    inp = int(input('in kilometers'))
    print(calculate_fare(inp))