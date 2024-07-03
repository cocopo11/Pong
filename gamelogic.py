from gameobject import window_height as HEIGHT
from gameobject import window_width as WIDTH


class GameLogic:
    """
    Game logic of Pong game
    Attributes:
        - ball: A Ball object
        - paddle_left: A Paddle object positioned in left side
        - paddle_right: A Paddle object positioned in right side
    Methods:
        - reset(): resets ball and paddles
        - update(): updates the game board for the next frame
        - ball_falls_left(): returns True if ball exceeds the left side of the screen
        - ball_falls_right(): returns True if ball exceeds the right side of the screen
        - ball_hits_wall(): returns True if ball hits the top or bottom wall
        - ball_hits_paddle(): returns True if ball hits any of the paddles
    """
    def __init__(self, ball, paddle_left, paddle_right):
        self.ball = ball
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.reset()

    def reset(self):
        self.ball.reset()
        self.paddle_left.reset()
        self.paddle_right.reset()

    def ball_falls_left(self): # <-- TODO: complete this function. check if self.ball.position[0] goes below 0
        return False

    def ball_falls_right(self): # <-- TODO: complete this function. check if self.ball.position[0] exceeds WIDTH
        return False

    def ball_hits_wall(self): # <-- TODO: complete this function. check if self.ball.position[1] goes beyond 0 or HEIGHT
        return False

    def ball_hits_paddle(self):
        return self.ball.is_collision(self.paddle_left) or self.ball.is_collision(self.paddle_right)

    def update(self):
        self.ball.update()
        self.paddle_left.update()
        self.paddle_right.update()
        # <-- TODO: Complete the following
        """ 
        check the conditions for the following and apply appropriate actions:
        IF ball falls left
            - score of the right paddle goes up
            - resets game
        IF ball falls right
            - score of the left paddle goes up
            - resets game
        IF ball hits wall
            - Y-axis velocity (i.e., self.ball.velocity[1]) reverses
        IF ball hits paddle
            - X-axis velocity reverses
        """

