input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def part1():
    register_x = 1
    cycle = 0
    control_points = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0
    
    cmds = get_input(input_file).strip().split("\n")
    
    for cmd in cmds:
        cycle += 1
        if cycle in control_points:
            total_signal_strength += cycle*register_x
            
        if cmd == "noop": continue
        else:
            # it is a addx command
            cycle += 1
            if cycle in control_points:
                total_signal_strength += cycle*register_x
                
            val = cmd.split(" ")[1]
            register_x += int(val)
    
    return total_signal_strength


def part2():
    register_x = 1
    cycle = 0
    sprite_position = [0, 1, 2]
    crt = ""
    
    cmds = get_input(input_file).strip().split("\n")
    
    for cmd in cmds:
        cycle += 1
        crt += "#" if (cycle%40)-1 in sprite_position else "."
        if cycle%40 == 0:
            crt += "\n"
            
        if cmd == "noop": continue
        else:
            # it is a addx command
            cycle += 1
            crt += "#" if (cycle%40)-1 in sprite_position else "."
            if cycle%40 == 0:
                crt += "\n"

            val = cmd.split(" ")[1]
            register_x += int(val)
            sprite_position[0] = register_x-1
            sprite_position[1] = register_x
            sprite_position[2] = register_x+1
            
    return crt


def main():
    print(part1()) # 14540
    print(part2()) # EHZFZHCZ
    """
    ####.#..#.####.####.####.#..#..##..#####
    #....#..#....#.#.......#.#..#.#..#....#.
    ###..####...#..###....#..####.#......#..
    #....#..#..#...#.....#...#..#.#.....#..#
    #....#..#.#....#....#....#..#.#..#.#....
    ####.#..#.####.#....####.#..#..##..####.
    """

        
if __name__ == "__main__":
    main()