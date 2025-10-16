def get_input() -> str:
    with open('input.txt', 'r') as fd:
        return fd.read().strip()


def main():
    input = get_input()

    ans = 0
    for i in input:
        if i == 'B':
            ans += 1
        elif i == 'C':
            ans += 3

    print(ans)


if __name__ == "__main__":
    main()