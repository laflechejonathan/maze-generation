import numpy
import random

# constants
width = height = 50
uncarved = [0.1, 0.1, 0.1]
carved = [0.9, 0.9, 0.9]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
start = (1, 1)
end = (width - 2, height - 2)

def is_carved(node):
    return (node == carved).all()

def is_uncarved(node):
    return (node == uncarved).all()

def get_open_field():
    grid = numpy.ones(shape=(width,height, 3))

    for x in range(0, width):
        for y in range(0, height):
            grid[x][y] = carved

    return grid

def get_uncarved_grid():
    grid = numpy.ones(shape=(width,height, 3))

    for x in range(0, width):
        for y in range(0, height):
            grid[x][y] = uncarved

    grid[0][0] = grid[0][1] = grid[1][0] = carved
    grid[width - 1][height - 1] = grid[width - 1][height - 2] = grid[width - 2][height - 1] = carved

    return grid

class Maze:

    def __init__(self, recorder):
        self.grid = get_uncarved_grid()
        self.recorder = recorder
        self.generate_maze(start)

    def mark_grid(self, pos, marking):
        self.grid[pos[0]][pos[1]] = marking
        self.recorder.record_frame(self.grid)

    def is_pos_carved(self, pos):
        return is_carved(self.grid[pos[0]][pos[1]])

    def is_pos_uncarved(self, pos):
        return is_uncarved(self.grid[pos[0]][pos[1]])


    # count carved neighbors for a given node
    def count_neighbors(self, x, y):
        neighbors = 0
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if new_x < width and new_y < height:
                if self.is_pos_carved((new_x, new_y)):
                    neighbors += 1
        return neighbors

    def generate_maze(self, pos):
        if pos[0] >= width - 1 or pos[1] >= height - 1 or pos[0] <= 0 or pos[1] <= 0:
            return False

        # too many neighbors
        if(self.count_neighbors(*pos)) > 1 and pos != start:
            if pos[0] < width - 3 or pos[1] < height - 3:
                return False

        # We've been here before! We're going in circles!
        if is_carved(self.grid[pos[0]][pos[1]]):
            return False

        # mark carved
        self.mark_grid(pos, carved)

        # At the end of the maze!
        if pos == end:
            return True

        # recurse into random neighbors
        is_end_reached = False
        random.shuffle(directions)
        for index in xrange(0, len(directions)):
            d = directions[index]
            new_x = pos[0] + d[0]
            new_y = pos[1] + d[1]
            self.generate_maze((new_x, new_y)) or is_end_reached

        return is_end_reached
