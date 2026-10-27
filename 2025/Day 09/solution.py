def get_input(filename: str, flag: int) -> list[str]:
    with open(filename, 'r') as fd:
        lines = fd.read().splitlines()
    if flag == 1:
        return [x.split(':')[1] for x in lines]
    elif flag == 2:
        res = []
        for line in lines:
            id_no, seq = line.split(':')
            res.append({'id': int(id_no), 'seq': seq})
        return res
    else:
        pass


def is_child(child: str, par_1: str, par_2: str) -> bool:
    for i in range(len(child)):
        if child[i] not in (par_1[i], par_2[i]):
            return False
    return True


def get_child_idx(dnas: list[str]) -> int:
    for i in range(len(dnas)):
        # rotate dnas list
        rotated = dnas[i:] + dnas[:i]
        if is_child(rotated[0], rotated[1], rotated[2]):
            return i
    return -1


def get_score(child: str, parent: str) -> int:
    score = 0
    for i in range(len(child)):
        if child[i] == parent[i]:
            score += 1
    return score


def get_degree(dnas: list[str], child_idx: int) -> int:
    child = dnas[child_idx]
    par_1 = dnas[(child_idx + 1) % len(dnas)]
    par_2 = dnas[(child_idx + 2) % len(dnas)]

    # print(f'Child: {child}')
    # print(f'Parent 1: {par_1}')
    # print(f'Parent 2: {par_2}')

    degree = 0
    return get_score(child, par_1) * get_score(child, par_2)


def part_1():
    dnas = get_input('input.txt', 1)
    # print(dnas)

    child_idx = get_child_idx(dnas)
    # print(f'Child index: {child_idx}')
    degree = get_degree(dnas, child_idx)
    print(degree)


def part_2():
    dnas = get_input('input.txt', 2)

    total_degree = 0
    for i in range(len(dnas)):
        # rotate dnas list
        rotated = dnas[i:] + dnas[:i]
        # check if rotated[0] is child of every combination
        for x in range(1, len(rotated)):
            for y in range(x + 1, len(rotated)):
                if is_child(rotated[0]['seq'], rotated[x]['seq'], rotated[y]['seq']):
                    print("Found child ID:", rotated[0]['id'], "with parents IDs:", rotated[x]['id'], rotated[y]['id'])
                    degree = get_score(rotated[0]['seq'], rotated[x]['seq']) * get_score(rotated[0]['seq'], rotated[y]['seq'])
                    total_degree += degree
    
    print("Total degree sum:", total_degree)


def add_family(families: list[dict], child_id: int, par_1_id: int, par_2_id: int) -> list[set[int]]:
    curr_fam = set([child_id, par_1_id, par_2_id])
    if len(families) == 0:
        families.append(curr_fam)
        return families
    for family in families:
        if len(curr_fam.intersection(family)) > 0:
            family.update(curr_fam)
            return families
    families.append(curr_fam)
    return families


def part_3():
    dnas = get_input('input.txt', 2)

    families = []

    for i in range(len(dnas)):
        rotated = dnas[i:] + dnas[:i]
        for x in range(1, len(rotated)):
            for y in range(x + 1, len(rotated)):
                if is_child(rotated[0]['seq'], rotated[x]['seq'], rotated[y]['seq']):
                    families = add_family(families, rotated[0]['id'], rotated[x]['id'], rotated[y]['id'])

    changed = True
    while changed:
        changed = False
        new_families = []
        for family in families:
            merged = False
            for new_family in new_families:
                if len(family.intersection(new_family)) > 0:
                    new_family.update(family)
                    merged = True
                    changed = True
                    break
            if not merged:
                new_families.append(family)
        families = new_families
    print("Total families found:", len(families))
    # return sum of largest family
    fam_sizes = [len(fam) for fam in families]
    index = fam_sizes.index(max(fam_sizes))
    print(sum(families[index]))

if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()