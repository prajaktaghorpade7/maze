import queue

def createMaze():
    maze = []
    maze.append(["|","O", "-", "-", "-", "-", "-", "-", "|"])
    maze.append(["|"," ", " ", " ", " ", " ", " ", " ", "|"])
    maze.append(["|"," ", "|", " ", " ", "-", "-", "-", "|"])
    maze.append(["|"," ", "|", "-", " ", " ", " ", " ", "|"])
    maze.append(["|"," ", "|", " ", "|", "-", "|", " ", "|"])
    maze.append(["|"," ", "|", " ", "|", " ", "|", " ", "|"])
    maze.append(["|","|", "|", " ", "|", " ", "|", " ", "|"])
    maze.append(["|"," ", " ", " ", " ", " ", " ", " ", "|"])
    maze.append(["|","-", "-", "-", "-", "-", "X", "-", "|"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("o ", end="")
            else:
                print(col + " ", end="")
        print()

        
#Function to find the valid direction (Left(L), Right(R), Up(U), Down(D))

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "|" or maze[j][i] == "-"):
            return False

    return True


#Function to return whether the path has reached the end point

def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("\nFound: " + moves +"\n")
        printMaze(maze, moves)
        return True

    return False


#Driver Code - Main Algorithm

nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()

while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]: 
        put = add + j
        if valid(maze, put):
            nums.put(put)

''' Symbols used:

    O : start point
    X : end point
    | or - : walls/obstacles
    
    This algorithm is a path finding method in a maze using Breadth First Search
    Created by Prajakta Ghorpade.
'''

