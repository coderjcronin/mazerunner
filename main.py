from graphics import Window
from maze import Maze
from objects import Point

SCREEN_X = 800
SCREEN_Y = 800
COLS = 12
ROWS = 12
MARGIN = 50

def main():
    win = Window(SCREEN_X, SCREEN_Y)

    cell_size_x = abs((SCREEN_X - 2 * MARGIN) // COLS)
    cell_size_y = abs((SCREEN_Y - 2 * MARGIN) // ROWS)
    cell_size = Point(cell_size_x, cell_size_y)

    origin_point = Point(MARGIN, MARGIN)

    maze = Maze(origin_point, ROWS, COLS, cell_size, win, 2)

    maze.solve()
    
    win.wait_for_close()
    

main()