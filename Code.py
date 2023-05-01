import random

def create_maze(width, height):
    maze = [[{"top": True, "right": True, "bottom": True, "left": True} for j in range(width)] for i in range(height)]

    current_i, current_j = random.randint(0, height - 1), random.randint(0, width - 1)
    stack = [(current_i, current_j)]

    while stack:
        current_i, current_j = stack.pop()
        maze[current_i][current_j]["visited"] = True
        directions = []
        if current_i > 0 and not maze[current_i - 1][current_j].get("visited"):
            directions.append(("top", -1, 0))
        if current_j < width - 1 and not maze[current_i][current_j + 1].get("visited"):
            directions.append(("right", 0, 1))
        if current_i < height - 1 and not maze[current_i + 1][current_j].get("visited"):
            directions.append(("bottom", 1, 0))
        if current_j > 0 and not maze[current_i][current_j - 1].get("visited"):
            directions.append(("left", 0, -1))
        if not directions:
            continue
        direction, di, dj = random.choice(directions)
        next_i, next_j = current_i + di, current_j + dj
        maze[current_i][current_j][direction] = False
        maze[next_i][next_j][{"top": "bottom", "right": "left", "bottom": "top", "left": "right"}[direction]] = False
        stack.append((next_i, next_j))

    for i in range(height):
        for j in range(width):
            if "visited" in maze[i][j]:
                del maze[i][j]["visited"]

    return maze

def print_maze(maze):
    height, width = len(maze), len(maze[0])
    for i in range(height):
        for j in range(width):
            print("+", end="")
            print("  " if maze[i][j]["top"] else "--", end="")
        print("+")
        for j in range(width):
            print("|" if maze[i][j]["left"] else " ", end="")
            print("  ", end="")
            print("|" if maze[i][j]["right"] else " ", end="")
        print("|")
    for j in range(width):
        print("+", end="")
        print("  " if maze[height - 1][j]["bottom"] else "--", end="")
    print("+")

choice = input("Milyen nehézségű labirintust szeretnél generálni? [1-5] -- ")
if choice == '1':
    maze1 = create_maze(10, 10)
    print_maze(maze1)
elif choice == '2':
    maze2 = create_maze(20, 20)
    print_maze(maze2)
elif choice == '3':
    maze3 = create_maze(30, 30)
    print_maze(maze3)
elif choice == '4':
    maze4 = create_maze(40, 40)
    print_maze(maze4)
elif choice == '5':
    maze5 = create_maze(50, 50)
    print_maze(maze5)

#maze = create_maze(10, 10)
#print_maze(maze)
