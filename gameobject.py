
window_width = 600
window_height = 400


class GameObject:
    """
    A GameObject in 2D space.
    X-axis direction: left-to-right, Y-axis direction: top-to-bottom
    Attributes:
        - position: (x, y)
        - size: (width, height)
        - velocity: (vx, vy)
    Methods:
        - update(): updates position applying velocity
        - is_collision(obj2): returns True if the current object collides with obj2
        - get_border_points(): returns (x1, y1, x2, y2) where (x1,y1) is the starting point of the object is (x1, y1) and the stopping point of the object is (x2, y2)
    """
    def __init__(self, position, size, velocity):
        self.position, self.size, self.velocity = position, size, velocity

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def get_border_points(self):
        # start point
        x1, y1 = self.position[0], self.position[1]
        x2, y2 = x1 + self.size[0], y1 + self.size[1]
        return x1, y1, x2, y2

    def is_collision(self, obj2):
        ax1, ay1, ax2, ay2 = self.get_border_points()
        bx1, by1, bx2, by2 = obj2.get_border_points()
        return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1
