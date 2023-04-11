# maldonga v1.0.0
# made by. notsngro_

from os.path import exists
import os
import sys

# log color
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

msgBoxMessage = ""
msgBoxTitle = ""
#msgBoxNormal = ctypes.windll.user32.MessageBoxW(0, msgBoxMessage, msgBoxTitle, 0)
#msgBoxWarning = ctypes.windll.user32.MessageBoxW(0, msgBoxMessage, msgBoxTitle, 0)
#msgBoxError = ctypes.windll.user32.MessageBoxW(0, msgBoxMessage, msgBoxTitle, 16)
DRIVE_PATH = 'C:/'
CURRENT_PATH = f'{os.path.abspath(os.getcwd())}'

# main
class Main:
    def chkfile():
        try:
            print("[INFO] Setting up...")

            mypc_link_exists = exists('./src/maldonga_bat/mypc_lk.bat')
            donga_link_exists = exists('./src/maldonga_bat/donga_mal_lk.bat')
            edge_link_exists = exists('./src/maldonga_bat/edge_lk.bat')
            ie_link_exists = exists('./src/maldonga_bat/ie_lk.bat')
            powerpoint_link_exists = exists('./src/maldonga_bat/powerpoint_lk.bat')

            print("[INFO] Checking files...")

            if mypc_link_exists == True:
                print(f'{bcolors.OKGREEN}[SUCCESS] MyPC Link file exists. {bcolors.ENDC}')
            else:
                print(f'{bcolors.FAIL}[ERROR] MyPC file does not exists.{bcolors.ENDC}')
                print(f"{bcolors.FAIL}[ERROR] Please check that src folder with './src/maldonga_bat/mypc_lk.bat' file exist.{bcolors.ENDC}")
                breakpoint
            if donga_link_exists == True:
                print(f'{bcolors.OKGREEN}[SUCCESS] Donga Link file exists. {bcolors.ENDC}')
            else:
                print(f'{bcolors.FAIL}[ERROR] Donga Link file does not exists.{bcolors.ENDC}')
                print(f"{bcolors.FAIL}[ERROR] Please check that src folder with './src/maldonga_bat/donga_mal_lk.bat' file exist.{bcolors.ENDC}")
                breakpoint
            if edge_link_exists == True:
                print(f'{bcolors.OKGREEN}[SUCCESS] Edge Link file exists. {bcolors.ENDC}')
            else:
                print(f'{bcolors.FAIL}[ERROR] Edge Link file does not exists.{bcolors.ENDC}')
                print(f"{bcolors.FAIL}[ERROR] Please check that src folder with './src/maldonga_bat/edge_lk.bat' file exist.{bcolors.ENDC}")
                breakpoint
            if ie_link_exists == True:
                print(f'{bcolors.OKGREEN}[SUCCESS] Internet Explorer Link file exists. {bcolors.ENDC}')
            else:
                print(f'{bcolors.FAIL}[ERROR] Interent Explorer Link file does not exists.{bcolors.ENDC}')
                print(f"{bcolors.FAIL}[ERROR] Please check that src folder with './src/maldonga_bat/ie_lk.bat' file exist.{bcolors.ENDC}")
                breakpoint
            if powerpoint_link_exists == True:
                print(f'{bcolors.OKGREEN}[SUCCESS] Powerpoint Link file exists. {bcolors.ENDC}')
            else:
                print(f'{bcolors.FAIL}[ERROR] Powerpoint Link file does not exists.{bcolors.ENDC}')
                print(f"{bcolors.FAIL}[ERROR] Please check that src folder with './src/maldonga_bat/powerpoint_lk.bat' file exist.{bcolors.ENDC}")
                breakpoint

        except:
            print("█▀▀ █▀█ █▀█ █▀█ █▀█   █▀█ █▀▀ █░█ █▀█ █▀█ █▀▀ █▀▄ █\n██▄ █▀▄ █▀▄ █▄█ █▀▄   █▄█ █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▀ ▄")
            print(f'{bcolors.FAIL}[ERROR] Please check that file exist on src folder. {bcolors.ENDC}')
            breakpoint

    def setupLink():
        DONGA_FILE_LOC = DRIVE_PATH + ''
        IE_FILE_LOC = DRIVE_PATH + ''
        MYPC_FILE_LOC = DRIVE_PATH + ''
        EDGE_FILE_LOC = DRIVE_PATH + ''
        POWERPOINT_FILE_LOC = DRIVE_PATH + ''

    def checkOSVersion():
        if (os.name == "Windows 10", os.name == "Windows 11"):
            print(f"{bcolors.FAIL}[ERROR] Current system is not Updated or, not Windows Operating System!\n[ERROR] This program is only works from Windows 10 up to the latest version.{bcolors.ENDC}")
            breakpoint
        else:
            return 0
        
    print("\n\n\n\n\n███╗░░░███╗░█████╗░██╗░░░░░██████╗░░█████╗░███╗░░██╗░██████╗░░█████╗░\n████╗░████║██╔══██╗██║░░░░░██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗\n██╔████╔██║███████║██║░░░░░██║░░██║██║░░██║██╔██╗██║██║░░██╗░███████║\n██║╚██╔╝██║██╔══██║██║░░░░░██║░░██║██║░░██║██║╚████║██║░░╚██╗██╔══██║\n██║░╚═╝░██║██║░░██║███████╗██████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║\n╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝")
    print("for Hyupsung Kyungbok Middle School Edition.\n")
    chkfile()
    checkOSVersion()
    setupLink()