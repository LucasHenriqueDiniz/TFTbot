    while LobbyStatus < 5: 
        
        while LobbyStatus == 0:
            print(PlayButton, LobbyStatus)
            pg.moveTo(PlayButton)
            pg.click()
            pg.sleep(0.2)
            if (PlayButton != None):
                print('passed', LobbyStatus)
                LobbyStatus =+ 1
                break;

            while LobbyStatus == 1: 
                print(SelectTFT, SelectTFTselected, LobbyStatus)
                pg.moveTo(SelectTFT)
                pg.click()
                pg.sleep(0.2)
                if ((SelectTFT != None) or (SelectTFTselected != None)):
                    print('passed', LobbyStatus)
                    LobbyStatus =+ 1
                    break;
                
            while LobbyStatus == 2:
                print('Confirm gamemode', LobbyStatus)
                pg.moveTo(Confirm)
                pg.click()
                pg.sleep(0.2)
                if (Confirm != None):
                    LobbyStatus =+ 1
                    break;
            if LobbyStatus == 3:
                print('Started searching for a match.', LobbyStatus)
                pg.moveTo(FindMatch)
                pg.click()
                pg.sleep(0.2)
                if (FindMatch != None):
                    LobbyStatus =+ 1
                        
        if LobbyStatus == 4:
            while(inQuene != None) or (MatchFound != None):
                if (MatchFound != None):
                    LobbyStatus =+ 1
                    break;
                else:
                    print("still searching for a match.....", LobbyStatus)
                    pg.sleep(.3)
                    
        if LobbyStatus == 5:
            print('Match Found!', LobbyStatus)
            pg.moveTo(MatchFound)
            pg.click()
            ingame = True
            pg.sleep(5)
            if (MatchFound != None):
                LobbyStatus =+ 1