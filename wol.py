import subprocess
import sys
import time

IP = "192.168.1.62"
m = 5
print("█░█░█▀▀░█░░░█▀▀░█▀█░█▄█░█▀▀░░░▀█▀░█▀█░░░█░█░█▀█░█")
print("█▄█░█▀▀░█░░░█░░░█░█░█░█░█▀▀░░░░█░░█░█░░░█▄█░█░█░█")
print("▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░░▀░░▀▀▀░░░▀░▀░▀▀▀░▀▀▀")
print("Eseguo primo tentativo di accensione del VSB-Server")

def ping (IP):
    result = subprocess.run(["ping", IP], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return 0 if result.returncode == 0 else 1

if ping(IP) == 0:
    print("Il server non è attivo! Vuoi attivarlo? [Y/N]")
    risposta = input()
    if risposta.upper() == "Y":
        print("Attendo prima di verificare il ping")
        time.sleep(30)
        print("Eseguo il ping")
        for m in range(5):
            subprocess.run(["WakeMeOnLan.exe", "/wakeup", IP])
            subprocess.run(["ping","-n", "1", IP])
            m += 1
        if ping(IP) == 1:
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
    
elif ping(IP) == 1:
    print("Il server è già attivo! Desideri essere reindirizzato alla pagina? [Y/N]")
    risposta = input()
    if risposta == "Y":
        subprocess.run(["explorer", "https://192.168.1.62:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"])
    else: 
        print("Va bene! Wol si chiuderà tra pochi istanti")
        sys.exit()
else:
        print("Risposta non valida. Si prega di rispondere con 'Y' o 'N'.")


