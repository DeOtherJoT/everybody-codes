def get_input() -> list[int]:
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
    return [int(line) for line in lines]


def main():
    input_list = get_input()
    
    minimum = min(input_list)
    diff = [(num - minimum) for num in input_list]
    print(sum(diff))


if __name__ == "__main__":
    main()