points_rule = { "X": 1, "Y": 2, "Z": 3, "lost": 0, "draw": 3, "won": 6 }

input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def calculate_point(opp: str, us: str) -> int:
    state = ""

    if opp == "A":
        if us == "X":
            state = "draw"
        elif us == "Y":
            state = "won"
        elif us == "Z":
            state = "lost"
            
    elif opp == "B":
        if us == "X":
            state = "lost"
        elif us == "Y":
            state = "draw"
        elif us == "Z":
            state = "won"
            
    elif opp == "C":
        if us == "X":
            state = "won"
        elif us == "Y":
            state = "lost"
        elif us == "Z":
            state = "draw"

    return points_rule[us] + points_rule[state]


def part1():
    total_point = 0
    
    rounds = get_input(input_file).split("\n")
    for r in rounds:
        if not r: continue
        opp, us = r.split(" ")
        total_point += calculate_point(opp, us)
        
    return total_point


def part2():
    total_point = 0
    
    rounds = get_input(input_file).split("\n")
    for r in rounds:
        if not r: continue
        opp, ending = r.split(" ")
        us = ""
        
        if opp == "A":
            if ending == "X":
                us = "Z"
            elif ending == "Y":
                us = "X"
            elif ending == "Z":
                us = "Y"
                
        elif opp == "B":
            if ending == "X":
                us = "X"
            elif ending == "Y":
                us = "Y"
            elif ending == "Z":
                us = "Z"
                
        elif opp == "C":
            if ending == "X":
                us = "Y"
            elif ending == "Y":
                us = "Z"
            elif ending == "Z":
                us = "X"

        total_point += calculate_point(opp, us)
        
    return total_point
        

def main():
    print(part1()) # 12645
    print(part2()) # 11756

        
if __name__ == "__main__":
    main()