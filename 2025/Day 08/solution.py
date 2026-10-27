def get_input(filename) -> list[int]:
    with open(filename, 'r') as fd:
        return [int(x) for x in fd.read().strip().split(',')]
        

def part_1():
    NAILS = 32
    MIDPOINT = NAILS // 2

    thread_data = get_input('input_1.txt')
    # print(thread_data)
    res = 0
    for idx in range(len(thread_data) - 1):
        if abs(thread_data[idx] - thread_data[idx + 1]) == MIDPOINT:
            res += 1
    print(res)


def num_inters(new_point, connections) -> int:
    res = 0
    x1, y1 = new_point
    for conn in connections:
        x2, y2 = conn
        if (x1 < x2 < y1 < y2) or (x2 < x1 < y2 < y1):
            res += 1
    return res


def part_2():
    points = get_input('input_2.txt')
    connections = []
    connections.append(sorted([points[0], points[1]]))

    # print(connections)
    res = 0

    for idx in range(1, len(points) - 1):
        new_point = sorted([points[idx], points[idx + 1]])
        res += num_inters(new_point, connections)
        connections.append(new_point)
    
    print(res)


def part_3():
    points = get_input('input_3.txt')
    connections = []

    for idx in range(len(points) - 1):
        new_point = sorted([points[idx], points[idx + 1]])
        connections.append(new_point)

    highest_inters = 0

    for x in range(256):
        for y in range(x + 1, 256):
            new_point = [x + 1, y + 1]
            inters = num_inters(new_point, connections)
            inters += sum([1 for con in connections if con == new_point])
            highest_inters = max(highest_inters, inters)
    print(highest_inters)



if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()