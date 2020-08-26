import pygame
import mycritters

 
# Define some colors
white     = ( 255, 255, 255)
green     = (   0, 255,   0)
lightblue = (   0, 100, 255)
brown     = ( 125, 100, 100)
 

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[1000,1000]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Critters")

# Function to draw background scene
def draw_background():
    pygame.draw.rect(screen,brown,[0, 700, 1000, 300])
    pygame.draw.rect(screen,green,[0, 600, 1000, 100])
    pygame.draw.rect(screen,lightblue,[0, 0, 1000, 600])
    pygame.draw.ellipse(screen,white,[50, 80, 100, 60])
    pygame.draw.ellipse(screen,white,[120, 60, 180, 80])
    pygame.draw.ellipse(screen,white,[700, 80, 150, 60])
    
 
# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

critterlist = []

######################################
# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN: # If user wants to perform an action
            if event.key == pygame.K_c:
                newcaterpillar = mycritters.Caterpillar()
                critterlist.append(newcaterpillar)
        if event.type == pygame.KEYDOWN: # If user wants to perform an action
            if event.key == pygame.K_b:
                new_butterfly = mycritters.Butterfly()
                critterlist.append(new_butterfly)
        if event.type == pygame.KEYDOWN: # If user wants to perfobrm an action
            if event.key == pygame.K_s:
                for critter in critterlist:
                    critter.change_colour()
                    
    # Draw the background scene
    draw_background()
    # Draw the critters
    for critter in critterlist:
        critter.draw_critter(screen)
     
    # Limit to 20 frames per second
    clock.tick(50)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()