input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


class Monkey:
    
    
    def __init__(self, items: list, operation: list, mod: int, true: int, false: int):
        self.items = items
        self.operation = operation
        self.mod = mod
        self.true = true
        self.false = false
        self.total_inspect = 0
        

def calculate_monkey_business(round_: int, worry_divider: int):
    monkeys = []
    global_mod = 1
    
    for monkey in get_input(input_file).strip().split("\n\n"):
        lines = monkey.split("\n")
        items = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        operation = lines[2].split(": ")[-1].replace("new = old ", "").split(" ")
        mod = int(lines[3].split(" ")[-1])
        global_mod *= mod
        true = int(lines[4].split(" ")[-1])
        false = int(lines[5].split(" ")[-1])
        monkeys.append(Monkey(items, operation, mod, true, false))
    
    for i in range(round_):
        for monkey in monkeys:
            while monkey.items:
                worry_level = monkey.items[0]
                if monkey.operation[0] == "+":
                    if monkey.operation[1] == "old":
                        worry_level += worry_level
                    else:
                        worry_level += int(monkey.operation[1])
                    
                elif monkey.operation[0] == "*":
                    if monkey.operation[1] == "old":
                        worry_level *= worry_level
                    else:
                        worry_level *= int(monkey.operation[1])
                
                worry_level = worry_level // worry_divider % global_mod
                monkey.total_inspect += 1
                
                del monkey.items[0]
                if worry_level%monkey.mod == 0:
                    monkeys[monkey.true].items.append(worry_level)
                else:
                    monkeys[monkey.false].items.append(worry_level)
                    
    
    total_inspects = sorted([m.total_inspect for m in monkeys])
    monkey_business = total_inspects[-1]*total_inspects[-2]

    return monkey_business 


def part1():
    return calculate_monkey_business(20, 3)


def part2():
    return calculate_monkey_business(10000, 1)


def main():
    print(part1()) # 110220
    print(part2()) # 19457438264

        
if __name__ == "__main__":
    main()