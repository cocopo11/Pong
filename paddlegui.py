from paddle import Paddle
from paddle import HEIGHT
from paddle import WIDTH
from tkinter import NW, NE

class PaddleGUI(Paddle):
    """
    Extends Paddle class
    Attributes:
        - canvas: A tkinter Canvas object that draws the game objects
        - gui_obj: A rectangle draw_object inside the canvas representing the Paddle
        - score_label: A label draw_object inside the canvas to show score of the paddle
    Methods:
        - move_up(): handles event when user presses the UP key
        - move_down(): handles event when user presses DOWN key
        - update(): updates paddle position and score of the paddle
    """
    def __init__(self, canvas, side="left"):
        super().__init__(velocity=[0,0])
        self.canvas = canvas
        keys=[None, None]
        anchor = None
        if side == 'left':
            self.position = [0, HEIGHT//2-35]
            keys[:] = ['<w>', '<s>']  # 변경: 왼쪽 패들을 위한 키 설정
            anchor = NW

        if side == "right":
            self.position = [WIDTH-self.size[0], HEIGHT//2-35]
            keys[:] = ['<Up>', '<Down>']
            anchor = NE

        self.gui_obj = self.canvas.create_rectangle(0, 0, self.size[0], self.size[1], fill="black")
        self.canvas.moveto(self.gui_obj, self.position[0], self.position[1])
        self.canvas.bind_all(keys[0], self.move_up)
        self.canvas.bind_all(keys[1], self.move_down)
        self.score_label = self.canvas.create_text(self.position[0], 0, anchor=anchor, text=" Score: 0")

    def move_up(self, event):
        self.velocity[1] = -5  # 위로 이동하도록 속도를 설정
        self.position[1] += self.velocity[1]
        self.canvas.moveto(self.gui_obj, self.position[0], self.position[1])

    def move_down(self, event):
        self.velocity[1] = 5  # 아래로 이동하도록 속도를 설정
        self.position[1] += self.velocity[1]
        self.canvas.moveto(self.gui_obj, self.position[0], self.position[1])

    def update(self):
        super().update()
        self.velocity[1] = 0
        self.canvas.moveto(self.gui_obj, self.position[0], self.position[1])
        self.canvas.itemconfig(self.score_label, text=" Score: " + str(self.score))