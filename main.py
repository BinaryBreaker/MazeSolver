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
