import json
from os.path import exists

def log(data):
    file_name = f"config_log/{data['player_name'].lower()}.json"

    if exists(file_name):
        with open(file_name) as file:
            file_content = json.load(file)

        file_content.append(data)

        with open(file_name, "w") as file:
            json_object = json.dumps(file_content, indent = 2)
            file.write(json_object)
    else:
        with open(file_name, "w") as file:
            data_list = []
            data_list.append(data)
            json_object = json.dumps(data_list, indent = 2)
            file.write(json_object)

if __name__ == "__main__":
    log("sample text", 1)
