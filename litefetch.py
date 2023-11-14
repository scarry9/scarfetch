import platform
import socket
import psutil
import colorama
from colorama import Fore, Style
import distro
from datetime import datetime
import os

colorama.init()

def get_system_info():
    system = platform.system()
    release = platform.release()
    architecture = platform.architecture()[0]
    hostname = socket.gethostname()
    cpu_cores = psutil.cpu_count(logical=False)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert to GB
    used_memory = round(psutil.virtual_memory().used / (1024 ** 3), 2)  # Convert to GB
    memory_percent = psutil.virtual_memory().percent
    boot_time = psutil.boot_time()
    current_time = datetime.now().timestamp()
    uptime_seconds = current_time - boot_time

    # Calculate hours and minutes for uptime
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)

    # Get Linux distribution information using distro library
    if system.lower() == 'linux':
        distro_id = distro.id()
        distro_version = distro.version()
        distro_name = distro.name()

        # Get Desktop Environment information
        desktop_environment = os.environ.get('XDG_CURRENT_DESKTOP', 'Unknown')
        linux_distro = f"{distro_name} Linux {architecture}"
    else:
        linux_distro = "Unable to detect"

    return {
        f"{Style.NORMAL}{Fore.GREEN}  __     __  |{Style.BRIGHT} Distro{Style.NORMAL}{Fore.CYAN}": linux_distro,                                      
        f"{Style.NORMAL}{Fore.GREEN}  \\ \\   / /  |{Style.BRIGHT} Host{Style.NORMAL}{Fore.CYAN}": hostname,                              
        f"{Style.NORMAL}{Fore.GREEN}   \\ \\ / /   |{Style.BRIGHT} DE{Style.NORMAL}{Fore.CYAN}": desktop_environment,
        f"{Style.NORMAL}{Fore.GREEN}    \\ v /    |{Style.BRIGHT} Kernel{Style.NORMAL}{Fore.CYAN}": release,
        f"{Style.NORMAL}{Fore.GREEN}     \\_/     |{Style.BRIGHT} Uptime{Style.NORMAL}{Fore.CYAN}": f"{uptime_hours} hours, {uptime_minutes} minutes",
        f"{Style.NORMAL}{Fore.GREEN}             |{Style.BRIGHT} RAM Usage{Style.NORMAL}{Fore.CYAN}": f"{used_memory}/{total_memory} GB",
        f"{Style.NORMAL}{Fore.GREEN}             |{Style.BRIGHT} CPU Cores{Style.NORMAL}{Fore.CYAN}": f"{psutil.cpu_count(logical=False)}"
    }
print(f"{Style.BRIGHT}{Fore.GREEN}-----------------------------------------------")

def print_system_info(info):
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)

print(f"{Style.BRIGHT}{Fore.GREEN}-----------------------------------------------")
