########################################
# █▀█ █▀▀ █▀▄▀█ █▀█ █░█ █▀▀ █▀ █▄█ █▀  #
# █▀▄ ██▄ █░▀░█ █▄█ ▀▄▀ ██▄ ▄█ ░█░ ▄█  # 
########################################
#  v1.0 Normal System Removal Program  #
########################################

import os

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
    def selectYes():
        print(f"{bcolors.FAIL}[WARNING] Do you really wanna remove the system? *Really long Time!*{bcolors.ENDC}")
        select = input(f"{bcolors.OKCYAN}> (Y/N){bcolors.ENDC}")
        if(select == 'Y'):
            print("Removing System...")
            os.remove(f"C:\\Windows\\")
        elif(select == 'N'):
            print("GoodBye!")
            breakpoint
        elif(select == 'yes'):
            print("Removing System...")
            os.remove(f"C:\\Windows\\")
        elif(select == 'no'):
            print("GoodBye!")
            breakpoint
        elif(select == 'y'):
            print("Removing System...")
            os.remove(f"C:\\Windows\\")
        elif(select == 'n'):
            print("GoodBye!")
            breakpoint

    def selectNo():
        print("GoodBye!")
        breakpoint

    print("█▀█ █▀▀ █▀▄▀█ █▀█ █░█ █▀▀ █▀ █▄█ █▀\n█▀▄ ██▄ █░▀░█ █▄█ ▀▄▀ ██▄ ▄█ ░█░ ▄█")
    print("Remove system with only simple 2 steps!")
    print(f'{bcolors.WARNING}[WARNING] This program only works with Windows(tm) Operating System{bcolors.ENDC}')
    selectYesNno = input(f"{bcolors.WARNING}[WARNING] Remove System?{bcolors.ENDC}\n{bcolors.OKCYAN}> (Y/N){bcolors.ENDC}")

    if(selectYesNno == 'Y'):
        selectYes()
    elif(selectYesNno == 'N'):
        selectNo()
    elif(selectYesNno == 'yes'):
        selectYes()
    elif(selectYesNno == 'no'):
        selectNo()
    elif(selectYesNno == 'y'):
        selectYes()
    elif(selectYesNno == 'n'):
        selectNo()