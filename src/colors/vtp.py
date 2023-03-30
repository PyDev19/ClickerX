import sys, termios, tty

def enable_vtp() -> None:
    """
    Enable virtual terminal processing to allow colored output in the console.

    Args: 
        None

    Returns: 
        None
    """
    
    # Enable virtual terminal processing
    if hasattr(termios, "VT220"):
        # Set the terminal to VT220 mode
        tty.setcbreak(sys.stdin.fileno(), termios.TCSANOW)
        
        # Enable virtual terminal processing
        sys.stdout.write('\x1b[?1h')
        sys.stdout.flush()

def disable_vtp() -> None:
    """
    Disable virtual terminal processing to prevent colored output in the console.

    Args: 
        None

    Returns: 
        None
    """
    attrs = termios.tcgetattr(sys.stdin)

    # Disable virtual terminal processing
    attrs[0] &= ~termios.ICANON
    attrs[3] &= ~(termios.ECHO | termios.ECHONL | termios.ICRNL | termios.INLCR | termios.IXON | termios.IXOFF)

    # Set the new terminal attributes
    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, attrs)
