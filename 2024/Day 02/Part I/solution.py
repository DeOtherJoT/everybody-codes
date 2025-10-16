def get_input() -> tuple[list[str], list[str]]:
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    runes = lines[0].split(':')[1].split(',')
    words = lines[2].split(' ')

    return runes, words


def main():
    runes, words = get_input()

    total = 0
    for word in words:
        for rune in runes:
            if rune in word:
                total += 1
    
    print(total)
    

if __name__ == "__main__":
    main()