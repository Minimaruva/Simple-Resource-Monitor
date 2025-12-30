import psutil
import time
from datetime import datetime
import sys


BYTES_TO_GB = 1024 ** 3
CPU_LOGICAL = psutil.cpu_count()
# Constants for pretty printing
WIDTH = 50
INNER_WIDTH = WIDTH - 2  # 48 spaces inside the borders

def clear_screen():
    print("\033[H\033[J", end="") 


def get_system_stats():
    """
    Fetch system metrics 
    Returns a dictionary
    """
    memory = psutil.virtual_memory()
    return {
        "cpu_percent": psutil.cpu_percent(),
        "mem_total_gb": round(memory.total / BYTES_TO_GB, 2),
        "mem_used_gb": round(memory.used / BYTES_TO_GB, 2),
        "mem_percent": memory.percent
    }


def print_stats(stats):
    clear_screen()

    # Header
    print('=' * WIDTH)
    print(f"={'Resource Monitor'.center(INNER_WIDTH)}=")
    print('=' * WIDTH)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"={'Time: ' + timestamp:^48}=") # ^48 centers values
    print('=' * WIDTH)

    cpu_txt = f" CPU Usage: {stats['cpu_percent']}%"
    cores_txt = f"Logical Cores: {CPU_LOGICAL}"
    # <23 for alignment
    print(f"={cpu_txt:^23}|| {cores_txt:^22}=")
    print(f"={'-' * INNER_WIDTH}=")

    mem_info = f" Memory: {stats['mem_used_gb']} GB / {stats['mem_total_gb']} GB ({stats['mem_percent']}%)"
    print(f"={mem_info:^48}=")
    print('=' * WIDTH + '\n')


if __name__ == '__main__':
    # First call is always 0.0 for initialization
    psutil.cpu_percent() 
    clear_screen()
    
    # History
    cpu_history = []
    mem_history = []
    start_time = datetime.now()

    try:
        while True:
            stats = get_system_stats()
            cpu_history.append(stats['cpu_percent'])
            mem_history.append(stats['mem_used_gb'])

            print_stats(stats)
            time.sleep(1)

    except KeyboardInterrupt:
        end_time = datetime.now()
        duration = end_time - start_time
        clear_screen()
        print("Monitoring Stopped")

        if cpu_history and mem_history:
            # Stats
            avg_cpu = sum(cpu_history) / len(cpu_history)
            max_cpu = max(cpu_history)
            avg_mem = sum(mem_history) / len(mem_history)
            max_mem = max(mem_history)

            print("\n" + "="*50)
            print(f"={'Session Summary'.center(48)}=")
            print("="*50)
            
            duration_txt = f"Duration: {str(duration).split('.')[0]}"
            print(f"={duration_txt:^48}=")
            print(f"={'-'*48}=")
            avg_cpu_txt = f" Avg CPU: {avg_cpu:.1f}%"
            max_cpu_txt = f" Max CPU: {max_cpu:.1f}%"
            print(f"={avg_cpu_txt:^23}||{max_cpu_txt:^23}=")

            avg_mem_txt = f" Avg Mem: {avg_mem:.2f} GB"
            max_mem_txt = f" Max Mem: {max_mem:.2f} GB"
            print(f"={avg_mem_txt:^23}||{max_mem_txt:^23}=")
            
            print("="*50 + "\n")

        sys.exit(0)
        