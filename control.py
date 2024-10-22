import numpy as np # we'll use numpy arrays as the basis for our grids. 
import sys
from typing import Tuple, List
from dataclasses import dataclass, field

# Set the number of states to use within each cell
states = 2  # we leave this as a global variable since it doesn't change.

# Things that can be changed: number of states, grid dimensions, square size,
# padding, neighbors function, rules function, grid initialization function.

class grid:
    # Updated on Mar 24, 2024 to reflect row-major
    # Note that numpy arrays create arrays in row-major order by default, which is opposite
    # You can read more about it here: https://numpy.org/doc/stable/glossary.html#term-row-major.
    gridSize: Tuple[int, int] # rows, columns == y,x
    data: np.ndarray 
    generations: int 

    def __init__(self, size, setup):
        self.gridSize = # YOUR CODE HERE! Where do we get the size we want for the grid?
        # YOUR CODE HERE...initialize data to the result of executing setup function on input size
        self.generations = 0


#--------------------------------------------------------------------
# Initialization functions -- used by the constructor. Only one is used
# in any game definition. You may add your own for the creative exercise.
#--------------------------------------------------------------------

# function: randStart
# Purpose: employed by grid __init__ (constructor) to give initial value to data
# param: size
# returns: an np array of size size, whose values are uniformly selected from range(states)
def randStart(size):
    # YOUR CODE HERE
    return

# function: glideStart
# Purpose: employed by grid __init__ (constructor) to give initial value to data
# param: size
# returns: an np array of size size, whose values are all zero, except for positions
# (2,0), (0,1), (2,1), (1,2), and (2,2), whose values are 1. Intended to be used
# on a game w 2 states.
def glideStart(size):
    # YOUR CODE HERE
    return

# --------------------------------------------------------------------
# Rule functions -- used by the evolve function. Only one is used
# in any game definition. You MUST add a new one for the creative exercise.
# --------------------------------------------------------------------

# function: ruleGOL
# purpose: applies a set of rules given a current state and a set of tallies over neighbor states
# params: cell, an element from range(states), where states is the global variable
#           tallies, tallies[k] = number of neighbors of state k, for all k in the range of states
# returns: a new state based on the classic rules of the game of life.
#           See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Note: assumes a two-state game, where 0 is "dead" and 1 is "alive"

def ruleGOL(cell, tallies):
    # YOUR CODE HERE
    return

# function: ruleCycle
# purpose: applies a set of rules given a current state and a set of tallies over neighbor states
# params: cell, an element from range(states), where states is the global variable
#           tallies, tallies[k] = number of neighbors of state k, for all k in the range of states
# returns: if k is the current state, returns k+1 if there is a neighbor of state k+1, else returns k

def ruleCycle(cell, tallies):
    # YOUR CODE HERE
    return


# --------------------------------------------------------------------
# Neighbor functions -- used by the evolve function. Only one is used
# in any game definition. You may add your own for the creative exercise.
# --------------------------------------------------------------------
# returns a list of neighbors in a square around x,y
def neighborSquare(x, y):
    # YOUR CODE HERE
    return

# returns a list of neighbors in a diamond around x,y (NWSE positions)
def neighborDiamond(x, y):
    # YOUR CODE HERE
    return


# function: tally_neighbors
# purpose: counts a given cell's the neighbors' states
# params: grid, an np array of data from a grid, containing states of all cells
#         position, the current cell position (a Tuple)
#         neighborSet, a function that when called on position x,y returns a list of x,y's neighbors
# returns: a list whose entries, tally[k] are the number of valid neighbors of x,y whose state is k.
# Note: neighborSet may not necessarily return *valid* neighbors. It's tally_neighbor's job to check
# for validity.

def tally_neighbors(grid, position, neighborSet):
    # YOUR CODE HERE
    return



# student: putting it all together.
# function: evolve
# purpose: to increment the automata by *one* time step. Given an array representing the automaton at the
# start of the time step (the start grid), this function creates an array for the end of the time step
# (the end grid) by applying the rule specified in function apply_rule to every position in the array.
# Note that all rule evaluation is done on the start grid, but the new state is set in the end grid.
# This function *changes* the input parameter to the new state. 
# The grid's generations variable should be incremented every time the function is called. (This variable
# may only be useful for debugging--there is a lot we *could* do with it, but our application doesn't use it.)
def evolve(gr, apply_rule, neighbors):
    # YOUR CODE HERE
    return


