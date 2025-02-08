

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
            )
        
class Cell():
    def __init__(self, window, pos1 = Point(), pos2 = Point()):
        self._window = window
        self.walls = { 'top' : True, 'right' : True, 'bottom' : True, 'left' : True}
        self._pos1 = pos1
        self._pos2 = pos2
        self.visited = False

    def draw(self, pos1=False, pos2=False):
        if pos1:
            self._pos1 = pos1
        if pos2:
            self._pos2 = pos2

        top_line = Line(Point(self._pos1.x, self._pos1.y), Point(self._pos2.x, self._pos1.y))
        right_line = Line(Point(self._pos2.x, self._pos1.y), Point(self._pos2.x, self._pos2.y))
        bottom_line = Line(Point(self._pos1.x, self._pos2.y), Point(self._pos2.x, self._pos2.y))
        left_line = Line(Point(self._pos1.x, self._pos1.y), Point(self._pos1.x, self._pos2.y))

        top_color, right_color, bottom_color, left_color = "white", "white", "white", "white"
        if self.walls['top']:
            top_color = "black"
        if self.walls['right']:
            right_color = "black"
        if self.walls['bottom']:
            bottom_color = "black"
        if self.walls['left']:
            left_color = "black"

        self._window.draw_line(top_line, top_color)
        self._window.draw_line(right_line, right_color)
        self._window.draw_line(bottom_line, bottom_color)
        self._window.draw_line(left_line, left_color)

    
    def draw_move(self, to_cell, undo=False):
        source_x = abs((self._pos1.x + self._pos2.x) // 2)
        source_y = abs((self._pos1.y + self._pos2.y) // 2)
        dest_x = abs((to_cell._pos1.x + to_cell._pos2.x) // 2)
        dest_y = abs((to_cell._pos1.y + to_cell._pos2.y) // 2)
        draw_line = Line(Point(source_x, source_y), Point(dest_x, dest_y))

        line_color = "red"
        if undo:
            line_color = "gray"

        self._window.draw_line( draw_line, line_color)