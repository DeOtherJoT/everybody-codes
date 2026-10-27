def add_op(a: list[int], b: list[int]) -> list[int]:
    return [a[0] + b[0], a[1] + b[1]]


def div_op(a: list[int], b: list[int]) -> list[int]:
    return [a[0] // b[0], a[1] // b[1]]


def mult_op(a: list[int], b: list[int]) -> list[int]:
    return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]


def main():
    A = [152, 57]
    start = [0, 0]

    for _ in range(3):
        start = mult_op(start, start)
        start = div_op(start, [10, 10])
        start = add_op(start, A)

    print(f"Final result: {start}")


if __name__ == "__main__":
    main()