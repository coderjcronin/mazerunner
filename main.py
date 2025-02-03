from graphics import Window
from objects import Point, Cell


def main():
    win = Window(800, 800)
    
    cell1 = Cell(win, Point(10,10), Point(30, 30))
    cell2 = Cell(win, Point(30,10), Point(50, 30))
    cell3 = Cell(win, Point(30,30), Point(50, 50))
    cell4 = Cell(win, Point(10,30), Point(30, 50))

    cell1.walls['right'] = False
    cell2.walls['left'], cell2.walls['bottom'] = False, False
    cell3.walls['top'], cell3.walls['left'] = False, False
    cell4.walls['right'] = False

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)
    cell4.draw_move(cell3, True)

    win.wait_for_close()

main()