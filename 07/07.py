
class Dir:
    def __init__(self, name, parent = None):
        self.name = name
        self.dirs = []
        self.files = []
        self.parent = parent
    
    def get_name(self):
        return self.name

    def get_all_dirs(self):
        dirs = []
        if self.dirs:
            dirs += self.dirs
            for dir in self.dirs:
                subdirs = dir.get_all_dirs()
                if subdirs:
                    dirs += subdirs
            return dirs
        return None
    
    def get_size(self):
        size = sum([file.size for file in self.files])
        for dir in self.dirs:
            size += dir.get_size()
        return size
    
    def __str__(self):
        return self.name

class File:
    def __init__(self, size, name):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name

def build_tree(lines):
    root = Dir('/')
    wd = root
    for line in lines:
        wd = parse_line(line, wd, root)
    return root

def parse_line(line, wd, root):
    command = line.strip().split(' ')
    if command[0] == '$' and command[1] == 'cd':
        return cd(wd, command[2], root)
    elif command[0] == 'dir':
        wd.dirs.append(Dir(command[1], wd))
    elif command[0].isdigit():
        wd.files.append(File(int(command[0]), command[1]))
    return wd

def cd(wd, td, root):
    if td == '..':
        return wd.parent    
    if td == '/':
        return root
    if t := [d for d in wd.dirs if d.name == td]:
        return t[0]
    else:
        mkdir = Dir(td, wd)
        wd.dirs.append(mkdir)
        return mkdir
        


lines = open('input.txt', 'r').readlines()
root = build_tree(lines)
small_dirs = [dir for dir in root.get_all_dirs() + [root] if dir.get_size() <= 100000]
print(sum([dir.get_size() for dir in small_dirs]))

delete_thresh = 30000000 - (70000000 - root.get_size())
over_thresh = [dir for dir in root.get_all_dirs() + [root] if dir.get_size() >= delete_thresh]
over_thresh.sort(key=lambda dir: dir.get_size())
print([dir.get_size() for dir in over_thresh][0])