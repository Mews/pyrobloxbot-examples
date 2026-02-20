import pyrobloxbot as bot
import time

def is_in_server():
    return bot.image_is_visible("index_button.png")


def join_server_and_wait():
    tank_game_id = 119789365111500
    bot.join_game(tank_game_id)

    while is_in_server():
        pass

    bot.wait_for_image("index_button.png")


def move_for_4_minutes():
    start_time = time.perf_counter()
    while (time.perf_counter() - start_time) < 4*60:
        bot.walk_left(1)
        bot.walk_right(1)


def open_tab_and_collect_rewards():
    bot.toggle_ui_navigation()
    bot.ui_navigate("down", "click", "left", "left", "click", "left", "click", "left", "click")
    # No need to toggle it back off, we're leaving the server right after

if __name__ == "__main__":
    total_diamonds = 0
    while True:
        join_server_and_wait()
        move_for_4_minutes()
        open_tab_and_collect_rewards()

        total_diamonds += 1250
        print("Diamonds farmed:", total_diamonds)
