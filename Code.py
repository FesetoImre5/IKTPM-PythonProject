import random

# hozzon létre egy labirintust adott szélességgel és magassággal
def create_maze(width, height):
    # hozzon létre egy rácsot az összes falat
    maze = [[{"top": True, "right": True, "bottom": True, "left": True} for j in range(width)] for i in range(height)]

    # véletlen cellából indul
    current_i, current_j = random.randint(0, height - 1), random.randint(0, width - 1)
    stack = [(current_i, current_j)]

    # végezzen mélységi keresést a falak eltávolításához és utak létrehozásához
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

    # távolítsa el a látogatott zászlót
    for i in range(height):
        for j in range(width):
            if "visited" in maze[i][j]:
                del maze[i][j]["visited"]

    return maze

def print_maze(maze):
    height, width = len(maze), len(maze[0])
    for i in range(height):
        # felső falak nyomtatása
        for j in range(width):
            print("+", end="")
            print("  " if maze[i][j]["top"] else "--", end="")
        print("+")
        # nyomtasson bal és jobb falakat
        for j in range(width):
            print("|" if maze[i][j]["left"] else " ", end="")
            print("  ", end="")
            print("|" if maze[i][j]["right"] else " ", end="")
        print("|")
    # nyomtasson alsó falakat
    for j in range(width):
        print("+", end="")
        print("  " if maze[height - 1][j]["bottom"] else "--", end="")
    print("+")

# példahasználat
maze = create_maze(10, 10)
print_maze(maze)
