from time import sleep

import numpy
import cv2


class ImageToHash:
    def __init__(self, image):
        self.image = image
        self.ArrayImage = None
        self.HashedSpaceString = None
        self.is_StartFound = False
        self.is_EndFound = False

    def ConvertImageToArray(self):
        img = cv2.imread(self.image, 0)
        self.ArrayImage = numpy.array(img)
        return self.ArrayImage

    def replaceTheRowOfHashedSpaceString(self, rowNo, replaceWith):
        temp = self.HashedSpaceString.split("\n")
        temp[rowNo] = replaceWith
        self.HashedSpaceString = "\n".join(temp)

    def replaceTheColumnOfHashedSpaceString(self, colNo, replaceWith):
        temp = self.HashedSpaceString.split("\n")
        twoDArray = [list(row) for row in temp]
        tempString = ""
        for index, row in enumerate(twoDArray):
            row[colNo] = replaceWith[index]
            tempString += "".join(row)
            if index != len(twoDArray) - 1:
                tempString += "\n"
        self.HashedSpaceString = tempString

    def ConvertArrayToHashString(self):
        self.HashedSpaceString = ""
        for index, i in enumerate(self.ArrayImage):
            for j in i:
                if j == 0:
                    self.HashedSpaceString += "#"
                else:
                    self.HashedSpaceString += " "
            if index != len(self.ArrayImage) - 1:
                self.HashedSpaceString += "\n"
        return self.HashedSpaceString

    def IndentifyStartAndEnd(self):
        temp = self.HashedSpaceString
        # getting first and last row
        firstRow = temp.split("\n")[0]
        lastRow = temp.split("\n")[-1]
        # getting first and last column
        firstCol = ""
        lastCol = ""
        for i in temp.split("\n"):
            if i == "":
                continue
            firstCol += i[0]
            lastCol += i[-1]
        # checking if the first row has an space if it does then it is the start replacing the first space with S
        if " " in firstRow:
            firstRow = firstRow.replace(" ", "S", 1)
            self.is_StartFound = True
        # checking if the last row has an space if it does then it is the end replacing it with E
        if " " in lastRow:
            lastRow = lastRow[::-1].replace(" ", "E", 1)
            lastRow = lastRow[::-1]
            self.is_EndFound = True
        if self.is_StartFound and self.is_EndFound:
            self.replaceTheRowOfHashedSpaceString(0, firstRow)
            self.replaceTheRowOfHashedSpaceString(-1, lastRow)
            return True
        if " " in firstCol:
            firstCol = firstCol.replace(" ", "S", 1)
            self.is_StartFound = True
        if " " in lastCol:
            lastCol = lastCol[::-1].replace(" ", "E", 1)
            lastCol = lastCol[::-1]
            self.is_EndFound = True
        if self.is_StartFound == False or self.is_EndFound == False:
            raise Exception("Start or End not found")
        self.replaceTheColumnOfHashedSpaceString(0, firstCol)
        self.replaceTheColumnOfHashedSpaceString(-1, lastCol)

    def saveHashToFile(self, file="hashed_maze.txt"):
        with open(file, "w") as f:
            f.write(self.HashedSpaceString)

    def StringToArray(self, mazeData):
        Array = []
        row = 0
        for line in mazeData.split("\n"):
            Array.append([])
            for char in line:
                if char == "#":
                    Array[row].append([0, 0, 0])
                elif char == ".":
                    Array[row].append([204, 204, 255])
                else:
                    Array[row].append([255, 255, 255])
            row += 1
        Array.pop()
        return Array

    def ArrayToImage(self, array):
        imgw = numpy.array(array)
        cv2.imwrite("solved_maze.png", imgw)

