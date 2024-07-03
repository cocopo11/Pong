from gameobject import GameObject
from gameobject import window_width as WIDTH
from gameobject import window_height as HEIGHT

class Paddle(GameObject):
    """
    A Paddle in Pong game
    Attributes:
        - score: score of the paddle
    Methods:
        - reset(): resets paddle position and velocity
    """
    def __init__(self, position=[0, 200-35], size=[10, 70], velocity=[0, 0]):
        super().__init__(position=position, size=size, velocity=velocity)
        self.score = 0

    def reset(self):
        self.velocity[1] = 0
        if self.position[0] < WIDTH//2:
            self.position[:] = [0, HEIGHT//2 - self.size[1]//2]
        else:
            self.position[:] = [WIDTH - 1 - self.size[0], HEIGHT//2 - self.size[1]//2]

