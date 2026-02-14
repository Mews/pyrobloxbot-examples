import pyrobloxbot as bot
import keyboard

if __name__ == "__main__":
    bot.options.force_focus = False

    keyboard.add_hotkey("u", lambda:bot.chat("/spec"))
    keyboard.add_hotkey("i", lambda:bot.chat("/serverlist"))
    keyboard.add_hotkey("o", lambda:bot.chat("/style"))

    while True:
        bot.wait(0.1)
