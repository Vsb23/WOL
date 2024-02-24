import os 

IP = "192.168.1.62"


def ping(IP):
    risp = os.system('ping ' + IP)
    return 0 if risp == 0 else 1

ping(IP)