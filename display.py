import pygame
from PIL import Image
import numpy as np # we'll use numpy arrays as the basis for our grids. 
import sys
import control

# Parameters for saving a GIF animation.
ANIMATION_FRAME_COUNT = 200
ANIMATION_FILENAME = 'cellular.gif'
ANIMATION_FRAMES = []

# Define some colors, mostly useful for testing
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# drawing parameters that determine the look of the grid when it's shown.
# These can be set, but defaults are probably fine
CELL_SIZE = 5  # size of the squares in pixels
CELL_PAD = CELL_SIZE // 5 # the number of pixels between each square

# function initialize_screen
# purpose: Create a window of appropriate size for the grid.
def initialize_screen(g):
    # Width, Height.
    global WINDOW_SIZE
    WINDOW_SIZE = ((CELL_SIZE + CELL_PAD) * g.gridSize[0] + CELL_PAD,
                   (CELL_SIZE + CELL_PAD) * g.gridSize[1] + CELL_PAD)

    # Give the window a name.
    pygame.display.set_caption("CPSC203 Life")

    # initializes the display window
    global SCREEN
    SCREEN = pygame.display.set_mode(WINDOW_SIZE)
    
# function draw_block
# purpose: draw a rectangle of color acolor for *grid* location x,y.
# returns: nothing
def draw_block(x, y, acolor):
    pixel_x = (CELL_SIZE + CELL_PAD) * x + CELL_PAD
    pixel_y = (CELL_SIZE + CELL_PAD) * y + CELL_PAD
    pygame.draw.rect(SCREEN, acolor, [pixel_x, pixel_y, CELL_SIZE, CELL_SIZE])

# function: draw
# purpose: translates the game representation from the grid, to an image on the screen
# param: gr, a grid. for every position in gr.data, computes a color based on the state
# in that location, and then makes a call to draw_block to place that color into the pygame
# screen. Also passes the grid location so draw_block can compute the correct screen location.
# The new color is represented in HSVA (see https://www.pygame.org/docs/ref/color.html#pygame.Color.hsva
# and has hue h = (360 // states) * current state, s = 100, and v = 50 (we just left A of HSVA 
# at its default value). You may want to experiment with these values for artistic effect. :)
# returns: nothing
def draw(g, states):
    for y in range(g.gridSize[0]):
        for x in range(g.gridSize[1]):
            state = g.data[x][y]
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

def updateAnimation(frame_count, frame_rate):
    if frame_count < ANIMATION_FRAME_COUNT:
        ANIMATION_FRAMES.append(Image.frombytes('RGB', WINDOW_SIZE, pygame.image.tobytes(SCREEN, 'RGB')))
    else:
        ANIMATION_FRAMES[0].save(ANIMATION_FILENAME, format='GIF',
                                 append_images=ANIMATION_FRAMES[1:], duration=1000/frame_rate,
                                 save_all=True, loop=0)
        sys.exit(0)
