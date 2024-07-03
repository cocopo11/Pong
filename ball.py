from gameobject import GameObject
from gameobject import window_width as WIDTH
from gameobject import window_height as HEIGHT
import random


class Ball(GameObject):
    """
    The Ball in Pong game
    Methods:
        - reset(): resets position and velocity of the ball
    """
    def __init__(self, position=[100, 100], diameter=15, velocity=[-2, -3]):
        super().__init__(position=position, size=[diameter, diameter], velocity=velocity)

    def reset(self):
        self.position[:] = [WIDTH//2, HEIGHT//2]
        self.velocity = [random.choice([-2, 2]), random.choice([-3, 3])]
