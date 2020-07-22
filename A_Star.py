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
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
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
        self.colour = WHITE

    # ** Set node state **

    def make_start(self):
        self.colour = ORANGE

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


# Data Structure creation
def make_grid(rows, width):
    grid = []
    gap = width // rows  # Gives the width of each Node based on the width of the page
    # Creat the list structure - List in List containing Nodes based on rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)  # new node(row, col, width, rows)
            grid[i].append(node)

    return grid


# draw grid lines
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))  # Draw line each horizontal line
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))  # Draw line each vertical line


def draw(win, grid, rows, width):
    win.fill(WHITE)  # Fill screen on new frame - normal for pygame

    # Loop through every node in list(row) in list(grid)
    for row in grid:
        for node in row:
            node.draw(win)  # Draw each node on the grid

    draw_grid(win, rows, width)  # Draw the grid on the page
    pygame.display.update()


# Node location for click
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    # Take pos of x , y and div by each of the cubes
    row = y // gap
    col = x // gap

    return row, col


# Main loop
def main(win, width):
    ROWS = 50  # Number of rows in the grip
    grid = make_grid(ROWS, width)  # Make the grid

    # Define start and end position
    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():  # Loop through events
            if event.type == pygame.QUIT:  # If the close button is pressed, break loop
                run = False

            # If algorithm running, don't allow changes to be made
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # If the left mouse button is pressed
                print("Left mouse clicked")
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)  # position in the game screen that was clicked
                node = grid[row][col]

                if not start and node != end: # If the start is not defined - set the clicked nod as start
                    start = node
                    start.make_start()

                elif not end and node != start:  # If end is not defined set node as end
                    end = node
                    end.make_end()

                elif node != end and node != start:  # If the start and end defined, set clicked node as barrier
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # If the right mouse button is pressed
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)  # position in the game screen that was clicked
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

    pygame.quit()


main(WIN, WIDTH)














