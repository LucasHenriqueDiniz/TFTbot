
#RUN IN HIGH CONSTRAST MODE

import pyautogui as pg
import pydirectinput as pgd
import time
from PIL import Image

lol = pg.getWindowsWithTitle("League Of Legends")
lolWindow = 'League Of Legends'

for window in lol:
    if window.title == "League of Legends":
        lol = window
        break
    else:
        print('window not found, current windows :', window)

lol.activate()

#TFT = pg.locateOnWindow('ImgsHC\TFT.png', lolWindow, confidence=0.8, grayscale=True)
#Jogar = pg.locateOnWindow('ImgsHC\Jogar.png', lolWindow, confidence=0.8, grayscale=True)
#Confirmar = pg.locateOnWindow('ImgsHC\Confirmar.png', lolWindow, confidence=0.8, grayscale=True)
#EncontrarPartida = pg.locateOnWindow('ImgsHC\Encontrar Partida.png', lolWindow, confidence=0.8, grayscale=True)
#Grupo = pg.locateOnWindow('ImgsHC\Grupo.png', lolWindow, confidence=0.8, grayscale=True)
#NormalGameMode = pg.locateOnWindow('ImgsHC\Normal.png', lolWindow, confidence=0.8, grayscale=True)
#Aceitar = pg.locateOnWindow('ImgsHC\Aceitar.png', lolWindow, confidence=0.8, grayscale=True)

def Process(Item):
    
    print(Item)
    pg.moveTo(Item)
    pg.click()
    pg.sleep(0.5)
    
''' 
if (Process(pg.locateOnWindow('ImgsHC\Jogar.png', lolWindow, confidence=0.8, grayscale=True)) == None):
    Process(pg.locateOnWindow('ImgsHC\Grupo.png', lolWindow, confidence=0.8, grayscale=True))
    Process(pg.locateOnWindow('ImgsHC\Encontrar Partida.png', lolWindow, confidence=0.8, grayscale=True))
else:
    Process(pg.locateOnWindow('ImgsHC\TFT.png', lolWindow, confidence=0.8, grayscale=True))
    Process(pg.locateOnWindow('ImgsHC\Confirmar.png', lolWindow, confidence=0.8, grayscale=True))
    Process(pg.locateOnWindow('ImgsHC\Encontrar Partida.png', lolWindow, confidence=0.8, grayscale=True))
'''
 
 

Process(pg.locateOnWindow('ImgsHC\Jogar.png', lolWindow, confidence=0.8, grayscale=True))
Process(pg.locateOnWindow('ImgsHC\TFT.png', lolWindow, confidence=0.8, grayscale=True))
Process(pg.locateOnWindow('ImgsHC\Confirmar.png', lolWindow, confidence=0.8, grayscale=True))
pg.sleep(2.5)
Process(pg.locateOnWindow('ImgsHC\Encontrar Partida.png', lolWindow, confidence=0.8, grayscale=True))

while(pg.locateOnWindow('ImgsHC\Aceitar.png', lolWindow, confidence=0.8, grayscale=True) == None):
    if (pg.locateOnWindow('ImgsHC\Aceitar.png', lolWindow, confidence=0.8, grayscale=True) != None):
        pg.moveTo(pg.locateOnWindow('ImgsHC\Aceitar.png', lolWindow, confidence=0.8, grayscale=True))
        pg.click()
        break;
    else:
        print("Procurando partida....")
        pg.sleep(1)