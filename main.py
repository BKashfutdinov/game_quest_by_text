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


locations = ["Вы находитесь в пещере",
             "Вы находитесь на подводной лодке",
             "Вы находитесь в комнате без окон",
             "Вы находитесь в комнате с окнами",
             "Вы находитесь в поле",
             "Вы находитесь в лесу"]

loc = locations[random.randint(0, len(locations) - 1)]
action=1
while action!=0:
    print(loc)
    action=int(input("Что вы хотите сделать: 0-закончить; 1-начать драку; 2-сбежать в другую локацию"))
    print(action)

    if action==1:
        fight()
    elif action==2:
        loc=locations[random.randint(0, len(locations) - 1)]
    elif action==0:
        exit(0)
