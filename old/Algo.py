a = None
with open("maze.txt", "r") as f:
    a = f.read()

start = None
first = None


class Node:
    def __init__(self, value=None):
        global start
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.value = value
        if value == "S":
            self.isStart = True
            start = self
        else:
            self.isStart = False
        if value == "E":
            self.isEnd = True
        else:
            self.isEnd = False
        self.isVisited = False

    def isConnected(self, node):
        if node is None:
            return False
        if node.left == self or node.right == self or node.up == self or node.down == self:
            return True


def convertStringTo2dArray(data):
    data = data.split("\n")
    data = [list(i) for i in data if i != ""]

    return data


def Convert2dArrayToNode():
    global start, first
    nodes = convertStringTo2dArray(a)
    for i in nodes:
        print(len(i), end=" ")
    temp = [[None for i in j] for j in nodes]
    print()
    for i in temp:
        print(len(i), end=" ")

    for rowIndex, row in enumerate(nodes):
        for colIndex, col in enumerate(row):
            temp[rowIndex][colIndex] = Node(col)
    for rowIndex, row in enumerate(temp):
        for colIndex, col in enumerate(row):
            if colIndex != 0:
                col.left = temp[rowIndex][colIndex - 1]
            if colIndex != len(row) - 1:
                col.right = temp[rowIndex][colIndex + 1]
            if rowIndex != 0:
                col.up = temp[rowIndex - 1][colIndex]
            if rowIndex != len(temp) - 1:
                col.down = temp[rowIndex + 1][colIndex]
    first = temp[0][0]


def printGraphInOrder():
    global first
    string = ""
    temp = first
    while temp.right is not None and temp.down is not None:
        while temp.right is not None:
            print(temp.value, end="")
            string += temp.value
            temp = temp.right
        print(temp.value)
        string += temp.value + "\n"
        temp = temp.down
        while temp.left is not None:
            temp = temp.left
    while temp.right is not None:
        print(temp.value, end="")
        string += temp.value
        temp = temp.right
    print(temp.value)
    string += temp.value + "\n"
    return string


def TriverseToFindPath(node: Node, prev=None):
    if node.isVisited:
        return False
    node.isVisited = True
    if node.isEnd:
        return True
    if node.value == "#":
        return False
    if node.right is not None:
        a = TriverseToFindPath(node.right, prev=node)
        if a:
            if node.value == " ":
                node.value = "_"
            return True
    if node.left is not None:
        a = TriverseToFindPath(node.left, prev=node)
        if a:
            if node.value == " ":
                node.value = "_"
            return True
    if node.up is not None:
        a = TriverseToFindPath(node.up, prev=node)
        if a:
            if node.value == " ":
                node.value = "|"
            return True
    if node.down is not None:
        a = TriverseToFindPath(node.down, prev=node)
        if a:
            if node.value == " ":
                node.value = "|"
            return True
    if node.value == " ":
        node.value = " "
    return False


# Convert TriverseToFindPath to a loop instead of recursion
def TriverseToFindPathLoop(node: Node, prev=None):
    stack = [node]
    isSolved = False
    while len(stack) > 0:
        node = stack.pop()
        if node.isVisited:
            continue
        node.isVisited = True
        if node.isEnd:
            isSolved = True
            break
        if node.value == "#":
            continue
        if node.up is not None:
            stack.append(node.up)
        if node.down is not None:
            stack.append(node.down)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    # only adding path if the maze is solved
    # adding path to only the nodes that are " " and are nebours of the path
    prev = None
    while stack and isSolved:
        node = stack.pop()

        if node.value == " ":
            node.value = "."
        prev = node
    return isSolved


def main():
    global start
    Convert2dArrayToNode()
    if start is None:
        print("No start point found")
        return
    print()
    print(TriverseToFindPathLoop(start))
    print("\n\n\n")
    with open("mazeSolved.txt", "w") as f:
        f.write(printGraphInOrder())


if "__main__" == __name__:
    main()
