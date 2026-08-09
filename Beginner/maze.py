import matplotlib.pyplot as plt
import numpy as np

maze = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,3,1],
    [1,1,1,1,1,0,0,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,2,1,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
])

def mazeAlgo():
    startX = 1
    startY = 11
    visited = 2

    def moveUp():
        nonlocal startY
        startY -= 2

    def moveDown():
        nonlocal startY
        startY += 2

    def moveRight():
        nonlocal startX
        startX += 2

    def moveLeft():
        nonlocal startX
        startX -= 2

    def checkAround():
        nonlocal startX, startY, visited

        for i in range(100):
            print("Current position:", startY, startX)

            if  maze[startY - 1, startX] in [0,3] and maze[startY - 2, startX] != 2:
                moveUp()
                if maze[startY, startX] == 3:
                    print("You won")
                    break
                else:
                    maze[startY, startX] = visited
            elif maze[startY, startX + 1] in [0,3] and maze[startY, startX + 2] != 2:
                moveRight()
                if maze[startY, startX] == 3:
                    print("You won")
                    break
                else:
                    maze[startY, startX] = visited
            elif maze[startY + 1, startX] in [0,3] and maze[startY + 2, startX] != 2:
                moveDown()
                if maze[startY, startX] == 3:
                    print("You won")
                    break
                else:
                    maze[startY, startX] = visited
            elif maze[startY, startX - 1] in [0,3] and maze[startY, startX - 2] != 2:
                moveLeft()
                if maze[startY, startX] == 3:
                    print("You won")
                    break
                else:
                    maze[startY, startX] = visited
            else:
                print("No available movement")
                return
    def printMaze():
        display = maze.copy()
        display[startY, startX] = 9
        print(display)
        
    checkAround()
    printMaze()

mazeAlgo()