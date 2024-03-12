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
    print("Scegliere tra le seguenti opzioni: \n 1) Accendere una VM \n 2) Accendere un container \n 3) MOdifica manuale")
    risposta = input()
    match risposta:
        case "1": 
            pass 
        case "2":
            pass
        case "3":
            print("Prova di connessione al " + Fore.LIGHTBLUE_EX + sw2 + Fore.RESET)
            os.system('putty\plink.exe -ssh 192.168.1.62 -l root -pw Tism0987 ')


def start():
    os.system('cls')
    welcome()
    connection()