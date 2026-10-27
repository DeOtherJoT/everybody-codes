def get_input() -> list[list[int]]:
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
    lines = [[int(x) for x in line.split(' ')] for line in lines]

    ret = []
    for col in range(len(lines[0])):
        ret.append([lines[row][col] for row in range(len(lines))])
    return ret


def begin_round(knight_lines: list[list[int]], round) -> list[list[int]]:
        


def print_result(knight_lines: list[list[int]]) -> None:
    firsts = [line[0] for line in knight_lines]
    print(''.join(str(x) for x in firsts))


def main():
    knight_lines = get_input()
    num_rounds = 1

    for round in range(num_rounds):
        knight_lines = begin_round(knight_lines, round)
        print_result(knight_lines)


if __name__ == "__main__":
    main()