from random import randint
import time


def arithmetic_operation(arithmetic_type):
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    if arithmetic_type == 'multiplication':
        return [num1 * num2, f'{num1} * {num2}']
    elif arithmetic_type == 'subtraction':
        return [num1 - num2, f'{num1} - {num2}']
    elif arithmetic_type == 'summation':
        return [num1 + num2, f'{num1} + {num2}']
    else:
        print('invalid')


def calc_table(question):
    print(question)
    print(question[1])
    start = time.time()
    inp_ans = int(input('What is the awnser?'))
    end = time.time()
    if inp_ans != question[0]:
        ans = 'wrong'
    else:
        ans = 'correct'
    return (question[1], ans, round(end - start, 2))


def time_element(element):
    return element[2]


if __name__ == '__main__':

    inp = input('arithmetic type')
    output = []
    for _ in range(0, 10):
        output.append(calc_table(arithmetic_operation(inp)))

output.sort(key=time_element)
print(output)
