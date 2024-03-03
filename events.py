import subprocess
import sys
import time
import os
from colorama import Fore

IP = "192.168.1.62"


def welcome(): 
    with open("writings\\WTW.txt", "r", encoding="utf8") as wl_write:
        out = wl_write.read()
        print(Fore.LIGHTGREEN_EX + out)
        print(Fore.RESET)


def ping(IP):
    m = 0
    while m < 3:
        m += 1
        sw = "Eseguo tentativo di connessione a VSB-Server"
        sys.stdout.write(sw + "." * m + "\r")
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
        print("Il server è già attivo! Desideri essere reindirizzato alla pagina? [Y/N]")
        risposta = input()
        if risposta == "Y":
            os.system('explorer "https://192.168.1.62:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"')
        else: 
            print("Va bene! Wol si chiuderà tra pochi istanti")
            sys.exit()



os.system('cls')
welcome()
ping(IP)

''' 
    
elif ping(IP) == False:
    
else:
        print("Risposta non valida. Si prega di rispondere con 'Y' o 'N'.")

'''
