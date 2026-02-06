import time
import random
from pynput.keyboard import Controller, Key

def type(text, error_rate=0.2):
    keyboard = Controller()

    # tentative
    adjacent_keys = {
        'a': 'swq', 'b': 'vghn', 'c': 'xvdf', 'd': 'sferx', 'e': 'rdsw',
        'f': 'dgrtv', 'g': 'fhtyb', 'h': 'gjuy n', 'i': 'ujko', 't': 'rfgy'
    }

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

        if char.lower() in adjacent_keys and random.random() < error_rate:
            wrong_char = random.choice(adjacent_keys[char.lower()])
            keyboard.type(wrong_char)
            time.sleep(random.uniform(0.1, 0.3))

            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            time.sleep(random.uniform(0.2, 0.5))

        keyboard.type(char)

# sample text
my_text = """Your text goes here. It will be typed out with human-like variability and pauses."""

type(my_text)