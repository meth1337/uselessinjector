# libraries
from concurrent.futures import process  # for actual dll injection
from pymem import *  # for opening a process
from os import system  # for setting the title
from colorama import Fore  # for cli color modulation
from requests import get  # for checking the current version of the script
import sys  # for working with exceptions

# colors
green = Fore.GREEN
red = Fore.RED
rs = Fore.RESET

system("title https://discord.gg/U9JFM5RH8Y")  # :)

# version check, not working for some reason
'''current_version = "v1.0.0"
github_version = get("https://raw.githubusercontent.com/meth1337/uselessinjector/main/version").text
print(f"{current_version} {github_version}")
if current_version == github_version:
    pass
else:
    print("There is an update for this script! Download it from https://github.com/meth1337/uselessinjector/releases\n\nPress ENTER to exit.")
    input()
    exit()'''

# try/except blocks
try:
    process_name = input("Enter the process name: ")
    open_process = Pymem(process_name)
    print(green + "[1] Process found" + rs)
    dll_path = input("Enter the path to dll: ")
    dll_path_bytes = bytes(dll_path, "UTF-8")
    print(green + "[2] Injecting..." + rs)
    process.inject_dll(open_process.process_handle, dll_path_bytes)
    print(green + "[3] Injected!" + rs + " Have a great time!\n\nPress ENTER to exit.")
    input()
except KeyboardInterrupt:
    exit()
except:
    error_log = open("log.txt", "w")
    error_log.write(f"{sys.exc_info()}")
    print(red + "\nError! " + rs + "The error log has been automatically generated. Open the issue at https://github.com/meth1337/uselessinjector/issues and post the text from log.txt there.\n\nPress ENTER to exit.")
    input()
