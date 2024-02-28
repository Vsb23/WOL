import subprocess
import sys
import time
import os


IP = "192.168.1.62"
m = 0
link_quoted = '"' + "https://192.168.1.62:8006/#v1:0:=node%2Fvsbserver:4:2::::7::" + '"'

def welcome(): 
    with open("WTW.txt", "r", encoding="utf8") as wl_write:
        out = wl_write.read()
        print(out)
def ping(IP):
    sw = "Eseguo tentativo di connessione a VSB-Server"
    for m in range(3):
        print(sw + "." * m)
        risp = os.system('ping -n 1 ' + IP )
        m += 1
    return True if risp == 0 else False


os.system('cls')
welcome()
ping(IP)

if ping(IP) == False:
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
            print("Il ping ha dato esito positivo! Vuoi essere reindirizzato alla pagina di controllo?")
            risposta = input()
            if risposta == "Y":
                while m < 5:
                    print("Reindirizzamento in corso" + "." * m)
                    m += 1
            else:
                print("Va bene! WOL si chiuderà tra pochi istanti")
                time.sleep(1)
                sys.exit()
        sys.exit()
    elif risposta.upper() == "N":
        print("WOl si chiuderà tra pochi istanti")
    
elif ping(IP) == True:
    print("Il server è già attivo! Desideri essere reindirizzato alla pagina? [Y/N]")
    risposta = input()
    if risposta == "Y":
        os.system('explorer "https://192.168.1.62:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"')
    else: 
        print("Va bene! Wol si chiuderà tra pochi istanti")
        sys.exit()
else:
        print("Risposta non valida. Si prega di rispondere con 'Y' o 'N'.")


