input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return  f.read()


def calculate_sum_of_calories(inventory: str) -> int:
    elves = inventory.split("\n\n")
    calories = list(map(lambda e: sum(list(map(lambda c: int(c) if c else 0, e.split("\n")))), elves))
    return calories


def part1():
    input = get_input(input_file)
    top_calorie = max(calculate_sum_of_calories(input))
    print(top_calorie) # 66186


def part2():
    input = get_input(input_file)
    calories = calculate_sum_of_calories(input)
    calories.sort()
    top_three = calories[-1] + calories[-2] + calories[-3]
    print(top_three) # 196804


def main():
    part1()
    part2()

        
if __name__ == "__main__":
    main()