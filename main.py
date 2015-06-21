import sys
from maze import Maze, start, end, get_open_field
from search import DepthFirstSearch, BreadthFirstSearch, AStarSearch
from animation import Recorder


def record_searches(recorder, grid):
    # DFS
    recorder.record_still_frame(grid, 100)
    dfs = DepthFirstSearch(grid, recorder)
    dfs.search(end, start)

    # BFS
    recorder.record_still_frame(grid, 100)
    bfs = BreadthFirstSearch(grid, recorder)
    bfs.search(end, start)

    # A*
    recorder.record_still_frame(grid, 100)
    a_star = AStarSearch(grid, recorder)
    a_star.search(end, start)

    recorder.record_still_frame(a_star.grid, 100)


def maze_fun(recorder):
    maze = Maze(recorder)
    record_searches(recorder, maze.grid)

def open_field_fun(recorder):
    open_field = get_open_field()
    record_searches(recorder, open_field)

def main():
    recorder = Recorder()

    maze_fun(recorder)
    open_field_fun(recorder)

    recorder.finish()
    # WARNING - saving animations is stupidly slow right now
    # recorder.save('generated_maze')
    recorder.show()




if __name__ == "__main__":
    sys.exit(main())

