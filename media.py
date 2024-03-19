'''
Questo file è per gestire la sessione multimediale del server. 

In teoria dovrebbe controllare interamente le cartelle presenti nella cartella Cinema, specialmente la cartella "serie", poi sceglierne un file multimediale casuale e riprodurre i successivi.
'''

import os
from colorama import Fore

path = "D:\Cinema"

'''
questo le printa soltanto, non permette di maneggiare i dati che registra
'''

'''
def print_folder_tree(path, indent=''):
    print(indent + os.path.basename(path) + '/') 
    indent += '  '
    
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        if os.path.isdir(item_path):
            print_folder_tree(item_path, indent)
        else:
            print(indent + '  ' + item_name) 
    return item_path
file = print_folder_tree(path,indent='')
print(file)

def print_folder_tree(path, indent=''):
    print(indent + os.path.basename(path) + '/') 
    indent += '    ' 
    
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        if os.path.isdir(item_path):
            print_folder_tree(item_path, indent)

print_folder_tree(path)

'''

