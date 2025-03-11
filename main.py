import control
import display

def main():
    
    # Used to manage how fast the screen updates
    clock = display.startClock()
    
    # some variables you probably won't want to change
    frame_count = 0
    frame_rate = 60
    
    # --- Initiate Grid
    # the game state is maintained in a grid object.
    # grid data values will be updated upon every click of the clock.
    g = control.WHICH_GRID
    display.initialize_screen(g)
    
    while True: # runs continually until stopped
        
        # --- Main event loop
        display.handleInputEvents()

        # --- Draw the grid
        # this function loops over the data in the grid object
        # and draws appropriately colored rectangles.
        display.draw(g, control.NUM_STATES)
        
        # --- Game logic should go here
        # control.evolve( g, rule, neighbors)
        # g -- an object of type grid, previously initialized to hold data start state
        # rule -- a function that applies the game rule, given a cell state and a neighbor tally
        # neighbors -- a function that returns a list of neighbors relative to a given x,y position.
        control.evolve(g, control.WHICH_RULE, control.WHICH_NEIGHBOR)
        
        # --- Mysterious reorientation that every pygame application seems to employ
        display.orientate()
        
        # --- Uncomment code below to save a GIF of your custom automaton
        if control.SAVE_ANIMATION:
            display.updateAnimation(frame_count, frame_rate)

        # --- Limit to 60 frames per second
        frame_count += 1
        clock.tick(frame_rate)
        
main()
