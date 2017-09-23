import math
import os
import random

health = 100
agility = 50
strength = 10


def hit(health, agility, strength):
    h = health - int(random.randint(0, 10) * (agility / 100 + 1)) - strength
    # print(h)
    return h


def fight():
    health_of_zombie = 50
    number_of_zombie = 1
    while health_of_zombie > 0:
        health_of_zombie = hit(health_of_zombie, agility, strength)
        print(health_of_zombie)


fight()
