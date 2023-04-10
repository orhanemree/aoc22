input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def detect_nth_distinct(inp: str, n: int) -> int:
    index = 0
    
    for i in range(len(inp)):
        if len(set(inp[i:i+n])) == n:
            index = i+n
            break
        
    return index


def part1():
    inp = get_input(input_file)
    start_of_packet = detect_nth_distinct(inp, 4)
    
    return start_of_packet


def part2():
    inp = get_input(input_file)
    start_of_message = detect_nth_distinct(inp, 14)
    
    return start_of_message


def main():
    print(part1()) # 1640
    print(part2()) # 3613

        
if __name__ == "__main__":
    main()