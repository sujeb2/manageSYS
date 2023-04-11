########################################
# █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀ █▄█ █▀ #
# █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ ▄█ ░█░ ▄█ #
########################################

import sys, os
from pathlib import Path
from pick import pick
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Main:
    print("Please wait...")
    STARTUP_LOCATION = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
    maldonga = f'./maldonga.py'
    removesys = f'./removeSys.py'
    try:
        startup_loc_exist = Path(STARTUP_LOCATION)
        maldonga_exist = Path(maldonga)
        removesys_exist = Path(removesys)

        if startup_loc_exist.is_dir():
            print(f"{bcolors.OKGREEN}[OK] '{STARTUP_LOCATION}' exists.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}[ERROR] {STARTUP_LOCATION} folder does not exists.")
            print(f'[ERROR] Please check Windows is correctly installed.{bcolors.ENDC}')
            breakpoint
        if maldonga_exist.is_file():
            print(f"{bcolors.OKGREEN}[OK] '{maldonga}' exists.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}[ERROR] {maldonga} file does not exists.")
            print(f'[ERROR] Please check Windows is correctly installed.{bcolors.ENDC}')
            breakpoint
        if removesys_exist.is_file():
            print(f"{bcolors.OKGREEN}[OK] '{removesys}' exists.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}[ERROR] {removesys} file does not exists.")
            print(f'[ERROR] Please check Windows is correctly installed.{bcolors.ENDC}')
            breakpoint

        title = "█▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀ █▄█ █▀\n█░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ ▄█ ░█░ ▄█\nSimple way to manage your system.\nPlease select an option below: "
        options = ['Run MALDONGA','Run removeSys','Add specific file to startup','Exit program.']
        option, index = pick(options, title)
        
        if index == 0:
            print(f"{bcolors.OKCYAN}[INFO] Please wait...{bcolors.ENDC}")
            os.startfile(f'{exec(open(maldonga))}')
        if index == 1:
            print(f"{bcolors.OKCYAN}[INFO] Please wait...{bcolors.ENDC}")
            os.startfile(f'{exec(open(removesys))}')
        if index == 2:
            print(f"[INFO] Please write down program path below:")
            value = input('>')

            ORIGINAL_FILE = value
            print("Copying...")
            try:
                shutil.copyfile(ORIGINAL_FILE, STARTUP_LOCATION)
            except:
                print(f"{bcolors.FAIL}[ERROR] An error occurred while trying to copy file '{ORIGINAL_FILE}' to '{STARTUP_LOCATION}'")
                print(f"[ERROR] Please check that file exists or, wrong path.{bcolors.ENDC}")
                breakpoint
        if index == 3:
            print("Goodbye!")
            breakpoint
    except:
        print(f"{bcolors.FAIL}[ERROR] An unknown error occurred while trying to run '{option}'")
        print("[ERROR] Please check that file exists or, Pathlib and pick library are installed.")
        print(f"[ERROR] If this error occurrs even after redownload script, please send error message to 'sdbb2q@gmail.com'{bcolors.ENDC}")
        breakpoint