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
        "Distro": linux_distro,
        "DE": desktop_environment,  # Separate key for Desktop Environment
        "Host": hostname,
        "System": system,
        "Kernel": release,
        "Uptime": f"{uptime_hours} hours, {uptime_minutes} minutes",
        "RAM Usage": f"{used_memory}/{total_memory} GB",
    }

def print_system_info(info):
    for key, value in info.items():
        key_color = Fore.CYAN
        value_color = Fore.WHITE
        print(f"{Style.BRIGHT}{key_color}{key}: {Style.NORMAL}{value_color}{value}{Style.RESET_ALL}")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
