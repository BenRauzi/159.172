import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
yellow   = ( 255,   255, 0)
purple   = ( 255,   0, 255)
brown    = ( 125, 100, 100)
blue     = (   0,   0, 255)

class Caterpillar:
    colour_scheme = [green, yellow, purple, blue] #these caterpillars are partially camoflaged. Best adapted to survive
    colour_scheme_2 = [yellow, purple, blue, black]

    def __init__(self):
        self.size = random.randint(0,3)
        x = random.randrange(50,950)
        y = random.randrange(600, 950)
        self.xcoord = x
        self.ycoord = y
        self.colours = self.colour_scheme

      
    def draw_critter(self, screen):
        x = self.xcoord 
        y = self.ycoord


        pygame.draw.ellipse(screen, self.colours[1], [x, y, 40, 45])
        for i in range(self.size + 1): #these caterpillars are fat so added more length - didn't change randint(0,3) because this was specified
             pygame.draw.ellipse(screen, self.colours[i], [x + 35 * (i), y, 40, 45])
        
        pygame.draw.ellipse(screen,black, [x+6, y+10, 10, 15])
        pygame.draw.ellipse(screen,black, [x+24, y+10, 10, 15])
        pygame.draw.line(screen,black, (x+11, y+1), (x+9, y-10), 3)
        pygame.draw.line(screen,black, (x+25, y+1), (x+26, y-10), 3)

    def change_colour(self):
        if self.colours == self.colour_scheme:
            self.colours = self.colour_scheme_2
        else:
            self.colours = self.colour_scheme       

#I could use inheritance here to make this better. I would any any language other than Python...
#but in Python it doesn't actually make it easier, it's just a mess.

class Butterfly: #these butterflies look bad but they are butterfiles!
    colour_scheme = [yellow, green, blue]
    colour_scheme_2 = [blue, purple, black]


    def __init__(self):
        self.size = random.randint(0,3)
        x = random.randrange(50,950)
        y = random.randrange(50, 500)
        self.xcoord = x
        self.ycoord = y
        self.colours = self.colour_scheme

    def draw_critter(self, screen):
        x = self.xcoord 
        y = self.ycoord


       
        
        for i in range(self.size):
            pygame.draw.ellipse(screen, self.colours[1], [x+ 30, y + 10 + 11 * i, 20, 15])
            pygame.draw.ellipse(screen, self.colours[2], [x - 10, y + 10 + 11 * i, 20, 15])
        
        pygame.draw.ellipse(screen, self.colours[0], [x, y, 40, 50])

        pygame.draw.ellipse(screen,black, [x+12, y+5, 6, 8])
        pygame.draw.ellipse(screen,black, [x+22, y+5, 6, 8])
        pygame.draw.line(screen,black, (x+15, y+1), (x+9, y-10), 2)
        pygame.draw.line(screen,black, (x+21, y+1), (x+26, y-10), 2)

    def change_colour(self):
        if self.colours == self.colour_scheme:
            self.colours = self.colour_scheme_2
        else:
            self.colours = self.colour_scheme       
            