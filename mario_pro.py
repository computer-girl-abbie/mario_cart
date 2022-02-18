import random
import datetime
from rich.console import Console
from rich.theme import Theme
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
    return random.choice(characters)


def get_cart():
    return random.choice(carts)


def get_wheels():
    return random.choice(wheels)


def get_glider():
    return random.choice(gliders)

# returns a random number between 1 and 12
def get_random_cup():
    return random.choice(list(trophy_names))


def display_data(data):
    console.print("Okie Dokie!", style="header", justify="center")
    print() # empty line
    for item in data:
        console.print(f"[u]{item['player_name']}[/u]", style="player", justify="center")
        console.print(f":joystick: {'Controller:':>15} [v]{item['controller']}[/v]", style="desc", justify="left")
        console.print(f":bust_in_silhouette: {'Character:':>14} [v]{item['character']}[/v]", style="desc", justify="left")
        console.print(f":racing_car: {'Cart:':>15} [v]{item['cart']}[/v]", style="desc", justify="left")
        console.print(f":white_circle: {'Wheels:':>14} [v]{item['wheels']}[/v]", style="desc", justify="left")
        console.print(f":kite: {'Glider:':>14} [v]{item['glider']}[/v]", style="desc", justify="left")
        print() # empty line
    console.print(f":chequered_flag: Let's Ride: {data[0]['cup']} :chequered_flag:", style="header", justify="center")


if __name__ == "__main__":
    custom_theme = Theme({
        "desc": "bold black on cornsilk1",
        "val": "bold dark_green on cornsilk1",
        "header": "bold cornsilk1 on red",
        "player": "bold cornsilk1 on dark_green",
        "prompt": "green",
        "text": "cornsilk1",
        "u": "underline",
        "p0": "green",
        "p1": "blue1",
        "repr.number": "bold dark_green",
    })
    console = Console(width=40, theme=custom_theme)

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

    console.input("\n[prompt]Press enter to continue...[/]:hourglass_not_done: ")

    for i in range(0, len(players)):
        data_list[i]['track_rank'] = {}

    print() # empty line
    console.print("Entering Ranks For Tracks", style="header", justify="center")
    for track in trophy_names[random_cup]:
        for i in range(0, len(players)):
            data_list[i]['track_rank'][track] = console.input(f"[p{i}]{data_list[i]['player_name']} --[/] [text]{track}:[/] ")
        console.rule(style="text")

    print() # empty line
    console.print("Entering Player Config Rating", style="header", justify="center")
    for i in range(0, len(players)):
        data_list[i]['rating'] = console.input(f"[text]Player [p{i}]{data_list[i]['player_name']}[/] config rating (1-5):[/] ")
        log(data_list[i])
