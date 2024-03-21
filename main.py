from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()