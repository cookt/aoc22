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


file = open("day7_input.txt", 'r')
path = ''
root_node = FileNode(path, None, [], [])
current_node = root_node

for line in file.readlines():
    if line.startswith("$"):
        commandArgs = line.rstrip().split(" ")
        command = commandArgs[0]
        if command == 'cd':
            newPath = commandArgs[1]
            if newPath == '..':
                current_node = current_node.parent
            else:
                next_node = [f for f in current_node.childNodes if f.name == newPath]
                current_node = next_node[0]
        else:
            continue
    else:
        file_listing = line.rstrip().split(" ")
        if file_listing[0] == 'dir':
            nodeName = file_listing[1]
            node = FileNode(current_node.name + nodeName, current_node, [], [])
            current_node.childNodes.append(node)
        else:
            fileName = file_listing[1]
            fileSize = int(file_listing[0])
            newFile = File(fileName, fileSize)
            current_node.files.append(newFile)

threshold = 100000

search_node = root_node


