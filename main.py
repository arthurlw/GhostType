import time
import random
from pynput.keyboard import Controller

def type(text):
    keyboard = Controller()

    print("Switch to your target window now...")
    time.sleep(3)

    for char in text:
        # uniform typing delay
        delay = random.uniform(0.05, 0.2)

        # pauses after punctuation
        if char in [',', '.', '!', '?']:
            delay += random.uniform(0.3, 0.8)

        if random.random() < 0.05:
            delay += random.uniform(1.0, 2.5)

        time.sleep(delay)
        keyboard.type(char)

# sample text
my_text = """Your text goes here. It will be typed out with human-like variability and pauses."""

type(my_text)