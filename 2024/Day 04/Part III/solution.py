def get_input():
    with open('input.txt', 'r') as fd:
        return [int(line) for line in fd.read().splitlines()]


def main():
    input_list = get_input()

    median = sorted(input_list)[len(input_list) // 2]

    total_strikes = sum(abs(x - median) for x in input_list)
    print(total_strikes)


if __name__ == "__main__":
    main()