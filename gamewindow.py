from gamelogic import GameLogic
from gamelogic import WIDTH
from gamelogic import HEIGHT
from paddlegui import PaddleGUI
from ballgui import BallGUI
from tkinter import *
import time


class GameWindow(GameLogic):
    def __init__(self):
        tk = Tk()
        tk.title("pong")
        self.canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bd=0, bg='papaya whip')
        self.paddle_left = PaddleGUI(self.canvas, side='left')
        self.paddle_right = PaddleGUI(self.canvas, side='right')
        self.ball = BallGUI(self.canvas)
        self.canvas.pack()
        tk.update()
        self.tk = tk
        super().__init__(self.ball, self.paddle_left, self.paddle_right)
        self.game_loop()

    def update(self):
        super().update()
        self.tk.update_idletasks()
        self.tk.update()

    def game_loop(self):
        while True:
            self.update()
            time.sleep(0.01)
