

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
    def __init__(self, window):
        self._window = window
        self.walls = { 'top' : True, 'right' : True, 'bottom' : True, 'left' : True}

    def draw(self, point1, point2):
        self._pos1 = point1
        self._pos2 = point2
        if self.walls['top']:
            self._window.draw_line(
                Line(Point(self._pos1.x, self._pos1.y), Point(self._pos2.x, self._pos1.y))
            )
        if self.walls['right']:
            self._window.draw_line(
                Line(Point(self._pos2.x, self._pos1.y), Point(self._pos2.x, self._pos2.y))
            )
        if self.walls['bottom']:
            self._window.draw_line(
                Line(Point(self._pos1.x, self._pos2.y), Point(self._pos2.x, self._pos2.y))
            )
        if self.walls['left']:
            self._window.draw_line(
                Line(Point(self._pos1.x, self._pos1.y), Point(self._pos1.x, self._pos2.y))
            )