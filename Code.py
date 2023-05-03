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
                pygame.draw.line(screen, (255,255,255), (x100, (y+1)100), ((x+1)100, (y+1)100), 1)
            # ha van jobb oldala kirajzoljuk
            if m[3]:
                pygame.draw.line(screen, (255, 255, 255), ((x+1)100, y100), ((x+1)100, (y+1)100), 1)
            # a másik kettőt nem kell, mert a felettünk és balra lévőnél már rajzoltuk

# elindítjuk a labirintus generálását 0,0 mezőtől, innen már rekurzívan meg fogja hívni magát a többi mezőre
genMaze(0,0)

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