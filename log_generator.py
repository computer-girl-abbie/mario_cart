def log(display, rating):
    filename = f"~/Projects/MarioCart/config_log/rating{rating}"

    with open(filename, "a") as file:
        file.write(display)


if __name__ == "__main__":
    log("sample text", 1)
