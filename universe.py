import pygame
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

# screen

WIDTH = 1100
SCREEN_WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Universe")
fps = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
font = pygame.font.SysFont("", 30, True)

mousePosX = 0
mousePosY = 0
BL = False
BR = False
BM = False


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (128, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 247, 0)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
PURPLE = (164, 66, 245)
GREENISH = (92, 153, 119)
BLUEISH = (127, 202, 235)

planets = [pygame.image.load('pictures/planet1.png'), pygame.image.load('pictures/planet2.png'),
           pygame.image.load('pictures/planet3.png'), pygame.image.load('pictures/planet4.png'),
           pygame.image.load('pictures/planet5.png'), pygame.image.load('pictures/planet6.png'),
           pygame.image.load('pictures/planet7.png'), pygame.image.load('pictures/planet8.png')]
for i in range(len(planets) - 2):
     planets[i] = pygame.transform.scale(planets[i], (50, 50)).convert_alpha()

planets[7] = pygame.transform.scale(planets[7], (100, 100)).convert_alpha()
planets[6] = pygame.transform.scale(planets[6], (70, 60)).convert_alpha()

purpleStarDust = pygame.transform.scale(pygame.image.load('pictures/purplestardust.png'), (50,50))
blueStarDust = pygame.transform.scale(pygame.image.load('pictures/bluestardust.png'), (50,50))

spaceship = pygame.transform.scale(pygame.image.load('pictures/spaceship.png'), (60, 60)).convert_alpha()

graphsBFS = [pygame.transform.scale(pygame.image.load('pictures/move' + str(i) + '.png'), (500, 260)).convert_alpha() for i in range(1,11)]
graphsBaBS = [pygame.transform.scale(pygame.image.load('pictures/moveb' + str(i) + '.png'), (710, 350)).convert_alpha() for i in range(1,14)]

heuristic11 = font.render("11", 1, BLACK)
heuristic8 = font.render("8", 1, BLACK)
heuristic12 = font.render("12", 1, WHITE)
heuristic21 = font.render("21", 1, BLACK)
heuristic20 = font.render("20", 1, WHITE)
heuristic22 = font.render("22", 1, BLACK)

NEXT = font.render("NEXT", 1, BLACK)
CHANGE = font.render("Change", 1, BLACK)

BFS = font.render("BFS", 1, BLACK)
BaBS = font.render("Branch and Bound Search", 1, BLACK)

queue = [pygame.image.load('pictures/m' + str(i) + '.png').convert_alpha() for i in range(1,12)]


expandingBaBS = [pygame.image.load('pictures/mb' + str(i) + '.png').convert_alpha() for i in range(1,14)]


S = font.render("S", 1, WHITE)
A = font.render("A", 1, WHITE)
B = font.render("B", 1, WHITE)
C = font.render("C", 1, WHITE)
D = font.render("D", 1, WHITE)
E = font.render("E", 1, WHITE)
F = font.render("F", 1, WHITE)
G = font.render("G", 1, WHITE)

b11 = font.render("11", 1, BLUEISH)
b6 = font.render("6", 1, BLUEISH)
b8 = font.render("8", 1, BLUEISH)
b10 = font.render("10", 1, BLUEISH)
b7 = font.render("7", 1, BLUEISH)
b9 = font.render("9", 1, BLUEISH)




# mouse
mouse_pos_x = 0
mouse_pos_y = 0
BL = True  # Left button pressed
BR = True  # Right button pressed


def mouseAction(mouse_pos_x, mouse_pos_y, BL, BR):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        (BL, BM, BR) = pygame.mouse.get_pressed()
    return (mouse_pos_x, mouse_pos_y, BL, BR)

def makeColors():
    colors = [BLUEISH for _ in range(13)]
    if(algorithm == 'BFS'):
        if(move == 1):
            colors[10] = RED
        elif (move == 2):
            colors[6] = RED
        elif (move == 3):
            colors[7] = RED
        elif (move == 4):
            colors[10] = RED
            colors[9] = RED
        elif (move == 5):
            colors[10] = RED
            colors[8] = RED
        elif (move == 6):
            colors[6] = RED
            colors[5] = RED
        elif (move == 7):
            colors[7] = RED
            colors[8] = RED
        elif (move == 8):
            colors[7] = RED
            colors[12] = RED
            colors[3] = RED
            colors[11] = RED
        elif (move == 9):
            colors[7] = RED
            colors[12] = RED
            colors[3] = RED
            colors[11] = RED
        elif (move == 10):
            colors[7] = RED
            colors[12] = RED
            colors[3] = RED
            colors[11] = RED
    if (algorithm == 'BaBS'):
        if (move == 1):
            colors[10] = RED
        elif (move == 2):
            colors[6] = RED
        elif (move == 3):
            colors[7] = RED
        elif (move == 4):
            colors[10] = RED
            colors[8] = RED
        elif (move == 5):
            colors[10] = RED
            colors[9] = RED
        elif (move == 6):
            colors[7] = RED
            colors[8] = RED
        elif (move == 7):
            colors[7] = RED
            colors[12] = RED
            colors[3] = RED
            colors[11] = RED
        elif (move == 8):
            colors[7] = RED
            colors[12] = RED
            colors[3] = RED
            colors[11] = RED
        elif (move == 9):
            colors[7] = RED
            colors[12] = RED
            colors[3] = RED
            colors[11] = RED
        elif (move == 10):
            colors[6] = RED
            colors[5] = RED
        elif (move == 11):
            colors[10] = RED
            colors[9] = RED
            colors[5] = RED
        elif (move == 12):
            colors[10] = RED
            colors[9] = RED
            colors[4] = RED
    return colors
def drawPlanets():
    screen.blit(planets[0], (100, 100)) #ljubicasta
    screen.blit(planets[1], (150, 250)) #plava
    screen.blit(planets[2], (50, 400)) #zelena
    screen.blit(planets[3], (400, 400)) #crvena
    screen.blit(planets[4], (600, 400)) # siva
    screen.blit(planets[5], (650, 150)) # narandzasta
    screen.blit(planets[6], (450, 100)) # jupiter
    screen.blit(planets[7], (465, 230)) # lime

    screen.blit(blueStarDust, (200, 400))
    screen.blit(purpleStarDust, (300, 150))

    screen.blit(heuristic11, (113, 115))
    screen.blit(heuristic8, (169, 270))
    screen.blit(heuristic12, (410, 415))
    screen.blit(heuristic20, (610, 415))
    screen.blit(heuristic22, (473,120))
    screen.blit(heuristic21, (503,270))

    screen.blit(A, (485, 240))
    screen.blit(B, (645, 400))
    screen.blit(C, (410, 380))
    screen.blit(D, (455, 90))
    screen.blit(E, (145, 250))
    screen.blit(F, (85, 90))
    screen.blit(G, (30, 400))
    screen.blit(S, (640, 140))

    #pygame.draw.circle(screen, GREENISH, (50, 430), 30)
    return

def drawLines():
    colors = makeColors()
    pygame.draw.line(screen, colors[0], (125, 150), (75, 400), 5) #roze - zelena
    pygame.draw.line(screen, colors[1], (150, 150), (175, 250), 5) #roze - plava
    pygame.draw.line(screen, colors[2], (100, 400), (175, 300), 5) # zelena - plava
    pygame.draw.line(screen, colors[3], (115, 415), (200, 415), 5) #zelena - Bstardust
    pygame.draw.line(screen, colors[4], (190, 300), (390, 425), 5)  # plava - crvena
    pygame.draw.line(screen, colors[5], (460, 425), (590, 425), 5)  # crvena - siva
    pygame.draw.line(screen, colors[6], (625, 390), (675, 200), 5)  # siva - narandzasta
    pygame.draw.line(screen, colors[7], (650, 175), (500, 150), 5)  # narandzasta - jupiter
    pygame.draw.line(screen, colors[8], (490, 165), (515, 245), 5)  # jupiter - lime
    pygame.draw.line(screen, colors[9], (455, 410), (515, 300), 5)  # crvena - lime
    pygame.draw.line(screen, colors[10], (655, 195), (540, 260), 5)  # narandzasta - lime
    pygame.draw.line(screen, colors[11], (465, 145), (350, 165), 5)  # jupiter - Pstardust
    #pygame.draw.line(screen, BLUEISH, (250, 400), (330, 200), 5)  # stardusts

    #main screen
    pygame.draw.line(screen, WHITE, (700, 0), (700, 500), 3)

    xpos = 250
    ypos = 420
    for i in range(20):
        xpos += (330-250)//20
        ypos += (200-420)//20
        pygame.draw.line(screen, colors[12], (xpos, ypos), (xpos + (330-250)//40, ypos + (200-420)//40), 5)  # stardusts

    screen.blit(b11, (60, 250))
    screen.blit(b6, (170, 200))
    screen.blit(b8, (140, 350))
    screen.blit(b8, (240, 350))
    screen.blit(b7, (450, 350))
    screen.blit(b8, (530, 430))
    screen.blit(b9, (630, 280))
    screen.blit(b6, (595, 230))
    screen.blit(b7, (580, 140))
    screen.blit(b8, (480, 200))
    screen.blit(b10, (380, 130))

    #Button
    pygame.draw.rect(screen, GREEN, (701, 450, 400, 50))
    pygame.draw.line(screen, BLACK, (900,450), (900,500))
    screen.blit(NEXT, (765, 465))
    screen.blit(CHANGE, (950, 465))


def drawspaceship(spaceshipPosX, spaceshipPosY):
    screen.blit(spaceship, (spaceshipPosX, spaceshipPosY))

def drawGraphs():
    pygame.draw.rect(screen, WHITE, (700,0,400,450))
    if(algorithm == 'BFS'):
        if(move>10):
            screen.blit(graphsBFS[9], (700,10))
        else:
            screen.blit(graphsBFS[move-1], (700, 10))
    if (algorithm == 'BaBS'):
        if (move > 13):
            screen.blit(graphsBaBS[12], (600, 0))
        else:
            screen.blit(graphsBaBS[move - 1], (600, 0))

def writeAlgorithms():
    if algorithm == "BFS":
        screen.blit(BFS, (865, 10))
        if(move > 11):
            screen.blit(queue[10], (700,300))
            #screen.blit(expanding[10], (705,380))
        else:
            screen.blit(queue[move-1], (700, 300))
            #screen.blit(expanding[move-1], (705, 380))
    else:
        screen.blit(BaBS, (770, 10))
        if(move > 13):
            screen.blit(expandingBaBS[12], (700, 300))
        else:
            screen.blit(expandingBaBS[move-1], (700, 300))


spaceshipPosX = 0
spaceshipPosY = 0
spaceshipStartPosX = 0
spaceshipStartPosY = 0
spaceshipEndPosX = 0
spaceshipEndPosY = 0
algorithm = "BFS"
positionSet = False
iteration = 0
move = 1
stop = True

while True:
    mouse_pos_x, mouse_pos_y, BL, BR = mouseAction(mouse_pos_x, mouse_pos_y, BL, BR)
    #screen.fill(BLACK)
    screen.blit(background, (0,0))
    drawPlanets()
    drawLines()
    drawGraphs()
    writeAlgorithms()
    #(655, 195), (540, 260)

    if(algorithm == "BFS" and not stop):


        if move == 1 and not positionSet:
            spaceshipStartPosX = 630
            spaceshipStartPosY = 175
            spaceshipEndPosX = 515
            spaceshipEndPosY = 235
            positionSet = True

        if(move == 2) and not positionSet:
            spaceshipStartPosX = 650
            spaceshipStartPosY = 175
            spaceshipEndPosX = 600
            spaceshipEndPosY = 365
            positionSet = True


        if(move == 3) and not positionSet:
            spaceshipStartPosX = 625
            spaceshipStartPosY = 150
            spaceshipEndPosX = 475
            spaceshipEndPosY = 125
            positionSet = True


        if (move == 4) and not positionSet:
            spaceshipStartPosX = 490
            spaceshipStartPosY = 275
            spaceshipEndPosX = 430
            spaceshipEndPosY = 385
            positionSet = True

        if (move == 5) and not positionSet:
            spaceshipStartPosX = 490
            spaceshipStartPosY = 220
            spaceshipEndPosX = 465
            spaceshipEndPosY = 140
            positionSet = True

        if (move == 6) and not positionSet:
            spaceshipStartPosX = 565
            spaceshipStartPosY = 400
            spaceshipEndPosX = 435
            spaceshipEndPosY = 400
            positionSet = True

        if (move == 7) and not positionSet:
            spaceshipStartPosX = 475
            spaceshipStartPosY = 140
            spaceshipEndPosX = 490
            spaceshipEndPosY = 220
            positionSet = True

        if (move == 8) and not positionSet:
            spaceshipStartPosX = 440
            spaceshipStartPosY = 120
            spaceshipEndPosX = 325
            spaceshipEndPosY = 140
            positionSet = True

        if (move == 9) and not positionSet:
            spaceshipStartPosX = 305
            spaceshipStartPosY = 175
            spaceshipEndPosX = 225
            spaceshipEndPosY = 375
            positionSet = True

        if (move == 10) and not positionSet:
            spaceshipStartPosX = 175
            spaceshipStartPosY = 390
            spaceshipEndPosX = 90
            spaceshipEndPosY = 390
            positionSet = True
        if  move == 11 and not positionSet:
            stop = True


    if (algorithm == "BaBS" and not stop):

        if move == 1 and not positionSet:
            spaceshipStartPosX = 630
            spaceshipStartPosY = 175
            spaceshipEndPosX = 515
            spaceshipEndPosY = 235
            positionSet = True
        if (move == 2) and not positionSet:
            spaceshipStartPosX = 650
            spaceshipStartPosY = 175
            spaceshipEndPosX = 600
            spaceshipEndPosY = 365
            positionSet = True
        if (move == 3) and not positionSet:
            spaceshipStartPosX = 625
            spaceshipStartPosY = 150
            spaceshipEndPosX = 475
            spaceshipEndPosY = 125
            positionSet = True
        if (move == 4) and not positionSet:
            spaceshipStartPosX = 490
            spaceshipStartPosY = 220
            spaceshipEndPosX = 465
            spaceshipEndPosY = 140
            positionSet = True
        if (move == 5) and not positionSet:
            spaceshipStartPosX = 490
            spaceshipStartPosY = 275
            spaceshipEndPosX = 430
            spaceshipEndPosY = 385
            positionSet = True
        if (move == 6) and not positionSet:
            spaceshipStartPosX = 475
            spaceshipStartPosY = 140
            spaceshipEndPosX = 490
            spaceshipEndPosY = 220
            positionSet = True
        if (move == 7) and not positionSet:
            spaceshipStartPosX = 440
            spaceshipStartPosY = 120
            spaceshipEndPosX = 325
            spaceshipEndPosY = 140
            positionSet = True
        if (move == 8) and not positionSet:
            spaceshipStartPosX = 305
            spaceshipStartPosY = 175
            spaceshipEndPosX = 225
            spaceshipEndPosY = 375
            positionSet = True
        if (move == 9) and not positionSet:
            spaceshipStartPosX = 175
            spaceshipStartPosY = 390
            spaceshipEndPosX = 90
            spaceshipEndPosY = 390
            positionSet = True
        if (move == 10) and not positionSet:
            spaceshipStartPosX = 565
            spaceshipStartPosY = 400
            spaceshipEndPosX = 435
            spaceshipEndPosY = 400
            positionSet = True
        if (move == 11) and not positionSet:
            spaceshipStartPosX = 435
            spaceshipStartPosY = 400
            spaceshipEndPosX = 565
            spaceshipEndPosY = 400
            positionSet = True
        if (move == 12) and not positionSet:
            spaceshipStartPosX = 365
            spaceshipStartPosY = 400
            spaceshipEndPosX = 165
            spaceshipEndPosY = 275
            positionSet = True
        if  move == 13 and not positionSet:
            stop = True

    if (iteration < 100):
        spaceshipPosX = spaceshipStartPosX + iteration * (spaceshipEndPosX - spaceshipStartPosX) / 100
        spaceshipPosY = spaceshipStartPosY + iteration * (spaceshipEndPosY - spaceshipStartPosY) / 100
        if(not stop):
            drawspaceship(spaceshipPosX, spaceshipPosY)
            iteration += 1
    else:
        #changing this
        #stop = True
        iteration = 0
        move += 1
        positionSet = False

    (mousePosX, mousePosY) = pygame.mouse.get_pos()
    (BL, BM, BR) = pygame.mouse.get_pressed()

    if(BL and 700 <= mousePosX <= 900 and 450 <= mousePosY <= 500):
        stop = False

    if (BL and 900 <= mousePosX <= 1100 and 450 <= mousePosY <= 500):
        stop = True
        if algorithm == "BFS":
            algorithm = "BaBS"
        else:
            algorithm = "BFS"
        move = 1



    pygame.display.update()

    fps.tick(60)