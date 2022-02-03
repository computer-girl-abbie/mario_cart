import random


trophy_names = [
    "Mushroom Cup",
    "Flower Cup",
    "Star Cup",
    "Special Cup",
    "Egg Cup",
    "Crossing Cup",
    "Shell Cup",
    "Banana Cup",
    "Leaf Cup",
    "Lightning Cup",
    "Triforce Cup",
    "Bell Cup",
]

# returns a random number 0-12 and adds one to avoid 0
rand_num = round(random.random() * len(trophy_names) - 1)
print(trophy_names[rand_num])
