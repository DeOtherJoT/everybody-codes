def get_input() -> tuple[list[str], list[str]]:
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
    runes = lines[0].split(':')[1].split(',')
    sentences = lines[2:]

    return runes, sentences


def start_op(word: str, runes: list[str], is_seen: list[str]) -> list[str]:
    for rune in runes:
        idx = 0
        while True:
            idx = word.find(rune, idx)
            if idx == -1:
                break
            # print(f'Found {rune} in {word} at {idx}')
            for i in range(idx, idx + len(rune)):
                is_seen[i] = '1'
            idx += 1

    return is_seen


def main():
    runes, sentences = get_input()

    # print(f'Runes: {runes}')
    # print(f'Sentences: {sentences}')

    runes_rev = [rune[::-1] for rune in runes]
    # print(f'Reversed Runes: {runes_rev}')
    total = 0
    for sentence in sentences:
        is_seen = ['0'] * len(sentence)
        is_seen = start_op(sentence, runes, is_seen)
        # print(f'After forward pass: {"".join(is_seen)}')
        is_seen = start_op(sentence, runes_rev, is_seen)
        # print(f'After backward pass: {"".join(is_seen)}')
        total += is_seen.count('1')
        
    print(total)


if __name__ == "__main__":
    main()