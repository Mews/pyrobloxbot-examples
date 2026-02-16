import pyrobloxbot as bot
import random
import datetime

def move_randomly():
    directions = ["l", "r"]
    d = random.choice(directions)

    bot.jump()
    bot.walk(d, duration=1)

def setup_camera_angle():
    bot.toggle_shift_lock()
    bot.reset_player()
    bot.wait(5)

def raid_going_on():
    return bot.image_is_visible("bossbar.png")

def walk_to_factory_door():
    bot.walk_right(5)
    bot.jump(2)
    bot.walk_forward(2)
    bot.walk_right(1.5)
    bot.walk("f", "r", duration=12.5)

def kill_core():
    bot.walk("f", "r", duration=2.5)
    
    bot.equip_slot(2)
    bot.jump(3, interval=0.1)
    bot.press_key("z")

    bot.walk("f", "r", duration=1)

    bot.jump(4, interval=0.1)
    bot.walk("f", "r", duration=0.75)

    bot.equip_slot(3)
    
    for _ in range(100):
        bot.mouse_left_click()

def store_fruit():
    bot.equip_slot(6)
    bot.press_key("backspace")
    bot.wait(3)
    bot.ui_navigate("down", "up", "click")

    # Be absolutely sure the fruit finished storing
    # Because resetting will delete the fruit
    # Could also use image recognition for this
    bot.wait(5)

    bot.reset_player()


if __name__ == "__main__":
    setup_camera_angle()
    while True:
        while not raid_going_on():
            move_randomly()
            bot.wait(1)

        print(f"Raid started at: {datetime.datetime.now()}")

        bot.reset_player()
        bot.wait(5)

        walk_to_factory_door()

        bot.wait(15)

        kill_core()

        store_fruit()
