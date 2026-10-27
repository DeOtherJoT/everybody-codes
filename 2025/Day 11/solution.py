def get_input(filename) -> list[int]:
    with open(filename, 'r') as fd:
        return [int(x) for x in fd.read().splitlines()]


def run_phase_1(columns: list[int]) -> list[int]:
    for idx in range(len(columns) - 1):
        if columns[idx] > columns[idx + 1]:
            columns[idx] -= 1
            columns[idx + 1] += 1
    return columns


def check_phase(columns: list[int]) -> bool:
    for idx in range(len(columns) - 1):
        if columns[idx] > columns[idx + 1]:
            return True
    return False


def run_phase_2(columns: list[int]) -> list[int]:
    for idx in range(len(columns) - 1):
        if columns[idx] < columns[idx + 1]:
            columns[idx] += 1
            columns[idx + 1] -= 1
    return columns


def ret_checksum(columns: list[int]) -> int:
    ret = 0
    for idx, val in enumerate(columns):
        ret += (idx + 1) * val
    return ret


def part_1():
    columns = get_input('input.txt')
    phase_1 = True

    # print(columns)
    for round in range(10):
        print(f"{round}: {columns}")
        if phase_1:
            columns = run_phase_1(columns)
            phase_1 = check_phase(columns)
        else:
            columns = run_phase_2(columns)
    print(ret_checksum(columns))


def is_equilibrium(columns: list[int]) -> bool:
    for idx in range(len(columns) - 1):
        if columns[idx] != columns[idx + 1]:
            return False
    return True


def part_2():
    columns = get_input('input.txt')
    phase_1 = True

    rounds = 0
    # print(check_phase(columns))
    while True:
        # print(f"{rounds}: {columns}")
        if phase_1:
            phase_1 = check_phase(columns)
            if phase_1:
                continue
            columns = run_phase_1(columns)
        else:
            columns = run_phase_2(columns)
        rounds += 1
        if is_equilibrium(columns):
            break
    print(rounds)


def part_3():
    columns = get_input('input.txt')
    avrg = sum(columns) // len(columns)
    print(sum(abs(x - avrg) for x in columns if x < avrg))


if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()