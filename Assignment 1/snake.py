"""
 Snake Game template, using classes.
 
 Derived from:
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import random
 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
 
# Screen size
height = 600
width = 600
 
# Margin between each segment
segment_margin = 3
 
# Set the width and height of each snake segment
segment_width = int(min(height, width) / 40 - segment_margin) #int() removes implicit conversion warnings
print(segment_width)
segment_height = int(min(height, width) / 40 - segment_margin) #int() removes implicit conversion warnings
 

class Food():
    def __init__(self):
        self.spriteslist = pygame.sprite.Group()

        for i in range(2):
            self.replenish()

    def replenish(self):
        item = Food_item()

        hit_list = pygame.sprite.spritecollide(item, my_snake.spriteslist, False) + pygame.sprite.spritecollide(item, ai_snake.spriteslist, False)
        if hit_list != []:
            self.replenish()
            return
        

        self.spriteslist.add(item)

class Food_item(pygame.sprite.Sprite):
    def __init__(self):
        # Set height, width
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)
 
        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()

        self.draw()

    def draw(self):

        x_offset = random.randrange(0, width / segment_width - 10)
        self.rect.x = int(x_offset * segment_width + x_offset * segment_margin) #int() removes implicit conversion warnings

        y_offset = random.randrange(0, width / segment_height - 10)
        self.rect.y = int(y_offset * segment_height + y_offset * segment_margin) #int() removes implicit conversion warnings

        hit_list = pygame.sprite.spritecollide(self, obstacles, False)
        if hit_list != []:
            self.draw()



class Snake():
    """ Class to represent one snake. """
    
    # Constructor
    def __init__(self, x_pos, y_pos):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(3):
            x = (segment_width + segment_margin) * x_pos  - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * y_pos
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)


        self.head = self.segments[0]

        # Set initial speed
        self.x_change = segment_width + segment_margin
        self.y_change = 0

    def grow(self):
        x_1 = self.segments[-1].rect.x
        y_1= self.segments[-1].rect.y

        x_2 = self.segments[-2].rect.x
        y_2= self.segments[-2].rect.y

        x = x_1 - x_2
        y = y_1 - y_2
        segment = Segment(x, y)

        self.segments.append(segment)
        self.spriteslist.add(segment)

        

            
    def move(self):
        global game_over
        # Figure out where new segment will be
        x = self.segments[0].rect.x + self.x_change
        y = self.segments[0].rect.y + self.y_change
        
        # Don't move off the screen
        # At the moment a potential move off the screen means nothing happens, but it should end the game
        if not(0 <= x <= width - segment_width and 0 <= y <= height - segment_height):  
            game_over = True
            return
    # Insert new segment into the list
        segment = Segment(x, y)
        self.segments.insert(0, segment)
        self.spriteslist.add(segment)
        self.head = segment
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
        old_segment = self.segments.pop()
        self.spriteslist.remove(old_segment)
    
    def ai_move(self):
        x = int(self.segments[0].rect.x + self.x_change)
        y = int(self.segments[0].rect.y + self.y_change)

        # Insert new segment into the list
        segment = Segment(x, y)
        self.segments.insert(0, segment)
        self.head = segment
        self.spriteslist.add(segment)

        if not(0 <= x <= width - segment_width and 0 <= y <= height - segment_height):  
            self.set_dir(random.randint(1,4))
            self.segments.remove(segment)
            self.spriteslist.remove(segment)
            self.ai_move()
            return

        for i in self.segments[1:]:
            if self.head.rect.colliderect(i.rect):
                self.set_dir(random.randint(1,4))
                self.segments.remove(segment)
                self.spriteslist.remove(segment)
                self.ai_move()
                return

        #doesn't TRY to eat food, but if it finds any it enjoyed a nice snack
        hit_list = pygame.sprite.spritecollide(self.head, food.spriteslist, True)
        if hit_list != []:
            food.replenish()
            self.grow()

        #we only need to check if the head collides with obstacles as all body parts follow the head.
        hit_list = pygame.sprite.spritecollide(self.head, obstacles, False)
        if hit_list != []:  
            self.set_dir(random.randint(1,4))
            self.segments.remove(segment)
            self.spriteslist.remove(segment)
            self.ai_move()
            return
        
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        old_segment = self.segments.pop()
        self.spriteslist.remove(old_segment)

    def set_dir(self, direction):
        if direction == 1: #left
            self.x_change = (segment_width + segment_margin) * -1
            self.y_change = 0
        if direction == 2: #right
            self.x_change = (segment_width + segment_margin)
            self.y_change = 0
        if direction == 3: #up
            self.x_change = 0
            self.y_change = (segment_height + segment_margin) * -1
        if direction == 4: #down
            self.x_change = 0
            self.y_change = (segment_height + segment_margin)



class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        # Set height, width

        size = random.randint(1, 3)
        
        obstacle_width = segment_width * size + (segment_margin) * (size - 1)
        obstacle_height = segment_height * size + (segment_margin) * (size - 1)

        self.image = pygame.Surface([obstacle_width, obstacle_height])
        self.image.fill(GREEN)

        self.draw()
        
    def draw(self):
        self.rect = self.image.get_rect()

        x_offset = random.randrange(0, width / segment_width - 12)
        self.rect.x = x_offset * segment_width + x_offset * segment_margin

        y_offset = random.randrange(0, width / segment_height - 12)
        self.rect.y = y_offset * segment_height + y_offset * segment_margin

        #checks obstacles do not collide with other obstacles OR the snake
        hit_list = pygame.sprite.spritecollide(self, obstacles, False) + pygame.sprite.spritecollide(self, my_snake.spriteslist, False)
        if hit_list != []:
            self.draw()
            


# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create a 600x600 sized screen
screen = pygame.display.set_mode([width, height + 50])
 
# Set the title of the window
pygame.display.set_caption('Snake Game')
 

obstacles = pygame.sprite.Group()

# Create the snakes
my_snake = Snake(30, 5)
ai_snake = Snake(10, 10)

#load 8 obstacles into the game in random positions
for i in range(8):
    obstacles.add(Obstacle())


#initalise food class 
food = Food()


#configure game-state variables to be accessed inside loop
score = 0
count = 0
clock = pygame.time.Clock()
done = False
game_over = False

#import font
font = pygame.font.SysFont("Calibri", 48)


while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the direction based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_snake.set_dir(1)
            if event.key == pygame.K_RIGHT:
                my_snake.set_dir(2)
            if event.key == pygame.K_UP:
                my_snake.set_dir(3)
            if event.key == pygame.K_DOWN:
                my_snake.set_dir(4)

    #game over screen
    if game_over:
        screen.fill(BLACK)

        text = font.render('Game Over, final score = ' + str(score), True, (255, 0, 0))

        # get the bounding box for the image
        textrect = text.get_rect()

        # set the position
        textrect.centerx = int(width/2)
        textrect.centery = height + 30

        # blit (copy) the image onto the screen
        screen.blit(text, textrect) 

        pygame.display.flip()

        continue

    # move snake one step
    my_snake.move()
    
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
    food.spriteslist.draw(screen)
    my_snake.spriteslist.draw(screen)
    obstacles.draw(screen)

    

    #display the current score

    #divider line for screen regions
    pygame.draw.line(screen, RED, (0, height), (width, height))

    # create an image (Surface) of the text
    text = font.render('Score = ' + str(score), True, (255, 0, 0))

    # get the bounding box for the image
    textrect = text.get_rect()

    # set the position
    textrect.centerx = int(width/2)
    textrect.centery = height + 30

    # blit (copy) the image onto the screen
    screen.blit(text, textrect) 

    snake_head = my_snake.head

    #check snake collisions that could cause game to end
    hit_list = pygame.sprite.spritecollide(snake_head, food.spriteslist, True)
    if hit_list != []:
        food.replenish()
        
        my_snake.grow()
        ai_snake.grow()
        score += 1

    #READ COMMENT BELOW
    #these are placed in this section of the code (not the classes) so that we can skip rendering an unnessecary frame. This is a small visual improvement but makes the game ending appear far nicer when you lose
    #we only need to check if the head collides with obstacles as all body parts follow the head.
    hit_list = pygame.sprite.spritecollide(snake_head, obstacles, True)
    if hit_list != []:
        game_over = True
        continue

    #checks for both if enemy snake runs into you, or if you run into enemy snake
    hit_list = pygame.sprite.spritecollide(snake_head, ai_snake.spriteslist, False) + pygame.sprite.spritecollide(ai_snake.head, my_snake.spriteslist, False)
    if hit_list != []:
        game_over = True
        continue
    
    for i in my_snake.segments[1:]:
        if snake_head.rect.colliderect(i.rect):
            game_over = True
            break
    

    count += 1
    if count % 10 == 0:
        ai_snake.set_dir(random.randint(1,4))

    ai_snake.ai_move()
    ai_snake.spriteslist.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(10)

pygame.quit()
