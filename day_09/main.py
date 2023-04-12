input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def position_knot(px: int, py: int, x: int, y: int) -> tuple:
    x_new = x
    y_new = y
    
    # check if tail is touching head
    if not ((x <= px+1) and (x >= px-1) and \
        (y <= py+1) and (y >= py-1)):
        if px == x:
            y_new = (py+y)//2
        elif py == y:
            x_new = (px+x)//2
        else:
            if px > x:
                x_new += 1
            else: 
                x_new -= 1
            if py > y:
                y_new += 1
            else:
                y_new -= 1

    return x_new, y_new


def calculate_tail_visited(input_: str, knots: list) -> list:
    tail_visited = set()
    
    cmds = input_.strip().split("\n")
    for cmd in cmds:
        direction, step = cmd.split(" ")
        
        # position head
        for i in range(int(step)):
            if direction == "U":
                # up
                knots[0][1] -= 1
            elif direction == "R":
                # right
                knots[0][0] += 1
            elif direction == "D":
                # down
                knots[0][1] += 1
            elif direction == "L":
                # left
                knots[0][0] -= 1
                
            # position every knot according to its parent knot
            for knot in range(1, len(knots)):
                knots[knot][0], knots[knot][1] = position_knot(knots[knot-1][0], knots[knot-1][1], knots[knot][0], knots[knot][1])
            
            # save position of tail
            tail_visited.add((knots[-1][0], knots[-1][1]))
        
    return len(tail_visited)


def part1():
    knot_count = 2
    knots = [[0, 0] for _ in range(knot_count)]
    
    tail_visited = calculate_tail_visited(get_input(input_file), knots)
    
    return tail_visited


def part2():
    knot_count = 10
    knots = [[0, 0] for _ in range(knot_count)]
    
    tail_visited = calculate_tail_visited(get_input(input_file), knots)
    
    return tail_visited


def main():
    print(part1()) # 6098
    print(part2()) # 2597

        
if __name__ == "__main__":
    main()