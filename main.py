from graphics import Window
from objects import Point, Cell


def main():
    win = Window(800, 800)
    
    demo_cell = Cell(win)
    
    demo_cell.walls['top'] = False
    demo_cell.draw(Point(45, 50), Point(70, 80))

    win.wait_for_close()

main()