from ball import Ball


class BallGUI(Ball):
    """
    Extends Ball class
    Attributes:
        - canvas: A tkinter Canvas object that draws the game objects
        - gui_obj: An oval draw object inside the canvas representing the Ball
    Methods:
        - update(): updates the ball position in the canvas
    """
    def __init__(self, canvas=None):
        super().__init__()
        self.canvas = canvas
        self.gui_obj = self.canvas.create_oval(0, 0, self.size[0], self.size[1], fill="red")
        self.canvas.moveto(self.gui_obj, self.position[0], self.position[1])

    def update(self):
        super().update()
        self.canvas.moveto(self.gui_obj, self.position[0], self.position[1])
