import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
yellow   = ( 255,   255, 0)
purple   = ( 200,   0, 255)
blue     = (   0,   0, 255)
lightblue = (100, 100, 255)
gray     = ( 100, 100, 100)

class Cell:
    def __init__(self, status):
        self.status = status

class Maze:
    def __init__(self, mazegrid):
        # set maze cells
        self.rows = len(mazegrid)
        self.columns = len(mazegrid[0])
        self.grid = []
        for row in range(self.rows):
            self.grid.append([])
            for column in range(self.columns):
                newcell = Cell(mazegrid[row][column])
                self.grid[row].append(newcell) 
        # choose random non-wall position for Theseus  
        self.bot_xcoord = random.randrange(1, self.rows-1)
        self.bot_ycoord = random.randrange(1, self.columns-1)
        while self.grid[self.bot_xcoord][self.bot_ycoord].status != 0:
            self.bot_xcoord = random.randrange(1, self.rows-1)
            self.bot_ycoord = random.randrange(1, self.columns-1)
        self.tokens = []
        for i in range(5):
            xcoord = random.randrange(1, self.rows-1)
            ycoord = random.randrange(1, self.columns-1)
            while self.grid[xcoord][ycoord].status != 0:
                xcoord = random.randrange(1, self.rows-1)
                ycoord = random.randrange(1, self.columns-1)
            self.tokens.append((xcoord, ycoord, random.choice([1,2,3])))
        self.show_tokens = False
             
    def reset(self, mazegrid):
        # reset the maze cells
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid[row][column] = Cell(mazegrid[row][column])
        # choose random non-wall position for Theseus   
        self.bot_xcoord = random.randrange(1, self.rows-1)
        self.bot_ycoord = random.randrange(1, self.columns-1)
        while self.grid[self.bot_xcoord][self.bot_ycoord].status != 0:
            self.bot_xcoord = random.randrange(1, self.rows-1)
            self.bot_ycoord = random.randrange(1, self.columns-1)
        self.show_tokens = False
            
    def display_tokens(self):
        self.show_tokens = True

    def display_maze(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[row][column].status == 0:
                    self.draw_plainsquare(screen, row, column)
                elif self.grid[row][column].status == 1:
                    self.draw_wallsquare(screen, row, column)
                elif self.grid[row][column].status == 2:
                    self.draw_perimsquare(screen, row, column)
                elif self.grid[row][column].status == 3:
                    self.draw_visitedsquare(screen, row, column)
                elif self.grid[row][column].status == 4:
                    self.draw_revisitedsquare(screen, row, column)
                elif self.grid[row][column].status == 5:
                    self.draw_exitsquare(screen, row, column)
        if self.show_tokens:
            for token in self.tokens:
                x_coord = token[0]
                y_coord = token[1]
                level = token[2]
                self.draw_token(screen, x_coord, y_coord, level)
        self.draw_bot(screen, self.bot_xcoord, self.bot_ycoord)

    def draw_plainsquare(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen,white,[j * (1000 / columns), i * (500 / rows), 
                                       (1000 / columns), (500 / rows)])
        
    def draw_wallsquare(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen,gray,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
       
    def draw_perimsquare(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen,gray,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
     
    def draw_visitedsquare(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen,yellow,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
        pygame.draw.ellipse(screen,lightblue,[j * (1000 / columns) + (1000 / (columns * 3)), 
                                         i * (500 / rows) + (500 / (rows * 3)), 
                                         (1000 / (columns * 3)), (500 / (rows * 3))])
        
    def draw_revisitedsquare(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen,lightblue,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
        pygame.draw.rect(screen,yellow,[j * (1000 / columns) + (1000 / (columns * 3)), 
                                         i * (500 / rows) + (500 / (rows * 3)), 
                                         (1000 / (columns * 3)), (500 / (rows * 3))])

    def draw_exitsquare(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen,black,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
    
    def draw_token(self, screen, i, j, level):
        rows = self.rows
        columns = self.columns
        if level == 1:
            pygame.draw.rect(screen,red,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
        elif level == 2:
            pygame.draw.rect(screen,yellow,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
        else:
            pygame.draw.rect(screen,green,[j * (1000 / columns), i * (500 / rows), 
                                        (1000 / columns), (500 / rows)])
    
    def draw_bot(self,screen, i, j):
        rows = self.rows
        columns = self.columns
        #Removed white rect behind bot so that you can see the colour behind it, and because it caused visual 'bugs' (didn't look good when it ran over blocks it'd already ran over and had white background)
        # pygame.draw.rect(screen,white,[j * (1000 / columns), i * (500 / rows), 
        #                                 (1000 / columns), (500 / rows)])
        pygame.draw.ellipse(screen,red,[j * (1000 / columns) + (1000 / (columns * 10)), 
                                         i * (500 / rows) + (500 / (rows * 10)), 
                                         ((1000 * 4)/ (columns * 5)), ((500 *4) / (rows * 5))])
        pygame.draw.ellipse(screen,black,[j * (1000 / columns) + (1000 / (columns * 4)), 
                                         i * (500 / rows) + (500 / (rows * 3)), 
                                         ((1000 * 1)/ (columns * 5)), ((500 * 1) / (rows * 5))])
        pygame.draw.ellipse(screen,black,[j * (1000 / columns) + ((1000 * 4) / (columns * 7)), 
                                         i * (500 / rows) + (500 / (rows * 3)), 
                                         ((1000 * 1) / (columns * 5)), ((500 * 1) / (rows * 5))])   

    
