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


def display_data(data):
    print("----- Let's Play Mario -----")
    for item in data:
        print(f"\t {item['player_name']}")
        print(f"Controller: {item['controller']}")
        print(f"Character: {item['character']}")
        print(f"Cart: {item['cart']}")
        print(f"Wheels: {item['wheels']}")
        print(f"Glider: {item['glider']}")
        print("-" * 30)
    print(f"Let's ride: {data[0]['cup']} \n")


if __name__ == "__main__":
    taken = []
    data_list = []
    random_cup = get_random_cup()

    for player in players:
        config_data = {}
        config_data["player_name"] = f"{player}"
        config_data["controller"] = f"{get_controller(taken)}"
        config_data["character"] = f"{get_character()}"
        config_data["cart"] = f"{get_cart()}"
        config_data["wheels"] = f"{get_wheels()}"
        config_data["glider"] = f"{get_glider()}"
        config_data["cup"] = f"{random_cup}"
        data_list.append(config_data)

    display_data(data_list)

    input("Enter any key to continue... ")

    for i in range(0, len(players)):
        data_list[i]['rating'] = input(f"Player {data_list[i]['player_name']} config rating (1-5): ")
        log(data_list[i])
