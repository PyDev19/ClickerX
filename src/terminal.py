import os, sys, termios

def reset_terminal() -> None:
    # Reset the terminal
    os.system("reset")

def lock_terminal():
    # Get the terminal attributes
    attrs = termios.tcgetattr(sys.stdin)

    # Set the terminal to non-canonical mode
    attrs[3] &= ~termios.ICANON

    # Set the terminal to echo off mode
    attrs[3] &= ~termios.ECHO

    # Apply the new terminal attributes
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, attrs)

def unlock_terminal():
     # Get the terminal attributes
    attrs = termios.tcgetattr(sys.stdin)

    # Enable canonical mode
    attrs[3] |= termios.ICANON

    # Enable echoing of input characters
    attrs[3] |= termios.ECHO

    # Apply the new terminal attributes
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, attrs)
