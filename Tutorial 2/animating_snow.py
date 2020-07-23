"""
 Animating multiple objects using a list.
 based on Sample Python/Pygame Programs
 Simpson College Computer Science
 
"""

# Import libraries 'pygame' and 'random'
import pygame
import random

# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

#colours for snowflakes

GREEN = [0, 255, 0]
RED = [255, 0, 0]
CYAN = [0, 255, 255]
MAGENTA = [255, 0, 255]
TEAL = [0, 128, 128]

COLOUR_LIST = [GREEN, RED, CYAN, MAGENTA, TEAL]

# Set the height and width of the screen
SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# Create an empty list
snow_list = []

# Loop 100 times and add a snow flake in a random x,y position
for i in range(100):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    colour = random.choice(COLOUR_LIST)
    snow_list.append([x, y, colour])

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
count = 0

def recolour_snowflake(snow_flake):
    snow_flake[2] = random.choice(COLOUR_LIST)
    return snow_flake

def keep_snowflake(snow_flake):
    if snow_flake[1] < 0 and random.randrange(30) == 0:
        return False
    return True

while True: #Using True instead of done saves unnessecary loop after completion and assigments

    #handle exit condition first so no unnesecary code is run
    if pygame.QUIT in map(lambda x: x.type, pygame.event.get()): #tidier than nested loops
        break #break out of the look when user closes the game

    snow_list = list(filter(keep_snowflake, snow_list)) #removes snowflakes over time
    if len(snow_list) == 0: #exit game if no snowflakes are left
        break

    #SHOULD BE down the bottom of the loop so we aren't changing colour unnessecarily on first loop - following instructions. Not starting loop at 1 intentionally because of instructions
    if count % 5 == 0: #every 5th iteration change colour
        snow_list = list(map(recolour_snowflake, snow_list)) 
    # Set the screen background
    screen.fill(BLACK)

    # Process each snow flake in the list
    for i in range(len(snow_list)):
    
        # Draw the snow flake
        pygame.draw.circle(screen, snow_list[i][2], snow_list[i][:2], 3)

        # Move the snow flake down one pixel
        snow_list[i][1] += random.randint(1,3)

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

    count +=1  

# If you forget this line, the program will 'hang' on exit.
pygame.quit()