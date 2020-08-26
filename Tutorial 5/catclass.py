import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

class caterpillar:
    def __init__(self, x, y):
        self.face_xcoord = x
        self.face_ycoord = y
        self.body = segment_queue()
        t = random.randrange(0,2)
        if t == 0:
            self.travel_direction = -1 #using a string for these in unnessecary
        else:
            self.travel_direction = 1 
        
    def display_caterpillar(self, screen):
        self.draw_face(screen)
        self.draw_body(screen)

    def draw_face(self, screen):
        x = self.face_xcoord 
        y = self.face_ycoord
        pygame.draw.ellipse(screen,red,[x, y, 40, 45])
        pygame.draw.ellipse(screen,black,[x+6, y+10, 10, 15])
        pygame.draw.ellipse(screen,black,[x+24, y+10, 10, 15])
        pygame.draw.line(screen,black, (x+11, y), (x+9, y-10), 3)
        pygame.draw.line(screen,black, (x+24, y), (x+26, y-10), 3)
        
    def draw_body(self, screen):
        # traverse the segment queue
        current_node = self.body.head
        while current_node is not None:
           current_node.draw_segment(screen) 
           current_node = current_node.next 

####### you need to complete these two methods

    def grow(self):
        #using length instead of coords requires less logic and is distance will be constant anyway
        #we can also change travel direction to a positive/negative int to determine direction without branching
        distance = 37 if self.body.length == 0 else (self.body.length) * 33 + 37
        self.body.addSegment(self.face_xcoord - self.travel_direction * distance, self.face_ycoord)


    def move(self):
        if self.body.length == 0: #if no body, don't move
            return
        current_node = self.body.head

        distance = self.travel_direction * 2
        self.face_xcoord += distance
        while current_node is not None:
            current_node.xcoord += distance
            current_node = current_node.next

        
        
class segment_queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
      
    def isEmpty(self):
        return self.length == 0
    
####### you need to complete this method
      
    def addSegment(self, x, y):

        segment = body_segment(x,y)
        if self.length == 0:
            self.head = segment
            self.last = segment
        else:
            self.last.next = segment
            self.last = segment
        self.length += 1
        # create a new body_segment node, with parameters x and y     
        # if segment queue is empty, the new node is both head and last
        # else, find the last node and then append the new node to the end of the queue
        # increment length of the segment queue
 
  
class body_segment:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.next = None
        
    def draw_segment(self, screen):
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen,green,[x, y, 35, 40])
        pygame.draw.line(screen,black, (x+8, y+35), (x+8, y+45), 3)
        pygame.draw.line(screen,black, (x+24, y+35), (x+24, y+45), 3)
        
