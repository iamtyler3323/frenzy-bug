#!/usr/bin/python
import random

class Ant(object):
    UP, DOWN, LEFT, RIGHT = range(4)

    def __init__(self, x, y,aiComponent):
        self.x = x
        self.y = y
        self.holdingFood = False
        self._direction = random.choice([Ant.UP, Ant.DOWN, Ant.LEFT, Ant.RIGHT])
        self.aiComponent = aiComponent


    @property
    def direction(self):
        if self._direction == Ant.UP:
            return 'Up'
        elif self._direction == Ant.DOWN:
            return 'DOWN'
        elif self._direction == Ant.LEFT:
            return 'Left'
        elif self._direction == Ant.RIGHT:
            return 'Right'
    
    @property
    def up(self):
        return self._direction == Ant.UP
    
    @property
    def down(self):
        return self._direction == Ant.DOWN

    @property
    def left(self):
        return self._direction == Ant.LEFT

    @property
    def right(self):
        return self._direction == Ant.RIGHT

    def facing(self):
        """Returns the coords of adjacent square the ant is facing."""

        if self._direction == ant.UP:
            dx = 0 
            dy = -1
        elif self._direction == ant.DOWN:
            dx = 0
            dy = 1
        elif self._direction == ant.LEFT:
            dx = -1
            dy = 0
        elif self._direction == ant.RIGHT:
            dx = 1
            dy = 0

        return (self.x + dx, self.y + dy)

    def update(self, world):
        self.aiComponent.update(self, world)

