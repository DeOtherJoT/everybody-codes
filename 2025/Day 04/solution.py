import math


def get_input(filename: str, flag: int) -> list[int]:
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    if flag == 1:
        return [int(line) for line in lines]
    return lines


def part_1():
    gears = get_input('input_1.txt', 1)
    ratio = 1
    for index in range(len(gears) - 1):
        ratio *= gears[index] / gears[index + 1]
    print(int(ratio * 2025))


def part_2():
    gears = get_input('input_2.txt', 1)
    ratio = 1
    for index in range(len(gears) - 1):
        ratio *= gears[index] / gears[index + 1]
    print(math.ceil(10000000000000 / ratio))


def part_3():
    gears = get_input('input_3.txt', 2)
    ratio = int(gears[0]) / int(gears[1].split('|')[0])
    for index in range(1, len(gears) - 1):
        ratio *= int(gears[index].split('|')[1]) / int(gears[index + 1].split('|')[0])
    
    print(int(ratio * 100))


if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()