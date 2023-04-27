import random
import pygame
from colorama import init, Fore

cell = 'c'
wall = 'w'

Size = 10


def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1] == 'c'):
        s_cells += 1
    return s_cells


def delete_wall(rand_wall):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

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

    while walls:
        rand_wall = walls[int(random.random()*len(walls))-1]

        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

        if rand_wall[0] != 0:
            if maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]+1] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

        if rand_wall[0] != height-1:
            if maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue
                            
        if rand_wall[1] != width-1:
            if maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

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

choice = input('Labirintust szeretnél csinálni? (Gépeld be pontosan ugyan azt a választ, amelyet itt ír): [Igen/Nem] -- ')
if choice == 'Igen':
    sizeChoice = input('Nehézség? [Easy/Medium/Hard/Extreme/Why] -- ')
    if sizeChoice == 'Easy':
        print_maze(init_maze(Size, Size))
    elif sizeChoice == 'Medium':
        print_maze(init_maze(Size * 3, Size * 3))
    elif sizeChoice == 'Hard':
        print_maze(init_maze(Size * 5, Size * 5))
    elif sizeChoice == 'Extreme':
        print_maze(init_maze(Size * 10, Size * 10))
    elif sizeChoice == 'Why':
        print_maze(init_maze(Size * 100, Size * 100))
elif choice == 'Nem':
    print('Rendben-')

