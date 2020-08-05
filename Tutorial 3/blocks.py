# Import the library of functions called 'pygame'
import sys, pygame

############################################################################################# 
# Define a function that will draw a stack of blocks at a certain location
# You need to update this function so that it draws a stack of blocks of the correct height
# currently ony one block is drawn

def draw_stack(screen,x,y, height): #ANCHOR point is the bottom block
    if height == 0:
        return

    #no else bock requied because if first conditional is true we will return

    draw_block(screen, x,y) #this maintains its own function for readability
    draw_stack(screen, x, y-26, height-1) #BLOCK height is 25. y-offset is 26 so we can see a gap.
    

##############################################################################################        
      
# Define a function that draws a single block at a particular location   
def draw_block(screen,x,y): 
    pygame.draw.rect(screen,white,[x,y,100,25])
        
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255,255,255]
blue = [ 0, 0,255]
green = [ 0,255, 0]
red = [255, 0, 0]

# Set the height and width of the screen
size=[1050,500]
screen=pygame.display.set_mode(size)
 
# Loop until the user clicks the close button.
done=False
clock = pygame.time.Clock()
 
 
while done==False:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    screen.fill(black)
     
    # Draw a stack of ten blocks at a particular location
    draw_stack(screen,200,300, 10)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Tidy up
pygame.quit ()
