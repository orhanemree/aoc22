input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def create_sets_from_pairs(pairs: list) -> list:
    for p in pairs:
        if not p: continue
        first, second = p.split(",")
        f_start, f_end = first.split("-")
        s_start, s_end = second.split("-")
        f = set(i for i in range(int(f_start), int(f_end)+1))
        s = set(i for i in range(int(s_start), int(s_end)+1))
        yield [f, s]


def part1():
    contains_other = 0
    
    pairs = get_input(input_file).split("\n")
    sets = create_sets_from_pairs(pairs)
    while sets:
        try:
            f, s = next(sets)
            if f.issuperset(s) or s.issuperset(f):
                contains_other += 1
        except StopIteration:
            break
    
    return contains_other
    

def part2():
    overlaps = 0
    
    pairs = get_input(input_file).split("\n")
    sets = create_sets_from_pairs(pairs)
    while sets:
        try:
            f, s = next(sets)
            if len(f.intersection(s)) > 0:
                overlaps += 1
        except StopIteration:
            break
        
    return overlaps


def main():
    print(part1()) # 538
    print(part2()) # 792

        
if __name__ == "__main__":
    main()