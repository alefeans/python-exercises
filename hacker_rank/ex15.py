import os
#import time

while True:
    filename = input("Digite o path/arquivo: ")
    try:
        txt = open(filename,'r')
        break
    except(IOError, ValueError):
        print("Só faz merda...")
print(txt.read())
txt.close()
