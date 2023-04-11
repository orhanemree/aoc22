input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def calculate_scenic_score(lines: list, x: int, y: int):
    col = len(lines[0])
    row = len(lines)
    max_ = int(lines[y][x])
    score = 1
    visible = 0
    
    # looking up
    for i in range(0, y):
        visible += 1
        if int(lines[y-i-1][x]) >= max_:
            break
    score *= visible
    visible = 0
            
    # looking right
    for i in range(x+1, col):
        visible += 1
        if int(lines[y][i]) >= max_:
            break
    score *= visible
    visible = 0
            
    # looking down
    for i in range(y+1, row):
        visible += 1
        if int(lines[i][x]) >= max_:
            break
    score *= visible
    visible = 0
    
    # looking left
    for i in range(0, x):
        visible += 1
        if int(lines[y][x-i-1]) >= max_:
            break
    score *= visible
            
    return score


def part1():
    lines = get_input(input_file).strip().split("\n")
    col = len(lines[0])
    row = len(lines)
    visible = []

    # top view
    for i in range(1, col-1):
        max_ = int(lines[0][i])
        for j in range(1, row-1):
            if int(lines[j][i]) > max_:
                max_ = int(lines[j][i])
                if (j, i) not in visible:
                    visible.append((j, i))
                
    # right view
    for i in range(1, row-1):
        max_ = int(lines[i][-1])
        for j in range(0, col-1):
            if int(lines[i][col-j-1]) > max_:
                max_ = int(lines[i][col-j-1])
                if (i, col-j-1) not in visible:
                    visible.append((i, col-j-1))
                    
    # bottom view
    for i in range(1, col-1):
        max_ = int(lines[-1][i])
        for j in range(1, row-1):
            if int(lines[row-j][i]) > max_:
                max_ = int(lines[row-j][i])
                if (row-j, i) not in visible:
                    visible.append((row-j, i))
                    
    # left view
    for i in range(1, row-1):
        max_ = int(lines[i][0])
        for j in range(0, col-1):
            if int(lines[i][j]) > max_:
                max_ = int(lines[i][j])
                if (i, j) not in visible:
                    visible.append((i, j))
            
    # trees inside the grid + edges + corners
    return len(visible) + 2*(col+row-4) + 4


def part2():
    max_scenic_score = 0
    
    lines = get_input(input_file).strip().split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            score = calculate_scenic_score(lines, col, row)
            max_scenic_score = score if score > max_scenic_score else max_scenic_score
            
    return max_scenic_score


def main():
    print(part1()) # 1543
    print(part2()) # 595080

        
if __name__ == "__main__":
    main()