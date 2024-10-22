import control
import display
from PIL import Image

def main():
    
    # Used to manage how fast the screen updates
    clock = display.startClock()
    
    # some variables you probably won't want to change
    frameCount = 0
    desiredGifLength = 200
    frameRate = 60
    frames = [] 
    
    # --- Initiate Grid
    # the game state is maintained in a grid object.
    # grid data values will be updated upon every click of the clock.
    # parameters are the (width, height) dimensions of the grid, and a
    # function that initializes the start state
    #g = grid((100, 150), randStart)
    g = control.grid((75,75), control.glideStart)
    
    while True: # runs continually until stopped
        
        # --- Main event loop
        display.handleInputEvents()

        # --- Draw the grid
        # this function loops over the data in the grid object
        # and draws appropriately colored rectangles.
        display.draw(g, control.states)
        
        # --- Game logic should go here
        # control.evolve( g, rule, neighbors)
        # g -- an object of type grid, previously initialized to hold data start state
        # rule -- a function that applies the game rule, given a cell state and a neighbor tally
        # neighbors -- a function that returns a list of neighbors relative to a given x,y position.
        # control.evolve(g, ruleCycle, neighborDiamond)
        control.evolve(g, control.ruleGOL, control.ruleGOL)
        
        # --- Mysterious reorientation that every pygame application seems to employ
        display.orientate()
        
        # --- Uncomment code below to save a GIF of your custom automaton
        # if frameCount < desiredGifLength:
        #     pygame.image.save(display.screen, "temp.png")
        #     frames.append(Image.open("temp.png"))
        # else:
        #     frames[0].save('custom.gif', format='GIF',
        #                    append_images=frames[1:], duration=1000/frameRate,
        #                    save_all=True, loop=0)
        # frameCount += 1

        # --- Limit to 60 frames per second
        clock.tick(frameRate)
        
main()