import random
import numpy
from maze import width, height, is_uncarved, directions

# constants
searched = [0.9, 0.1, 0.1]
solved = [0.1, 0.1, 0.9]

def is_searched(node):
    return (node == searched).all()

class SearchAlgorithm:

    def __init__(self, grid, recorder, add, pop, get_directions):
        self.grid = numpy.array(grid)
        self.recorder = recorder
        self.add = add
        self.pop = pop
        self.get_directions = get_directions

    def mark_grid(self, pos, marking):
        self.grid[pos[0]][pos[1]] = marking
        self.recorder.record_frame(self.grid)

    def can_visit(self, position):
        # out of bounds bro
        if position[0] < 0 or position[0] >= width or position[1] < 0 or position[1] >= height:
            return False
        # You can't step here!
        if is_uncarved(self.grid[position[0]][position[1]]):
            return False
        # We've been here before!
        if is_searched(self.grid[position[0]][position[1]]):
            return False

        return True

    def search(self, curr, dest):
        parents = {curr: None}
        frontier = []
        self.add(frontier, curr, dest)
        self.mark_grid(curr, searched)

        while len(frontier) > 0:
            curr = self.pop(frontier)

            if curr == dest:
                # mark solution
                while curr != None:
                    self.mark_grid(curr, solved)
                    curr = parents[curr]
                return True

            for d in self.get_directions():
                new_x = curr[0] + d[0]
                new_y = curr[1] + d[1]
                new_pos = (new_x, new_y)
                if self.can_visit(new_pos):
                    parents[new_pos] = curr
                    self.add(frontier, new_pos, dest)
                    self.mark_grid(new_pos, searched)
        return False

def DepthFirstSearch(grid, recorder):
    def add(frontier, item, dest):
        frontier.append(item)

    def pop(frontier):
        return frontier.pop()

    def get_directions():
        random.shuffle(directions)
        return directions

    return SearchAlgorithm(grid, recorder, add, pop, get_directions)

def BreadthFirstSearch(grid, recorder):
    def add(frontier, item, dest):
        frontier.append(item)

    def pop(frontier):
        return frontier.pop(0)

    def get_directions():
        return directions

    return SearchAlgorithm(grid, recorder, add, pop, get_directions)

def AStarSearch(grid, recorder):
    def add(frontier, item, dest):
        frontier.append(item)
        frontier.sort(key= lambda x : (dest[0] - x[0])**2 + (dest[1] - x[1])**2 )

    def pop(frontier):
        return frontier.pop(0)

    def get_directions():
        return directions

    return SearchAlgorithm(grid, recorder, add, pop, get_directions)

