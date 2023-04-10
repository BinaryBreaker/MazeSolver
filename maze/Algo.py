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


class PathFinder:

    def __init__(self, mazeString):
        global start, first
        self.MazeString = mazeString
        self.TwoDArray = None

    def convertStringTo2dArray(self):
        self.TwoDArray = self.MazeString.split("\n")
        self.TwoDArray = [list(i) for i in self.TwoDArray if i != ""]
        return self.TwoDArray

    def Convert2dArrayToNode(self):
        global start, first
        nodes = self.convertStringTo2dArray()
        temp = [[None for i in j] for j in nodes]
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

    def printGraphInOrder(self):
        global first
        string = ""
        temp = first
        while temp.right is not None and temp.down is not None:
            while temp.right is not None:
                string += temp.value
                temp = temp.right
            string += temp.value + "\n"
            temp = temp.down
            while temp.left is not None:
                temp = temp.left
        while temp.right is not None:
            string += temp.value
            temp = temp.right
        string += temp.value + "\n"
        return string

    def TriverseToFindPathLoop(self):
        stack = [start]
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

    def safeTheFile(self):
        with open("Solved_maze.txt", "w") as f:
            f.write(self.printGraphInOrder())


