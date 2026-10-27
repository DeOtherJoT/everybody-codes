def get_input(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, 'r') as fd:
        lines = fd.read().splitlines()

    names = lines[0].split(',')
    rules = lines[2:]

    return names, rules


def process_rules(in_list: list[str]) -> dict[str, list]:
    res = {}
    for item in in_list:
        subject, rule = item.split(' > ')
        res[subject] = rule.split(',')
    return res


def validate_name(name: str, rules: dict) -> bool:
    flag = True

    for idx in range(len(name) - 1):
        if name[idx + 1] not in rules[name[idx]]:
            return False
    return True


def part_1():
    names, rules = get_input('input_1.txt')
    
    rules = process_rules(rules)
    # print(rules)
    for name in names:
        flag = validate_name(name, rules)
        if flag == True:
            print(f"{name} has been validated")

            
def part_2():
    names, rules = get_input('input_2.txt')

    rules = process_rules(rules)
    res = 0
    for idx, name in enumerate(names):
        if validate_name(name, rules):
            res += (idx + 1)
    print(res)


def create_names(base: str, rules: dict) -> set[str]:
    created = set()

    if len(base) >= 7 and len(base) <= 11:
        created.add(base)
    elif len(base) > 11:
        return created
    
    for extend in rules.get(base[-1], []):
        created |= create_names(base + extend, rules)
    return created


def part_3():
    names, rules = get_input('input_3.txt')
    rules = process_rules(rules)
    # print(rules)
    # return
    seen_names = set()
    for name in names:
        if validate_name(name, rules):
            seen_names |= create_names(name, rules)
    print(len(seen_names))


if __name__ == "__main__":
    # part_1()
    # part_2()
    part_3()