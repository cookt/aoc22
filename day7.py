from typing import List

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class FileNode:
    def __init__(self, name: str, parent: 'FileNode', childNodes: List['FileNode'], childFiles: List['File']):
        self.name = name
        self.parent = parent
        self.childNodes = childNodes
        self.files = childFiles
    
    def total_size(self):
        fileSize = sum([f.size for f in self.files])
        if len(self.childNodes) == 0:
            return fileSize
        else:
            return fileSize + sum([fn.total_size() for fn in self.childNodes])
    
    def find_subdirs(self, threshold: int):
        subdirs = []
        searchNodes = self.childNodes
        while len(searchNodes) > 0:
            mnode = searchNodes.pop()
            if mnode.total_size() <= threshold:
                subdirs.append(mnode)
            searchNodes.extend(mnode.childNodes)
        return subdirs

    def find_smallest_above(self, required: int):
        searchNodes = self.childNodes
        dirs_above = []
        while len(searchNodes) > 0:
            mnode = searchNodes.pop()
            if mnode.total_size() < required:
                continue
            else:
                dirs_above.append(mnode)
            searchNodes.extend(mnode.childNodes)
        min_bytes_over = float('inf')
        print(dirs_above)
        final_node = None
        for d in dirs_above:
            bytes_over = d.total_size() - required
            print(d, bytes_over)
            if bytes_over < min_bytes_over:
                min_bytes_over = bytes_over
                final_node = d
        return final_node.total_size()

    def __str__(self) -> str:
        return self.name + ', size=' + str(self.total_size())
    
    def __repr__(self) -> str:
        return self.name + ', size=' + str(self.total_size())

    def print_tree(self, numTabs: int):
        dir_str = ' ' * numTabs
        print(dir_str + '-' + self.name)
        for f in self.files:
            print(dir_str + '-' + f.name + ' (file, size=' + str(f.size) + ')')
        for f in self.childNodes:
            f.print_tree(numTabs+1)

file = open("day7_input.txt", 'r')
path = '/'
root_node = FileNode(path, None, [], [])
current_node = root_node

for line in file.readlines():
    if line.startswith("$"):
        commandArgs = line.rstrip().split(" ")
        command = commandArgs[1]
        if command == 'cd':
            newPath = commandArgs[2]
            if newPath == '..':
                current_node = current_node.parent
            elif newPath == root_node.name:
                continue
            else:
                next_node = [f for f in current_node.childNodes if f.name == newPath]
                current_node = next_node[0]
        else:
            continue
    else:
        file_listing = line.rstrip().split(" ")
        if file_listing[0] == 'dir':
            nodeName = file_listing[1]
            node = FileNode(nodeName, current_node, [], [])
            current_node.childNodes.append(node)
        else:
            fileName = file_listing[1]
            fileSize = int(file_listing[0])
            newFile = File(fileName, fileSize)
            current_node.files.append(newFile)

threshold = 100000
# dires = root_node.find_subdirs(threshold)
# print(sum([f.total_size() for f in dires]))
root_node.print_tree(0)
available = 70000000
update = 30000000
unused = available - root_node.total_size()
required = update - unused
print(required)
print(root_node.find_smallest_above(required))