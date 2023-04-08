from string import ascii_letters

input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return  f.read()


get_prioritie_of_char = lambda c: ascii_letters.index(c)+1


def part1():
    total_prioritie = 0
    
    lines = get_input(input_file).split("\n")
    for l in lines:
        if not l: continue
        first, second = set(l[:len(l)//2]), set(l[len(l)//2:])
        common = first.intersection(second)
        total_prioritie += get_prioritie_of_char(common.pop())

    print(total_prioritie) # 8394
    

def part2():
    total_prioritie = 0
    
    lines = get_input(input_file).split("\n")
    groups = [[set(lines[i*3]), set(lines[i*3+1]), set(lines[i*3+2])] for i in range(len(lines)//3)]
    for g in groups:
        badge = g[0].intersection(g[1].intersection(g[2]))
        total_prioritie += get_prioritie_of_char(badge.pop())
        
    print(total_prioritie) # 2413


def main():
    part1()
    part2()

        
if __name__ == "__main__":
    main()