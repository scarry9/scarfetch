import platform
import socket
import psutil
import colorama
from colorama import Fore

colorama.init()

def get_system_info():
    system = platform.system()
    release = platform.release()
    architecture = platform.architecture()[0]
    hostname = socket.gethostname()
    cpu_cores = psutil.cpu_count(logical=False)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert to GB
    uptime = round((psutil.boot_time() - psutil.time.time()) / 3600, 2)  # Convert to hours

    # Get Linux distribution information
    if system.lower() == 'linux':
        distro_info = ' '.join(platform.uname()[-2:])
        linux_distro = distro_info.strip()
    else:
        linux_distro = "Not applicable"

    return {
        "System": system,
        "Release": release,
        "Architecture": architecture,
        "Hostname": hostname,
        "CPU Cores": cpu_cores,
        "Total Memory": f"{total_memory} GB",
        "Uptime": f"{uptime} hours",
        "Linux Distro": linux_distro,
    }

def print_system_info(info):
    for key, value in info.items():
        print(Fore.GREEN + f"{key}: {value}")

    print("""
    _nnnn_        
        dGGGGMMb       
       @p~qp~~qMb      
       M|@||@) M|      
       @,----.JM|      
      JS^\__/  qKL     
     dZP        qKRb   
    dZP          qKKb  
   fZP            SMMb 
   HZM            MMMM 
   FqM            MMMM 
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'  
     `-'       `--' hjm
""")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
