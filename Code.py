import random

from colorama import init, Fore

cell = 'c'
wall = 'w'

S = 10

def init_maze(width,height):
    maze = []
    for i in range(0,height):
        line = []
        for j in range(0,width):
            line.append('u')
        maze.append(line)


    starting_height = int(random.random() * height)

    if starting_height == 0:
        starting_height += 1

    if starting_height == height-1:
        starting_height -= 1


    starting_width = int(random.random() * width)

    if starting_width == 0:
        starting_width += 1

    if starting_width == width-1:
        starting_width -= 1

    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])


    maze[starting_height - 1][starting_width] = wall
    maze[starting_height][starting_width - 1] = wall
    maze[starting_height][starting_width + 1] = wall
    maze[starting_height + 1][starting_width] = wall
    return maze

def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end='')
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end='')
            else:
                print(Fore.RED, f'{maze[i][j]}', end='')
        print('')

choice = input('Create a maze? (Type the answer exactly the same as it says) [Yes/No] -- ')
if choice == 'Yes':
    sizeChoice = input('Difficulty? [Easy/Medium/Hard/Extreme/Why] -- ')
    if sizeChoice == 'Easy':
        print_maze(init_maze(S, S))
    elif sizeChoice == 'Medium':
        print_maze(init_maze(S * 3, S * 3))
    elif sizeChoice == 'Hard':
        print_maze(init_maze(S * 5, S * 5))
    elif sizeChoice == 'Extreme':
        print_maze(init_maze(S * 10, S * 10))
    elif sizeChoice == 'Why':
        print_maze(init_maze(S * 100, S * 100))
elif choice == 'No':
    print('Alright-')

