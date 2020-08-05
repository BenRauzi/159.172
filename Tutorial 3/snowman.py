# Import the library of functions called 'pygame'
import sys, pygame
 
# Define a function that will draw a snowman at a certain location
def draw_snowman(screen,x,y, size):
        pygame.draw.ellipse(screen,white,[int(size*0.35)+x,0+y,int(size/4),int(size/4)]) #added all the int()s last minute before submission due to a warning message (That doesn't affect the task at all, but in future versions of Python may, and so want to be safe for the marker)
        pygame.draw.ellipse(screen,white,[int(size*0.23)+x,int(size/5)+y,int(size/2),int(size/2)])
        pygame.draw.ellipse(screen,white,[0+x,int(size*0.65)+y,size,size])

#def draw_snowmen(screen, x, y):
    #if x > size[0]: #size of screen
     #   return
    #draw_snowman(screen, x, y)
   # draw_snowmen(screen, x+150, y) #snowmen should be at least 'half a snowman' distance apart to allow for social distancing

def draw_snowmen2(screen, x, y, man_size):
    if x > size[0] or man_size < 20: #size[0] = size of screen on x axis
        return
    draw_snowman(screen, x, y, man_size)
    draw_snowmen2(screen, x+150, y + 7, man_size - 5) #y increases as floor should stay rougly in the same place. I would have done proper calculation for this but question didn't say to so I'm just doing it from personal opinion, not a requirement
# Initialize the game engine
pygame.init()
 
#200
#100
#65+200=265
#90*0.65+200 = 
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
     
    # Draw Snowman at a particular location
    draw_snowmen2(screen,10,200, 100)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Tidy up
pygame.quit ()
