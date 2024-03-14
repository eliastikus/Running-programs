import os
import time
import psutil
import getpass
import pygetwindow as gw
from datetime import datetime
from data_save import save_data

def find_visible_windows():
    return set(gw.getAllTitles())

def find_opened_processes_in_taskbar(visible_windows):
    opened_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.name() in visible_windows:
                opened_processes.append(proc.name())
        except psutil.AccessDenied:
            pass
        except psutil.NoSuchProcess:
            pass
    return opened_processes

def monitor():
    user = getpass.getuser()
    visible_windows = find_visible_windows()

    while True:
        current_visible_windows = find_visible_windows()
        new_windows = current_visible_windows - visible_windows

        if new_windows:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(user, [{"program": window, "time": current_time} for window in new_windows])

        visible_windows = current_visible_windows
        time.sleep(1)

def main():
    while True:
        print(" 1. Start monitoring process")
        print(" 2. Delete data")
        print(" 3. Exit")

        user_input = int(input("Select option please: "))

        if user_input == 1:
            print("Monitoring was started. Press Ctrl+C to stop monitoring.")
            monitor()
        elif user_input == 2:
            if os.path.exists("data.json"):
                os.remove("data.json")
                print("Data deleted successfully.")
            else:
                print("No data to delete.")
        elif user_input == 3:
            break
        else:
            print("Wrong option, please select a correct one.")

if __name__ == "__main__":
    main()


__author__ = 'eliastikus'
__email__ = 'eliastikus@gmail.com'
