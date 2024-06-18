
import pyautogui as pg
import pydirectinput as pgd
import time
from PIL import Image

lol = pg.getWindowsWithTitle("League Of Legends")
ingame = False
lolWindow = 'League Of Legends'
pg.PAUSE = 0.05
pg.FAILSAFE = True

for window in lol:
    if window.title == "League of Legends":
        lol = window
        break
    else:
        print('window not found, current windows :', window)

lol.activate()

#centerW = lol.left + (lol.width/2)
#centerH = lol.top + (lol.height/2)
#pg.moveTo(centerW, centerH)

##button7location = pyautogui.locateOnScreen('calc7key.png', grayscale=True)
#pyautogui.screenshot(region=(0,0, 300, 400))

def Checklobby():
    if (pg.locateOnScreen('Imgs\lobby\LobbyDetect3.png', confidence=0.7, grayscale=True) != None):
        print('You are in the lobby')
        ingame = False
        
# Find Play Button
PlayButton = pg.locateOnWindow('Imgs\lobby\Play.png', lolWindow, confidence=0.7)
SelectTFT = pg.locateOnWindow('Imgs\lobby\TFTimg.png', lolWindow, confidence=0.7)
SelectTFTselected = pg.locateOnWindow('Imgs\lobby\TFTimg.png', lolWindow, confidence=0.7)
Confirm = pg.locateOnWindow('Imgs\lobby\Confirm.png', lolWindow, confidence=0.7)
FindMatch = pg.locateOnWindow('Imgs\lobby\FindMatch.png', lolWindow, confidence=0.7)
SearchingMatch = pg.locateOnWindow('Imgs\lobby\SearchingMatch.png', lolWindow, confidence=0.7)
MatchFound = pg.locateOnWindow('Imgs\lobby\MatchFound.png', lolWindow, confidence=0.7)
inQuene = pg.locateOnWindow('Imgs\lobby\SearchingMatch.png', lolWindow, confidence=0.7)
GroupButton = pg.locateOnWindow('Imgs\lobby\Group.png', lolWindow, confidence=0.7)

def startGame():
    LobbyStatus = 0
    while LobbyStatus < 5:
        
        while LobbyStatus == 0:
            pg.moveTo(PlayButton)
            pg.click()
            LobbyStatus += 1
            print(PlayButton, LobbyStatus)
            pg.sleep(0.5)
            
        while LobbyStatus == 1:
            pg.moveTo(SelectTFT)
            pg.click()
            print(SelectTFT, LobbyStatus)
            pg.sleep(0.5)
            if (pg.moveTo(SelectTFT) != None):
                LobbyStatus +=  1
            
        while LobbyStatus == 2:
            pg.moveTo(Confirm)
            pg.click()
            LobbyStatus += 1
            print(Confirm, LobbyStatus)
            pg.sleep(0.5)
        
Checklobby()         
startGame()