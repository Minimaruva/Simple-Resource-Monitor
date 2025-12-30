import psutil
import time
from datetime import datetime


def cpu_percent():
    return psutil.cpu_percent()


def clear_screen():
    print("\033[H\033[J", end="") # ANSI escape code to clear screen

def pretty_print():
    cpu_p = cpu_percent()
    cpu_logical = psutil.cpu_count()
    memory = psutil.virtual_memory()
    memory_total = round(memory.total / (1024 ** 3), 2)
    memory_used = round(memory.used / (1024 ** 3), 2)

    clear_screen()
    print('='*50 + '\n='+' '*16+'Resource Monitor' + ' '*16+ '=\n'+'='*50)
    print(f"={' '*12}Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{' '*11}=")
    print('='*50+'\n'+'='*50)
    
    print(f"= CPU Usage: {cpu_p}% {' '*(7-len(str(cpu_p)))}|| CPU Cores (Logical): {cpu_logical} =")
    print(f"={'-'*48}=")

    print(f"= Memory Used: {memory_used} out of {memory_total} GB {' '*(22-len(str(memory_total)+str(memory_used)))}=")
    print(f"={'-'*48}=")

    print("=" * 50 + '\n')



    
if __name__ == '__main__':
    while True:
        pretty_print()
        time.sleep(1)
        

