def get_input() -> list[int]:
    with open('input.txt', 'r') as fd:
        return [int(x) for x in fd.read().split(',')]


def part_1(columns: int = 90, spells = None):
    if spells is not None:
        in_list = spells
    else:
        in_list = get_input()
    # print(in_list)

    total = 0
    # print("In part 1")
    # print(in_list)
    for elem in in_list:
        total += columns // elem
    
    return(total)


def display_wall(built_wall: list[int]):
    max_height = max(built_wall)
    width = len(built_wall)

    for level in range(max_height, 0, -1):
        line = ''
        for w in range(width):
            if built_wall[w] >= level:
                line += '#'
            else:
                line += ' '
        print(line)
    # temp = [x for x in range(width)]
    # print(''.join([str((x + 1) % 10) for x in temp]))
    # print(width)


def get_spell_slot(built_wall: list[int]) -> int:
    for idx, height in enumerate(built_wall):
        if height == 0:
            continue
        return idx + 1


def part_2():
    built_wall = get_input()
    # display_wall(built_wall)
    width = len(built_wall)
    spell: list[int] = []
    while sum(built_wall) > 0:
        # display_wall(built_wall)
        # print('---')
        spell_slot = get_spell_slot(built_wall)
        spell.append(spell_slot)
        for idx in range(spell_slot - 1, width, spell_slot):
            if built_wall[idx] > 0:
                built_wall[idx] -= 1
    
    print('Spell:', spell)
    # ans = 1
    # for s in spell:
    #     ans *= s
    # print('Answer:', ans) 
    return spell


def part_3():
    # built_wall = get_input()
    spell = part_2()

    BLOCKS = 202520252025000

    start = 0
    end = 202520252025000
    while start < end:
        mid = (start + end) // 2
        result = part_1(mid, spells=spell)
        if result == BLOCKS:
            break
        elif result < BLOCKS:
            start = mid + 1
        else:
            end = mid - 1
    print('Minimum columns:', mid - 1)





if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()