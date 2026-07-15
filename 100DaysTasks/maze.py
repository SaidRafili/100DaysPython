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

    def moveUp():
        nonlocal startY
        startY -= 1

    def moveDown():
        nonlocal startY
        startY += 1

    def moveRight():
        nonlocal startX
        startX += 1

    def moveLeft():
        nonlocal startX
        startX -= 1

    def checkAround():
        nonlocal startX, startY

        for i in range(100):
            print(f"Step {i}: position = ({startX}, {startY})")
            print("Current position:", startY, startX)

            if maze[startY, startX] == 3:
                print("You won")
                return

            elif maze[startY - 1, startX] in [0, 3]:
                moveUp()

            elif maze[startY, startX + 1] in [0, 3]:
                moveRight()

            elif maze[startY + 1, startX] in [0, 3]:
                moveDown()

            elif maze[startY, startX - 1] in [0, 3]:
                moveLeft()

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