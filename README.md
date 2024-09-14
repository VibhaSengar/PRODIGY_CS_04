# PRODIGY_CS_04
This task is focused on creating a basic keylogger that captures and logs keystrokes on a system and saves them to a file. A keylogger is a program that records the keys pressed on a keyboard. The program should be used with ethical considerations, and only in environments where logging is permitted.

Pynput Library:

The pynput library is used to listen to keyboard events, making it possible to capture keystrokes in real-time. This library supports mouse and keyboard input events, but in this case, only keyboard events are of interest.
pip install pynput

Log File (log_file):

The keylogger logs all captured keystrokes into a file named key_log.txt.
This file will be created or appended to, depending on the execution of the program.
Key Writing Function (write_to_file):

This function processes the keys pressed and logs them into the log_file.
Special keys like space, enter, and others are handled separately:
Space (Key.space): Recorded as a space ' '.
Enter (Key.enter): Recorded as a newline '\n'.
Other special keys like shift, ctrl, and esc are ignored.
Key Press Listener (on_press):

This function listens for key press events.
Every time a key is pressed, it triggers the write_to_file function, which logs the key data.
Key Release Listener (on_release):

This optional function listens for key release events.
In this example, it is used to stop the keylogger if the ESC key is released, which effectively stops the program.
Listener Setup:

A Listener object is created, which listens for both key presses and key releases. The program runs in a loop, capturing all the keys until the ESC key is pressed.

Conclusion:
This simple keylogger captures keyboard inputs in real-time and logs them into a text file. It's an excellent example of how to use the pynput library to monitor system inputs but should always be implemented with ethical considerations.
