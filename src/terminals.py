#!/usr/bin/python

def turn(ant, world, direction):
    ant._direction = direction

def turnUp(ant, world):
    ant.turn(ant.UP)

def turnDown(ant, world):
    ant.turn(ant.DOWN)

def turnLeft(ant, world):
    ant.turn(ant.LEFT)

def turnRight(ant, world):
    ant.turn(ant.RIGHT)

def move(ant, world):
    x,y = ant.facing(ant.x + dx, ant.y + dy)
    if world.getLocation(x,y) is None:
        ant.x += dx
        ant.y += dy

def pickup(ant, world):
    food = world.getFoodAtLocation(*facing(ant))
    if food is not None:
        ant.holdingFood = True
        world.removeFood(food)

def senseFood(ant, world):
    food = world.getFoodAtLocation(*facing(ant))
    return food is not None

def drop(ant, world):
    if world.isNest(*facing(ant)):
        ant.holdingFood = False
        world.nest.addFood()

def atNest(ant, world):
    return world.isNest(*facing(ant))

def facingNest(ant, world):
    nest = world.nest
    nest_coords = nest.x, nest.y

    return (ant.up and nest.y < ant.y or
            ant.down and nest.y > ant.y or
            ant.left and nest.x < ant.x or
            ant.right and nest.x > ant.x)

def ifTerm(ant, world, *ops):
    cond, ifTrue, ifFalse = ops
    if cond():
        return ifTrue()
    else:
        return ifFalse()
