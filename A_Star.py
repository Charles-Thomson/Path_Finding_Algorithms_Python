import pygame
import math
from queue import PriorityQueue

WIDTH = 800  # Width/Height
WIN = pygame.display.set_mode((WIDTH, WIDTH))  # Set up the display
pygame.display.set_caption("A* path finding Algorithm")

# Define the visual colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 244, 208)

class Node:
    def __init__(self, row, col, width, total_rows):
        # Row and col position
        self.row = row
        self.col = col

        self.x = col * width
        self.y = col * width

        self.colour = WHITE
        self.neighbours = []
        self.total_rows = total_rows

    # Get node position
    def get_pos(self):
        return self.row, self.col

    # ** Return node state **

    def is_closed(self):
        return self.colour == RED

    def is_open(self):
        return self.colour == GREEN

    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == ORANGE

    def is_end(self):
        return self.colour == TURQUOISE

    def reset(self):
        self.colour == WHITE

    # ** Set node state **

    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    # Draw the screen
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        pass

    # Less then, compare this and the Node
    def __lt__(self, other):
        return False


# Find the distance between point 1 and point 2 - Manhattan Distance
def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)








