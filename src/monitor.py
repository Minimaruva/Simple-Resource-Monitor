import psutil
import time
from datetime import datetime


def cpu_percent():
    return psutil.cpu_percent(interval=1)


def clear_screen():
    print("\033[H\033[J", end="") # ANSI escape code to clear screen

def pretty_print():
    print('='*50 + '\n='+' '*16+'Resource Monitor' + ' '*16+ '=\n'+'='*50)
    print(psutil.users())
    print(cpu_percent())
    print(psutil.virtual_memory())

    
if __name__ == '__main__':
    while True:
        pretty_print()
        time.sleep(1)
        clear_screen()

