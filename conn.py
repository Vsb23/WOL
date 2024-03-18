from events import *
import os
from colorama import Fore

sw2 = "VSB-Server"

def welcome(): 
    with open("writings\\VS.txt", "r", encoding="utf8") as wl_write:
        out = wl_write.read()
        print(Fore.LIGHTBLUE_EX + out)
        print(Fore.RESET)

def connection(): 
    print("Scegliere tra le seguenti opzioni: \n 1) Accendere una VM \n 2) Accendere un container \n 3) Modifica manuale")
    risposta = input()
    match risposta:
        case "1": 
            os.system('putty\plink.exe -ssh root@192.168.1.62 -pw Tism0987 qm list \n')
            print("Inserire l'ID della VM che si desidera accendere")

            risposta = input()
            vm_id = os.system('\n putty\plink -ssh root@192.168.1.62 -pw Tism0987 qm start ' + risposta)

            print("Si è scelto di accendere la VM" + str(vm_id) + "\n Accensione in corso")
            os.system('putty\plink -ssh root@192.168.1.62 -pw Tism0987 qm start ' + risposta)


        case "2":
            os.system('putty\plink.exe -ssh root@192.168.1.62 -pw Tism0987 pct list \n')
            print("Inserire l'ID del container che si desidera accendere")

            risposta = input()
            vm_id = os.system('\n putty\plink -ssh root@192.168.1.62 -pw Tism0987 pct start ' + risposta)

            print(" Si è scelto di accendere il container" + str(vm_id) + "\n Accensione in corso")
            os.system('putty\plink -ssh root@192.168.1.62 -pw Tism0987 qm start ' + risposta)

        case "3":
            print("Prova di connessione al " + Fore.LIGHTBLUE_EX + sw2 + Fore.RESET)
            os.system('putty\plink.exe -ssh 192.168.1.62 -l root -pw Tism0987 ')


def start():
    os.system('cls')
    welcome()
    connection()