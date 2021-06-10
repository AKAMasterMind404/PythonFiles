import random


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        while True:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            if (x - self.x_center) ** 2 + (y - self.y_center) ** 2 <= self.radius ** 2:
                return [x, y]
