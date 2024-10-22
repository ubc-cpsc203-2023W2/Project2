import pygame
import numpy as np # we'll use numpy arrays as the basis for our grids. 
import sys
from typing import Tuple, List
from dataclasses import dataclass, field
import control

# Define some colors, mostly useful for testing
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# words to display on the window
pygame.display.set_caption("CPSC203 Life")

# drawing parameters that determine the look of the grid when it's shown.
# These can be set, but defaults are probably fine
sqSize = 3  # size of the squares in pixels
pad = sqSize // 5 # the number of pixels between each square

# computed from parameters above and grid g dimensions
s = (75, 75) # dimensions of pixels in screen window (width,height)

screen = pygame.display.set_mode(s)  # initializes the display window

# function draw_block
# purpose: draw a rectangle of color acolor for *grid* location x,y. Uses globals pad and sqSize.
# returns: nothing
def draw_block(x, y, acolor):
    pygame.draw.rect(screen, acolor, [x, y, sqSize, sqSize])

# function: draw
# purpose: translates the game representation from the grid, to an image on the screen
# param: gr, a grid. for every position in gr.data, computes a color based on the state
# in that location, and then makes a call to draw_block to place that color into the pygame
# screen. Also passes the grid location so draw_block can compute the correct screen location.
# The new color is represented in HSVA (see https://www.pygame.org/docs/ref/color.html#pygame.Color.hsva
# and has hue h = (360 // states) * current state, s = 100, and v = 50 (we just left A of HSVA 
# at its default value). You may want to experiment with these values for artistic effect. :)
# returns: nothing
def draw(gr, states):
    for y in range(np.size(gr.data, 0)):
        for x in range(np.size(gr.data, 1)):
            state = gr.data[x][y]
            col = pygame.Color(0,0,0)    
            h = (360 // states) * state
            col.hsva = (h, 100, 50)
            draw_block(x, y, col)

# Used to manage how fast the screen updates
def startClock():
    clock = pygame.time.Clock()
    return clock

# Reorientate screen
def orientate():
    pygame.display.flip()

# given: necessary for gracefully ending game loop (pygame)
def handleInputEvents():
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close...
            sys.exit(0)  # quit

