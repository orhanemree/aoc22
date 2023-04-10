input_file = "input.txt"

def get_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


class Dir:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        
    
    def get_path(self):
        if not self.parent:
            return self.name
        parent_name = self.parent.get_path()
        return parent_name + self.name
    
    
    def add_child(self, child):
        self.children.append(child)
        
        
    def get_child(self, name: str):
        return [c for c in self.children if c.name == name][0]
    
        
    def get_size(self):
        return sum([c.get_size() for c in self.children])
    

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        
        
    def get_size(self):
        return self.size
        

def create_tree(input_: str):
    root = Dir("/")
    current_dir = root
    
    for line in input_.strip().split("\n"):
        tokens = line.split(" ")
        
        if tokens[0] == "$":
            # it is a command
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    current_dir = root
                elif tokens[2] == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.get_child(tokens[2])

            elif tokens[1] == "ls":
                continue
            
        elif tokens[0] == "dir":
            # it is another dir
            current_dir.add_child(Dir(tokens[1], current_dir))
        
        elif tokens[0].isdigit():
            # it is size of a file
            current_dir.add_child(File(tokens[1], int(tokens[0])))
            
    return root


def get_dir_sizes(root, dir_sizes={}):
    for c in root.children:
        if type(c).__name__ == "Dir":
            dir_sizes[c.get_path()] = c.get_size()
            get_dir_sizes(c, dir_sizes)
            
    return dir_sizes


def part1():
    root = create_tree(get_input(input_file))
    dir_sizes = get_dir_sizes(root)
    
    return sum([dir_sizes[size] for size in dir_sizes if dir_sizes[size] < 100000])
    

def part2():
    root = create_tree(get_input(input_file))
    dir_sizes = get_dir_sizes(root)
    space_required = 30000000-(70000000-root.get_size())
    
    return min([dir_sizes[size] for size in dir_sizes if dir_sizes[size] > space_required])


def main():
    # oh, that one was hard
    print(part1()) # 1391690
    print(part2()) # 5469168

        
if __name__ == "__main__":
    main()