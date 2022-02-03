import random
import datetime
from mario_data import *
from log_generator import log

def get_controller(number):
    while True:
        control_num = round(random.random() * (len(players) - 1) + 1)
        if control_num in number:
            continue
        taken.append(control_num)
        return control_num


def get_character():
    rand_num = round(random.random() * len(characters) - 1)
    return characters[rand_num]


def get_cart():
    rand_num = round(random.random() * len(carts) - 1)
    return carts[rand_num]


def get_wheels():
    rand_num = round(random.random() * len(wheels) - 1)
    return wheels[rand_num]


def get_glider():
    rand_num = round(random.random() * len(gliders) - 1)
    return gliders[rand_num]

# returns a random number between 1 and 12
def get_random_cup():
    rand_num = round(random.random() * len(trophy_names) - 1)
    return trophy_names[rand_num]


if __name__ == "__main__":
    taken = []
    display = "------ Let's Play Mario -----\n"
    for player in players:
        display += f"""\
\t{player}
Controller: {get_controller(taken)}
Character: {get_character()}
Cart: {get_cart()}
Wheels: {get_wheels()}
Glider: {get_glider()}
------------------------------
"""
    display += f"Let's ride: {get_random_cup()}"
    print(display)
    input("Enter any key to continue... ")
    ratings = []
    for player in players:
        rating = input(f"Player {player} config rating (1-5): ")
        display += f"\nPlayer {player} config rating: {rating}"
        ratings.append(rating)
    display += f"\n{str(datetime.datetime.now())}\n"
    display += "*" * 60
    display += "\n\n\n" 
    if ratings[0] == ratings[1]:
        log(display, rating)
    else:
        log(display, ratings[0])
        log(display, ratings[1])
