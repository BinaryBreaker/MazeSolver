import numpy
import cv2
image = r".\assets\maze10.png"


# convert the image to grayscale and then to 2d array
def convert_to_2d_array(image):
    img = cv2.imread(image, 0)
    return numpy.array(img)


def ImageToFile(image):
    a = convert_to_2d_array(image)
    b = ""
    for i in a:
        for j in i:
            if j == 0:
                b += "#"
            else:
                b += " "

        b += "\n"
    with open("maze.txt", "w") as f:
        f.write(b)


def FileToArray(file):
    mazeData = None
    with open(file, "r") as f:
        mazeData = f.read()
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


def ArrayToImage(array):
    img = convert_to_2d_array(image)
    imgw = numpy.array(array)
    # img = Image.fromarray(img.astype(numpy.uint8))
    cv2.imwrite("mazeq1.png", imgw)


def main():
    Array = FileToArray("mazeSolved.txt")
    # with open("mazeSolvedq.txt", "w") as f:
    #     f.write(str(Array))
    ArrayToImage(Array)


main()
# ImageToFile(image)
