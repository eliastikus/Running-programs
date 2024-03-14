"""

:authors: eliastikus
:copyright: (c) 2024 eliastikus

"""
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

def main():
    user = getpass.getuser()
    visible_windows = find_visible_windows()

    while True:
        current_visible_windows = find_visible_windows()
        new_windows = current_visible_windows - visible_windows

        if new_windows:
            print("Newly opened windows:")
            for window in new_windows:
                print(window)
                
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(user, [{"program": window, "time": current_time} for window in new_windows])

        visible_windows = current_visible_windows
        time.sleep(1)

if __name__ == "__main__":
    main()


__author__ = 'eliastikus'
__email__ = 'eliastikus@gmail.com'
