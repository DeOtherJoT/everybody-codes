def get_input(filename: str) -> str:
    with open(filename, 'r') as fd:
        return fd.read()


def sort_and_unique(numlist: list[int]) -> list[int]:
    numlist.sort(reverse=True)
    unique = []
    [unique.append(x) for x in numlist if x not in unique]
    return unique


def part_1():
    input = get_input('input_1.txt')

    input = [int(x) for x in input.split(',')]
    cleaned = sort_and_unique(input)
    print(sum(cleaned))


def part_2():
    input = get_input('input_2.txt')

    cleaned = sort_and_unique([int(x) for x in input.split(',')])
    print(sum(cleaned[-20:]))


def pop_set(numlist: list[int]) -> list[int]:
    unique = []
    [unique.append(x) for x in numlist if x not in unique]
    for x in unique:
        numlist.pop(numlist.index(x))
    return numlist


def part_3():
    input = get_input('input_3.txt')
    sets_made = 0

    cleaned = [int(x) for x in input.split(',')]
    cleaned.sort(reverse=True)
    while (len(cleaned) > 0):
        sets_made += 1
        cleaned = pop_set(cleaned) 
    print(sets_made)


if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()