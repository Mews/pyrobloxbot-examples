import pyrobloxbot as bot
import random

def move_randomly(n_times):
    directions = ["f", "b", "l", "r"]
    for _ in range(n_times):
        d = random.choice(directions)
        bot.walk(d, duration=1)

while True:
    with bot.restore_focus():
        move_randomly(5)
    bot.wait(10)
