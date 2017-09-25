import math
import os
import random

health = 100
agility = 50
strength = 10


def hit(health, agility, strength):
    hit_strength = int(random.randint(0, 10) * (agility / 100 + 1)) + strength - defence(agility)
    # print(h)
    return health - hit_strength


def fight():
    health_of_zombie = 50
    number_of_zombie = 1
    do = {'1':hit, '2': defence, '3': escape}

    while health_of_zombie > 0:

        try:
            action_fight = int(input("1-ударить, 2-оборонятся, 3-попытаться убежать из боя"))
        except ValueError:
            action_fight = 3

        if action_fight == 1:
            health_of_zombie = hit(health_of_zombie, agility, strength)
        elif action_fight == 2:
            print("Попытка защититься")
        else:
            print("Вы пытаетесь убежать")
            escape()

        if health_of_zombie <= 0:
            print("Вы убили зомби")
        else:
            print("Вы ударили зомби, у него осталось", health_of_zombie, "здоровья")


def defence(a):
    defence_point = a // 5
    return defence_point

def escape():
    pass


locations = ["Вы находитесь в пещере",
             "Вы находитесь на подводной лодке",
             "Вы находитесь в комнате без окон",
             "Вы находитесь в комнате с окнами",
             "Вы находитесь в поле",
             "Вы находитесь в лесу"]

loc = locations[random.randint(0, len(locations) - 1)]
action = 1
while action != 0:
    print(loc)
    try:
        action = int(input("Что вы хотите сделать: 0-закончить; 1-начать драку; 2-сбежать в другую локацию"))
    except ValueError:
        action = 0
    print(action)

    if action == 1:
        fight()
    elif action == 2:
        loc = locations[random.randint(0, len(locations) - 1)]
        # elif action == 0:
        #    exit(0)
