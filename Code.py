import random
import pygame

# létrehozzuk a pygame-et
pygame.init()
# csinálunk kijelzőt megadott méretben
screen = pygame.display.set_mode((1001,1001))
# kiírjuk a fejlécre
pygame.display.set_caption("Maze Generator")
# lérehozzuk az órát amivel majd fps-t tudunk szabályozni
clock = pygame.time.Clock()

# létrehozzuk a labirintus változóját
size = 10
# falak sorrendje top, bottom, left, right
maze = [[[True] * 4 for j in range(size)] for i in range(size)]

# alap rekurzív labirintus generátor függény (saját magát hívja a kövi mezőre)
def genMaze(x,y):
    # megszerzünk egy véletlenszerű még üres szomszédos mezőt
    n = getNeighbor(x, y)
    # amíg van újabb üres szomszéd
    while n:
        # minket kinyitunk felé
        maze[x][y][whichNeighbor(n[0]-x, n[1]-y)] = False
        # a másik mezőt kinyitjuk felénk
        maze[n[0]][n[1]][whichNeighbor(x - n[0], y - n[1])] = False
        # meghívjuk a generálást arra a mezőre is
        genMaze(n[0], n[1])
        # (^^ a tovább generálás után) keresünk egy újabb üres szomszédos mezőt
        n = getNeighbor(x, y)

# keresünk egy random szabad szomszédos mezőt
def getNeighbor(x, y):
    # elkezdjük össze gyűjteni a szabad szomszédokat
    neighbors = []
    # mind a 4 szomszédot megnézzük, ha van (nem esik pályán kívül) és üres mező, akkor feljegyezzük
    if y > 0 and maze[x][y-1] == [True]*4:
        neighbors.append((x, y-1))
    if y < size-1 and maze[x][y+1] == [True]*4:
        neighbors.append((x, y+1))
    if x > 0 and maze[x-1][y] == [True]*4:
        neighbors.append((x-1, y))
    if x < size-1 and maze[x+1][y] == [True]*4:
        neighbors.append((x+1, y))
    # ha egyet se találtunk, akkor hamissal térünk vissza
    if len(neighbors) == 0:
        return False
    # egyébként véletlenszerűvel (össze keverjük és a 0-ással)
    random.shuffle(neighbors)
    return neighbors[0]

# két koordináta különbségéből megmondja, hogy a mező 4db boolean értékéből melyik irányú falon megyünk át
def whichNeighbor(dx,dy):
    return (1 if dx+dy > 0 else 0) + (2 if dx != 0 else 0)

# kirajzolja a mezőket a pygame-be
def drawMaze():
    # feketével töltjük ki a képernyőt
    screen.fill((0,0,0))
    # végig megyünk a mezőkön
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            # a kiválasztot mezőt...
            m = maze[x][y]
            # ha van alja kirajzoljuk
            if m[1]:
                pygame.draw.line(screen, (255, 255, 255), (x * 100, (y + 1) * 100), ((x + 1) * 100, (y + 1) * 100), 1)
            # ha van jobb oldala kirajzoljuk
            if m[3]:
                pygame.draw.line(screen, (255, 255, 255), ((x + 1) * 100, y * 100), ((x + 1) * 100, (y + 1) * 100), 1)
            # a másik kettőt nem kell, mert a felettünk és balra lévőnél már rajzoltuk


# elindítjuk a labirintus generálását 0,0 mezőtől, innen már rekurzívan meg fogja hívni magát a többi mezőre
genMaze(0, 0)

# kirajzoljuk a legenerált labirintust, amíg a felhasználó be nem zárja
done = False
while not done:
    # várjuk az X gomb megnyomását
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
    # kirajzolunk
    drawMaze()
    # kirakjuk a friss rajzot a képernyőre (rajzolás mindig egy másodlagos képernyőre történik, hogy ne villogjon)
    pygame.display.flip()
    # várunk picit, hogy kb 60fps-el rajzoljunk (ne terheljük túl a videókártyát)
    clock.tick(60)
# kilépett a felhasználó, pygame leállítás és vége
pygame.quit()