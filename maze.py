from objects import Cell, Point
import random
import time

class Maze:
    def __init__(
            self,
            pos,
            num_rows,
            num_cols,
            cell_size,
            win,
            seed = None
    ):
        self._cells = []
        self._pos = pos
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win

        if seed is None:
            self._seed = random.seed()
        else:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_walls_r(0, 0)
        self._reset_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

        self._break_entrance_and_exit()


    def _break_entrance_and_exit(self):
        self._cells[0][0].walls['top'] = False
        self._cells[self._num_cols - 1][self._num_rows - 1].walls['bottom'] = False

        self._draw_cell(0,0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited: #left
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited: #right
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited: #up
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited: #down
                to_visit.append((i, j + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            which_way = random.randrange(len(to_visit))
            direction = to_visit[which_way]

            if direction[0] == i - 1: #left
                self._cells[i][j].walls['left'] = False
                self._cells[i - 1][j].walls['right'] = False
            if direction[0] == i + 1: #right
                self._cells[i][j].walls['right'] = False
                self._cells[i + 1][j].walls['left'] = False
            if direction[1] == j - 1: #up
                self._cells[i][j].walls['top'] = False
                self._cells[i][j - 1].walls['bottom'] = False
            if direction[1] == j + 1: #down
                self._cells[i][j].walls['bottom'] = False
                self._cells[i][j + 1].walls['top'] = False

            self._break_walls_r(direction[0], direction[1])

    def _reset_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._pos.x + i * self._cell_size.x
        y1 = self._pos.y + j * self._cell_size.y
        x2 = x1 + self._cell_size.x
        y2 = y1 + self._cell_size.y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.025)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows -1: # We Win!
            return True
        
        #Time to travel.. 
        if (
            i > 0 and
            not self._cells[i][j].walls['left'] and
            not self._cells[i - 1][j].visited
            #Left
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        if (
            i < self._num_cols and
            not self._cells[i][j].walls['right'] and
            not self._cells[i + 1][j].visited
            #Right
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (
            j > 0 and
            not self._cells[i][j].walls['top'] and
            not self._cells[i][j - 1].visited
            #Up
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if (
            j < self._num_rows and
            not self._cells[i][j].walls['bottom'] and
            not self._cells[i][j + 1].visited
            #Down
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False #Beep beep, whoops

    
    def solve(self):
        return self._solve_r(0, 0)        
    