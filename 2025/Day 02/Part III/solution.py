def gen_grid(start: list[int]):
    grid = []
    for y in range(0, 1001):
        for x in range(0, 1001):
            grid.append([start[0] + (x * 1), start[1] + (y * 1)])

    return grid


def add_op(a: list[int], b: list[int]) -> list[int]:
    return [a[0] + b[0], a[1] + b[1]]


def div_op(a: list[int], b: list[int]) -> list[int]:
    return [int(a[0] / b[0]), int(a[1] / b[1])]


def mult_op(a: list[int], b: list[int]) -> list[int]:
    return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]


def main():
    A=[-79745,-16616]
    grid = gen_grid(A)
    total = 0
    lolbit = ""

    # print(f"last value: {grid[-1]}")
    for index, point in enumerate(grid):
        start = [0, 0]
        flag = True

        for _ in range(100):
            start = mult_op(start, start)
            start = div_op(start, [100000, 100000])
            start = add_op(start, point)
            if abs(start[0]) > 1000000 or abs(start[1]) > 1000000:
                flag = False
                lolbit += "."
                break

        if flag:
            total += 1
            lolbit += "x"

        # lolbit += ' '
        if (index) % 1001 == 0:
            lolbit += "\n"

    print(f"Total valid points: {total}")
    print(lolbit)

if __name__ == "__main__":
    main()