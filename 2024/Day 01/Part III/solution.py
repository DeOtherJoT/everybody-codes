def get_input() -> str:
    with open("input.txt", "r") as file:
        return file.read().strip()


def group_up(input: str) -> list[str]:
    return [input[i : i + 3] for i in range(0, len(input), 3)]


def main():
    input = get_input()

    groups = group_up(input)

    keys = {
        'x': 0,
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 5
    }

    total = 0
    for group in groups:

        x_count = group.count('x')
        # print(f"Group: {group}, x_count: {x_count}")

        if x_count == 0:
            total += sum(keys[c] for c in group) + 6
        elif x_count == 1:
            total += sum(keys[c] for c in group) + 2
        else:
            total += sum(keys[c] for c in group)
    print (total)


if __name__ == "__main__":
    main()