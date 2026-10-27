def get_input(filename):
    with open(filename, 'r') as fd:
        return fd.read().strip()


def count_lower(arr: str, target: str) -> int:
    return sum([1 for x in arr if x == target])


def part_1():
    input = get_input("input_1.txt")

    processed = [x for x in input if x in "Aa"]
    res = 0
    # print(processed)
    for idx, alph in enumerate(processed):
        if alph == "A":
            res += count_lower(processed[idx + 1 :], 'a')
    print(res)


def part_2():
    input = get_input("input_2.txt")

    res = 0
    for idx, alph in enumerate(input):
        if alph in "ABC":
            res += count_lower(input[idx + 1 :], alph.lower())
    print(res)


def part_3():
    input_tents = get_input('input_3.txt')

    # print(len(input_tents))
    input_tents = input_tents * 1000
    res = 0
    for idx, alph in enumerate(input_tents):
        if alph in "abc":
            # take 1000 chars to the left and right
            left = input_tents[max(0, idx - 1000) : idx]
            right = input_tents[idx + 1 : idx + 1001]
            res += count_lower(left + right, alph.upper())
    print(res)


if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()