import json
from os.path import exists

def display_all(player_name):
    file_name = f"config_log/{player_name.lower()}.json"
    if exists(file_name):
        with open(file_name, "r") as file:
            json_object = json.load(file)
        print(json.dumps(json_object, indent = 2))
    else:
        print("Player file not found.")


if __name__ == "__main__":
    player_name = input("Enter player name: ")
    display_all(player_name.lower())
