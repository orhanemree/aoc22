input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def create_stack_table(crates: list) -> dict:
    crates.reverse()
    stack = {}
    
    for c in crates:
        for i in range((len(crates[0])+1)//4):
            val = c[i*3+1+i].strip()
            if not val: continue
            if type(stack.get(str(i+1))) != list:
                stack[str(i+1)] = []
            stack[str(i+1)].append(val)
            
    return stack


def part1():
    crates, procedure = get_input(input_file).split("\n\n", 1)
    crates = crates.rsplit("\n", 1)[0].split("\n")
    
    # create stack as dictionary from given input as text
    stack = create_stack_table(crates)
    
    # apply the procedure step by step
    for p in procedure.split("\n"):
        if not p: continue
        _, count, _, from_, _, to = p.split(" ")
        for i in range(int(count)):
            val = stack[from_].pop()
            stack[to].append(val)

    # join the top ones to create message
    message = ""   
    for i in range((len(crates[0])+1)//4):
        message += stack[str(i+1)][-1]
        
    print(message) # WCZTHTMPS


def part2():
    crates, procedure = get_input(input_file).split("\n\n", 1)
    crates = crates.rsplit("\n", 1)[0].split("\n")
    
    # create stack as dictionary from given input as text
    stack = create_stack_table(crates)
    
    # apply the procedure with ability to pick up multiple crates
    for p in procedure.split("\n"):
        if not p: continue
        _, count, _, from_, _, to = p.split(" ")
        temp_stack = []
        for i in range(int(count)):
            val = stack[from_].pop()
            temp_stack.append(val)
        temp_stack.reverse()
        stack[to] += temp_stack
    
    # join the top ones to create message
    message = ""   
    for i in range((len(crates[0])+1)//4):
        message += stack[str(i+1)][-1]
        
    print(message) # BLSGJSDTS


def main():
    part1()
    part2()

        
if __name__ == "__main__":
    main()