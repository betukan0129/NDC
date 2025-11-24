# Créé par beytu, le 15/10/2024 en Python 3.7
import pygame
import main2
from clsss2 import Jeu
p = main2.accuil(main2.importf,main2.coordim)
while True:
    if p == 1:
        while True:
            if main2.niv1(main2.importf,main2.coordim,Jeu,main2.defcolli,main2.collsioson) == 'reset':
                print('restarting...')
            else:
                break
        p = main2.accuil(main2.importf,main2.coordim)
    elif p == 2:
        while True:
            if main2.niv2(main2.importf,main2.coordim,Jeu) == 'reset':
                print('restarting...')
            else:
                break
        p = main2.accuil(main2.importf,main2.coordim)
    elif p== 3:
        while True:
            if main2.niv3(main2.importf,main2.coordim,Jeu,main2.defcolli,main2.collsioson) == 'reset':
                print('restarting...')
            else:
                break
        p = main2.accuil(main2.importf,main2.coordim)
    elif p == 4 :
        while True:
            if main2.niv4(main2.importf,main2.coordim,main2.collsioson,main2.defcolli,Jeu) == 'reset':
                print("restarting...")
            else:
                break
        p = main2.accuil(main2.importf,main2.coordim)






