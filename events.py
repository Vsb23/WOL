import subprocess
import sys
import time
import os
from colorama import Fore
import conn

IP = "192.168.1.62"
sw = "Eseguo tentativo di connessione a " 
sw2 = "VSB-Server"
sw3 = "Il server è già "
sw3_5 = "attivo!" 
sw4 = "Scegliere l'opzione desiderata: \n 1) Reindirizzamento sulla pagina di controllo \n 2) Reindirizzamento su VSB-SERVER \n 3) Uscita \n"


def welcome(): 
    with open("writings\\WTW.txt", "r", encoding="utf8") as wl_write:
        out = wl_write.read()
        print(Fore.LIGHTGREEN_EX + out)
        print(Fore.RESET)


def ping(IP):
    m = 0
    while m < 3:
        m += 1
        sys.stdout.write(sw + Fore.LIGHTGREEN_EX + sw2 + "." * m + "\r" + Fore.RESET)
        risp = os.system('ping -n 1 ' + IP )
        time.sleep(2)
    if risp != 0:
        print("Il server non è attivo! Vuoi attivarlo? [Y/N]")
        risposta = input()
        if risposta.upper() == "Y":
            print("Attendo prima di verificare il ping")
            subprocess.run(["WakeMeOnLan.exe", "/wakeup", IP])
            time.sleep(30)
            print("Eseguo il ping")
            for m in range(5):
                subprocess.run(["WakeMeOnLan.exe", "/wakeup", IP])
                subprocess.run(["ping","-n", "1", IP])
                m += 1
            if ping(IP) == True:
                print("Il ping ha dato esito positivo!")
                print("Reindirizzamento verso la pagina di controllo")
                os.system('explorer "https://192.168.1.62:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"')
        elif risposta.upper() == "N":
            print("WOl si chiuderà tra pochi istanti")
    else:
        sys.stdout.write(sw3 + Fore.LIGHTGREEN_EX + sw3_5 + Fore.RESET + "\n" + sw4)
        risposta = input()
        match risposta:
            case "1":
                os.system('explorer "https://192.168.1.62:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"')
            case "2":
                conn.start()
            case "3":
                sys.exit()