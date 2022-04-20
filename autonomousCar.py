import pygame
import random
import threading

pygame.init()
win = pygame.display.set_mode((1150, 620))
pygame.display.set_caption("Autonomous Car")
x = 0
y = 0

width = 30
height = 50

# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True
moveDown = False
decreaseSpeed = False
dcnt = 0
cnt = 0
# infinite loop
# colour = (0,0,255)
def color():
    #print("Called!")
    threading.Timer(10.0, color).start()
    colour = random.choice([(255, 0, 0), (0, 255, 0)])
    #print(colour)
    return colour
colour = color()
print(colour)
while run:
    if moveDown and y < 620 - height:
        pygame.time.delay(500)
        if decreaseSpeed and y>0:
            y = y + 2 - dcnt
            # print(y)
        else:
            y = y + 5 + cnt
    # print(cnt)
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1200 - width:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        moveDown=False
        y -= vel

    if keys[pygame.K_DOWN] and y < 620 - height:
        moveDown=True
        pygame.time.delay(500)
        y = y + 10

    if keys[pygame.K_SPACE] and y < 620 - height:
        moveDown = True
        decreaseSpeed = False
        pygame.time.delay(500)
        cnt = cnt + 5
        dcnt = 0
        #y = y + 10 + cnt

    if keys[pygame.K_BACKSPACE] and y < 620 - height:
        # moveDown=True
        print(dcnt)
        decreaseSpeed = True
        cnt = 0
        pygame.time.delay(500)
        if dcnt<=1:
            dcnt = dcnt+1
        if dcnt==1:
            y = y
        else:
            y = y + 2 - dcnt
        # pygame.time.delay(500)

        #y -= 2

    # completely fill the surface object
    win.fill((0, 0, 0))

    # with black colour

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    pygame.draw.line(win, (211, 211, 211),
                     [200, 550],
                     [200, 0], 25)
    pygame.draw.line(win, (211, 211, 211),
                     [400, 620],
                     [400, 75], 25)
    pygame.draw.line(win, (211, 211, 211),
                     [600, 550],
                     [600, 0], 25)
    pygame.draw.line(win, (211, 211, 211),
                     [800, 620],
                     [800, 75], 25)
    pygame.draw.line(win, (211, 211, 211),
                     [1000, 550],
                     [1000, 0], 25)
    pygame.draw.line(win, (211, 211, 211),
                     [1175, 620],
                     [1175, 0], 25)
    pygame.draw.rect(win, (255, 255, 255), (212, 275, 177, 40))
    pygame.draw.rect(win, (255, 255, 0), (0, 425, 188, 20))
    pygame.draw.rect(win, (255, 255, 0), (413, 425, 175, 22))
    pygame.draw.rect(win, (255, 255, 0), (812, 200, 177, 22))
    # pygame.draw.circle(win, (255,0,0), (625, 150), 5)
    pygame.draw.circle(win, colour, (625, 150), 5)

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()