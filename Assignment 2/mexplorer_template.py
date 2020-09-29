import pygame
import mazeclass

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid =  [[2,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,2],
             [2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,2],
             [2,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,2],
             [2,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,2],
             [2,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,2],
             [2,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,2],
             [2,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,2],
             [2,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,2],
             [2,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,2],
             [2,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,2],
             [2,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,2],
             [2,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,2],
             [2,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# Some (silly) sample code for moving one step forward and backward

def forwardbackward(curpos):
    # Warm up at the current position
    moveto(curpos, 3)
    moveto(curpos, 3)
    # Look for positions that can be visited
    neighbourlist = unvisitedneighbours(curpos)    
    if neighbourlist != []:        
        # Select the first position that can be visited
        newpos = neighbourlist[0]      
        # Go to that position
        moveto(newpos, 3)
        # Warm up at the new position
        moveto(newpos, 4)
        # Move back
        moveto(curpos, 4)

def unvisitedneighbours(curpos):
    # Return list of unvisited positions that can be reached from current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status == 0:
                    free.append(newpos)     
    return free

def visitedneighbours(curpos):
    # Return list of unvisited positions that can be reached from current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status == 0 or the_maze.grid[newpos[0]][newpos[1]].status == 3:
                    free.append(newpos)     
    return free

def moveto(newpos, status, movebot=True):
    # Mark the new position as being visited
    the_maze.grid[newpos[0]][newpos[1]].status = status
    # If required, move to the new position
    if movebot:
        the_maze.bot_xcoord = newpos[0]
        the_maze.bot_ycoord = newpos[1]
    # Wait a bit and then display the current state of the maze
    pygame.time.delay(30)
    the_maze.display_maze(screen)
    pygame.display.flip()
    pygame.event.pump()
    
# Code to be implemented


def depthfirsttraversal(curpos, previous_path=[]):
    # Do a depth-first traversal of all unvisited neighbours
    
    neighbourlist = unvisitedneighbours(curpos)
    moveto(curpos, 3)
    # print(neighbourlist)
    if len(neighbourlist) > 0:    
        for neighbour in neighbourlist:

            moveto(neighbour, 3)
            
            depthfirsttraversal(neighbour)

            moveto(curpos,4)
    else:
        moveto(curpos, 4)


def depthfirstsearch(curpos):
    # Perform a depth-first search to find the exit
    pass

def breadthfirstsearch(curpos):
    # Perform a breadth-first search to find the exit
    pass

def tokencollection(curpos):
    # Collect all tokens in topological order
    pass

# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_f:
                    the_maze.reset(mazegrid)
                    forwardbackward((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    depthfirsttraversal((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_s:
                    the_maze.reset(mazegrid)
                    depthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_b:
                    the_maze.reset(mazegrid)
                    breadthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_t:
                    the_maze.reset(mazegrid)
                    the_maze.display_tokens()
                    tokencollection((the_maze.bot_xcoord, the_maze.bot_ycoord))
                         
        the_maze.display_maze(screen)
        # Limit to 50 frames per second
        clock.tick(50)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()