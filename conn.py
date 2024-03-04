from events import *
import os

os.system('cls')


def welcome(): 
    with open("writings\\VS.txt", "r", encoding="utf8") as wl_write:
        out = wl_write.read()
        print(Fore.LIGHTBLUE_EX + out)
        print(Fore.RESET)


