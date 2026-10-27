def get_input(filename: str, flag: int):
    if flag == 1:
        with open(filename, 'r') as fd:
            data = fd.read()
        data = data.split(':')[1].split(',')
        return [int(x) for x in data]
    elif flag == 2:
        with open(filename, 'r') as fd:
            data = fd.read().splitlines()
        res = []
        for line in data:
            line = line.split(':')[1]
            res.append([int(x) for x in line.split(',')])
        return res
    else:
        with open(filename, 'r') as fd:
            data = fd.read().splitlines()
        return data


def is_filled(row: list[int]) -> bool:
    return (0 in row) == False


def insert_element(fishbone: list[list[int]], num: int) -> list[list[int]]:
    # print(f"Attempting to insert {num} into fishbone: {fishbone}")
    for index, row in enumerate(fishbone):
        if is_filled(row):
            continue
        if num < row[1] and row[0] == 0:
            row[0] = num
            # print(f"Inserted {num} to the left of {row[1]} in row {index}, fishbone: {fishbone}")
            return fishbone
        elif num > row[1] and row[2] == 0:
            row[2] = num
            # print(f"Inserted {num} to the right of {row[1]} in row {index}, fishbone: {fishbone}")
            return fishbone
        else:
            continue
            # print(f"Could not insert {num} in row {index}, moving to next row.")
    # print(f"All rows filled or could not insert {num}, creating new row.")
    fishbone.append([0, num, 0])
    return fishbone
        

def gen_fishbone(input: list[int]) -> list[list[int]]:
    fishbone: list[list[int]] = []
    for idx, num in enumerate(input):
        if idx == 0:
            fishbone.append([0, num, 0])
            continue
        fishbone = insert_element(fishbone, num)
    return fishbone


def part_1():
    input = get_input('input_1.txt', 1)
    fishbone = gen_fishbone(input)

    print(f"Spine: {'' .join([str(row[1]) for row in fishbone])}")


def part_2():
    input_list = get_input('input_2.txt', 2)
    spines = []
    for input in input_list:
        fishbone = gen_fishbone(input)
        spine = ''.join([str(row[1]) for row in fishbone])
        spines.append(int(spine))
    print(f"{max(spines)-min(spines)}")


def ret_rows(fishbone: list[list[int]]) -> list[int]:
    rows = []
    for row in fishbone:
        temp = [x for x in row if x != 0]
        rows.append(int(''.join([str(x) for x in temp])))
    return rows


def part_3():
    input_list = get_input('./yt/everybody_codes_e2025_q05_p3.txt', 3)
    processed = []
    for input in input_list:
        id_no, nums = input.split(':')
        id_no = int(id_no)
        nums = [int(x) for x in nums.split(',')]
        fishbone = gen_fishbone(nums)
        spine = int(''.join([str(row[1]) for row in fishbone]))
        joined_rows = ret_rows(fishbone)
        processed.append({
            'id': id_no,
            'spine': spine,
            'rows': joined_rows,
            'fishbone': fishbone
        })
        # print(f"{id_no:>4}:{spine:>16}:{':'.join([str(x) for x in joined_rows])}")
    processed = sorted(processed, key=lambda x: (x['spine'], x['rows'], x['id']), reverse=True)
    for x in processed:
        print(f"{x['id']:>4}:{x['spine']:>16}:{':'.join([str(y) for y in x['rows']])}")

    checksum = 0
    for idx, item in enumerate(processed):
        # print(f"Multiplying index {idx + 1} with ID {item['id']}")
        checksum += (idx + 1) * item['id']
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    part_3()