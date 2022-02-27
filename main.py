import sys

import pygame

from random import randint


# initialize pygame
pygame.init()

# variables initialize

 # screen size
width = 600
height = 400

 # bird positions
delta = width/25
xpos = 600-delta
ypos = height/3

 # bird speed
speed = 1

birds = []

# initialize main screen
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


# initialize objects to be drawn on the main screen
background_image = pygame.image.load("resources/green2.jpg")
tree = pygame.image.load("resources/tree2.png")

# more birds into a list
for number in range(10):
    birdpic = pygame.image.load("resources/bird.png")
# the bird: xpos, ypos, image, speed, counter, name
    counter = 0
    ypos = randint(height/10, height/2)
    speed = randint(1, 4)
    bird = {"xpos": xpos, "ypos": ypos, "bird": birdpic, "counter": counter, "name": "test", "speed": speed}
    birds.append(bird)

# start main loop for game to begin
while True:
    pass

#  A) check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))
    # update variables dynamically
    for bird in birds:
        bird["xpos"] = bird["xpos"] - bird["speed"]
        #  B) draw objects on screen
        screen.blit(bird["bird"], (bird["xpos"], bird["ypos"]))

    screen.blit(tree, (300, 100))
#  C) update display
    pygame.display.update()
    clock.tick(60)




