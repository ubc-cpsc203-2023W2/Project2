# Project 2: Cellular Automata. 

## The Game

In this project we will develop a platform for exploring grid-based simulations based on an approach 
commonly known as "cellular automata." Like Voronoi Diagrams and Markov Chains which we studied in 
class, cellular automata have broad applications across arts and sciences. Mathematicians and computer
scientists have made careers of studying their features, and they allow scholars from application areas 
as diverse as epidemiology
and traffic flow to assess innovations and policies. They are a powerful tool for experimentation, but 
they lend themselves to (fairly) simple implementation, so they're perfect for our project!

Classic examples of cellular automata include [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)
and [Cyclic CA](https://en.wikipedia.org/wiki/Cyclic_cellular_automaton). The final result of this assignment will
give you a general framework within which you can illustrate these two automata, in addition to many others.

## The Algorithm

### The general case
Consider a 2d grid, and imagine that every cell in the grid has a *state* at a particular point in time. A grid cell's
*next* state is determined by its current state, together with the states of its neighbors, based on a given *rule*. 

The illustration below shows a single time step for a cellular automata consisting of 64 cells in a grid. 
Each cell is in one of 3 states (white, green, and orange) in the first time step. The state of each cell in the next
time step is determined by a simple rule:
a cell takes the _most common color_ among its 8 neighbors. Most of
the cells will be white, but 45 and 55 will be orange (count for yourself to make sure you understand the rule!).

![time step illustration](timestep.png)

Note that in this example, another time step would yield an all white grid, and it would never change again in 
successive time steps.

In this project we will define two different rule sets. One corresponds to that of Conway's Game of Life, and the other
corresponds to the Cyclic CA. We encourage you to experiement with other rules, including the majority rule mentioned 
above. A little bit of research will give you about a bazillion different rules you might try.

Notice also that our example above assumed the set of neighbors was defined to be the 8 surrounding cells of a given cell. 
In the
project you will define functions that define the set of neighbors. In one, it's the set of 8, in another its the NWSE 
non-diagonal adjacent cells. We could easily redefine our definition of "neighbors" to include, for example, the 8 
surrounding cells, plus one more in each NWSE direction, for a total of 12 neighbors. 

Finally, the number of states is something that we set as a global variable. Conway's Game of Life uses 2 states, the Cyclic CA uses any number (and you will want to experiment with different values)!

### The initial state

In order to start a sequence of time steps, we must have someplace to start! The utility of a simulation can depend 
profoundly on its initial grid configuration. In this project we ask you to implement two functions that the simulation
can use to initialize the grid. In one case, the particular starting state gives fascinating results within Conway's GOL.
The second starting state simply generates a grid containing states uniformly chosen from the set of states.

## PyGame

Cellular automata in 2 dimensions is represented as a grid which evolves over time, and as such, it lends itself 
to animated visualization. For this task, we employ PyGame, a lightweight game engine for Python that makes windowing
and game state evaluation simple and accessible. In the given code you will see references to a few pygame functions 
whose role is to set up and administer the game window. You may largely ignore these functions, unless you would like
to learn just a little bit about how interactive graphics work, in general. 

## Examples

1. In this example we use the Conway's GOL rule on a 2-state grid of size 25 by 25 with an initial state that has a 
few non-zero 
entries in the upper left corner of the grid.

![glider](glider.gif)

2. The following example is exactly the same as the previous, except that we started the simulation with a random state in
every cell.

![random life](randLife.gif)

3. The last example uses cyclic rules (defined in the given code and on the wikipedia page above) on a grid of size 40 by 40
initialized randomly over 12 states.

![random cycle](cycle12rand.gif)

## The Structure

The Project contains three main files: `main.py`, `control.py`, and, `display.py`. These three files work together to run our game. 

The `main.py` file contain the main program loop that runs the game. It calls functions from both  `control.py` and `display.py`.

As the name suggests, `display.py` contains the display code. This is where most of our PyGame code is located.
You are not required (and should not) modify anything in `main.py` and `display.py`.

The only file you are required to modify and submit is `control.py`. This file contains all the game logic.


## Deliverables

### Part 1: Basic Code

You must complete all the requested code inside `control.py`. Our POTD this week and next will help you with these!

### Part 2: Creative Component (BONUS)

We would like you to experiment with the tool you have programmed by discovering your own interesting cellular automaton. 
Your discovery will require you to implement the following:

1. An initialization function that sets up the grid for the first iteration. 
2. A rule function.
3. A neighborhood function. 
4. A number of states.
5. A grid size. 

You may decide to use *one* of the elements that you defined for the previous part--the random initializer 
or the 8-neighbor set, for example. But you must define a new rule function.

To show us that you have completed this work, please post your result as a .gif to the EdStem forum, together with a 
brief writeup telling us what you did.

This will be worth some small bonus on your course grade.

## Handing in your work

Submit the `control.py` file to PrairieLearn.

## Good Luck!

## Optional resources
Here are some fun examples of cellular automaton application!
- [Simulating COVID-19 with Cellular Automata](https://towardsdatascience.com/simulating-covid-19-with-cellular-automata-aeb820910a9)
- [Zero Player Game](https://www.youtube.com/watch?v=N-BbgqOjIqk)








