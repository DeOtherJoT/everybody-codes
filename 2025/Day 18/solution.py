import re


def get_input(filename: str, flag: int) -> list[str]:
    with open(filename, 'r') as fd:
        if flag == 1:
            return fd.read().split('\n\n')
        elif flag == 2:
            steps, in_data = fd.read().split('\n\n\n')
            return steps.split('\n\n'), in_data.split('\n')


def process_block(block: str, tree: dict) -> dict:
    lines = block.splitlines()
    plant, thickness = list(map(int, re.findall(r'\d+', lines[0])))
    incoming_energy = 0
    for line in lines[1::]:
        if 'free' in line:
            incoming_energy += 1
        else:
            source_plant, branch_thickness = list(map(int, re.findall(r'\d+', line)))
            incoming_energy += tree.get(source_plant, 0) * branch_thickness
    if thickness > incoming_energy:
        tree[plant] = 0
    else:
        tree[plant] = incoming_energy
    return tree


def part_1():
    input_lst = get_input('input.txt', 1)
    # print(input_lst)
    marker = len(input_lst)
    tree = {}
    for block in input_lst:
        tree = process_block(block, tree)
    print(tree[marker])


def process_block2(block: str, tree: dict, in_bin: list[int]) -> dict:
    lines = block.splitlines()
    plant, thickness = list(map(int, re.findall(r'\d+', lines[0])))
    incoming_energy = 0
    for line in lines[1::]:
        if 'free' in line:
            if in_bin[plant - 1] == 1:
                incoming_energy += 1
            else:
                incoming_energy += 0
        else:
            source_plant, branch_thickness = list(map(int, re.findall(r'-?\d+', line)))
            incoming_energy += tree.get(source_plant, 0) * branch_thickness
    if thickness > incoming_energy:
        tree[plant] = 0
    else:
        tree[plant] = incoming_energy
    return tree


def part_2():
    plant_lst, in_data = get_input('input.txt', 2)
    total = 0
    marker = len(plant_lst)

    for line in in_data:
        tree = {}
        in_bin = list(map(int, line.split(' ')))
        for block in plant_lst:
            tree = process_block2(block, tree, in_bin)
        print(tree[marker])
        total += tree[marker]
    print(total)


if __name__ == "__main__":
    # part_1()
    part_2()