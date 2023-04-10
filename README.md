# Maze Solver

The Maze Solver Algorithm  can solve mazes given in the form of an image or a string of hash and spaces. It is written using the NumPy and OpenCV packages.

## Features
- Can solve mazes given in the form of an image or a string of hash and spaces.
- Uses the Depth-First Search Maze Solver Algorithm to find the shortest path from the starting position to the end of the maze.
- Performs image preprocessing to convert the maze image to a binary image with the maze walls in black and the empty spaces in white.
- Returns a list of tuples representing the path taken by the solver to reach the end of the maze.
- Written in Python using the NumPy and OpenCV packages.

## Installation
To install the package, you can use pip:
```
pip install numpy opencv-python

```

## ScreenShots
| Unsolved  | Solved |  Unsolved |  Solved |
| ------- | ------- |  ------- |  ------- |
|<img src="https://github.com/BinaryBreaker/MazeSolver/raw/master/screenshots/img_1.png" alt="maze screenshot" width="500">|<img src="https://github.com/BinaryBreaker/MazeSolver/raw/master/screenshots/img.png" alt="maze screenshot" width="500">|<img src="https://github.com/BinaryBreaker/MazeSolver/raw/master/screenshots/img_2.png" alt="maze screenshot" width="500">|<img src="https://github.com/BinaryBreaker/MazeSolver/raw/master/screenshots/img_3.png" alt="maze screenshot" width="500">|


## Usage
The main function in this code uses the Maze Solver Algorithm to solve a maze given as an image file. Here's how it works:

- The ImageToHash class is used to read in the maze image and convert it to a string of hash and spaces.
- The PathFinder class is initialized with the maze string.
- The PathFinder class converts the maze string to a 2D array of Node objects.
- The TriverseToFindPathLoop method of the PathFinder class is called to solve the maze and find the shortest path from the start to the end.
- If the maze is solved, the ArrayToImage method of the ImageToHash class is used to convert the solved maze back to an image and save it to a file.
- The string "Solved" is printed to the console.
- To use this code with your own maze image, you should replace the path in the ImageToHash constructor with the path to your own maze image.

```
from maze.ImageToHash import ImageToHash
from maze.Algo import PathFinder


def main():
    image = ImageToHash(r"./assets/maze.png")
    image.ConvertImageToArray()
    image.ConvertArrayToHashString()
    image.IndentifyStartAndEnd()
    pf = PathFinder(image.HashedSpaceString)
    pf.Convert2dArrayToNode()
    if pf.TriverseToFindPathLoop():
        image.ArrayToImage(image.StringToArray(pf.printGraphInOrder()))
        print("Solved")



if __name__ == "__main__":
    main()


```


## Image Preprocessing

```
    def ConvertImageToArray(self):
        img = cv2.imread(self.image, 0)
        self.ArrayImage = numpy.array(img)
        return self.ArrayImage
        
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

```
This code block contains two functions used for image preprocessing before solving the maze.

The ConvertImageToArray function uses the OpenCV library to read in the maze image and convert it to a NumPy array. The array is then stored in the ArrayImage variable and returned for further processing.

The ConvertArrayToHashString function converts the NumPy array of the maze into a string of hash and spaces representing the maze walls and empty spaces respectively. The function iterates over each row and column of the array, and adds a "#" character to the string for each black pixel (i.e., maze wall) and a " " character for each white pixel (i.e., empty space). The resulting string is stored in the HashedSpaceString variable and returned for use in the PathFinder class.

These two functions are essential for preprocessing the maze image before it can be solved by the PathFinder class. By converting the image to a binary format and then to a string of hash and spaces, the algorithm can accurately identify the walls and empty spaces in the maze and find the shortest path from the starting position to the end.



## Credits
This algorithm was developed by BinaryBreaker. If you have any questions or feedback, please contact me at muzamilhuss4@gmail.com.
