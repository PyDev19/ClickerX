import ctypes

# Load the Windows API DLL
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Define constants for console mode flags
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

# Get the console handle
console_handle = kernel32.GetStdHandle(-11)  # -11 is the constant for stdout

def enable_vtp() -> None:
    """
    Enable virtual terminal processing to allow colored output in the console.

    Args: 
        None

    Returns: 
        None
    """
    
    # Get the current console mode
    mode = ctypes.c_ulong()
    kernel32.GetConsoleMode(console_handle, ctypes.byref(mode))

    # Enable virtual terminal processing
    mode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING

    # Set the new console mode
    kernel32.SetConsoleMode(console_handle, mode)

def disable_vtp() -> None:
    """
    Disable virtual terminal processing to prevent colored output in the console.

    Args: 
        None

    Returns: 
        None
    """
    
    # Get the current console mode
    mode = ctypes.c_ulong()
    kernel32.GetConsoleMode(console_handle, ctypes.byref(mode))

    # Enable virtual terminal processing
    mode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING

    # Set the new console mode
    kernel32.SetConsoleMode(console_handle, mode)
