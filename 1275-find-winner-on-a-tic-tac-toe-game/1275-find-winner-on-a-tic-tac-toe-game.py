class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        game = [[None , None , None], [None , None , None] , [None , None , None]]
        gameEmptyCells = [3 , 3 , 3]
        gameColumnEmptyCells = [3 , 3, 3]
        #gameDiagonalEmptyCells = [3 , 3, 3]
        gameDiagonalCellsCovered = 0
        
        currentPlayer = "A"
        for move in moves:
            pos1 , pos2 = move
            game[pos1][pos2] = currentPlayer
            
            if gameEmptyCells[pos1] > 0:
                gameEmptyCells[pos1] = gameEmptyCells[pos1] - 1
            
            if gameColumnEmptyCells[pos2] > 0:
                gameColumnEmptyCells[pos2] = gameColumnEmptyCells[pos2] - 1
                
            if pos1 == pos2:
                gameDiagonalCellsCovered = gameDiagonalCellsCovered + 1
                
            if currentPlayer == "A":
                currentPlayer = "B"
            else:
                currentPlayer = "A"
        
        print(game)
        print(gameEmptyCells)
        print(gameColumnEmptyCells)
        
        for position , row in enumerate(game):
            if gameEmptyCells[position] == 0:
                prevPlayer = None
                count = 0
                for idp , player in enumerate(row):
                    if idp == 0:
                        prevPlayer = player
                        count = count + 1
                    else:
                        if prevPlayer != player:
                            break
                        else:
                            count = count + 1
                if count == 3:
                    return prevPlayer
        
        for column in range(0 , 3):
            if gameColumnEmptyCells[column] == 0:
                prevPlayer = None
                count = 0
                for row in range( 0 , 3):
                    if row == 0:
                        prevPlayer = game[row][column]
                        count = count + 1
                    else:
                        player = game[row][column]
                        if prevPlayer == player:
                            count = count + 1
                        else:
                            break
                
                if count == 3:
                    return prevPlayer
        
        print("gameDiagonalCellsCovered = "  , gameDiagonalCellsCovered)
        if True:
            prevPlayer = game[0][0]
            if prevPlayer != None:
                count = 1
                for row in range(1 , 3):
                    if row == 0:
                        prevPlayer = game[row][row]
                        count = count + 1
                    else:
                        player = game[row][row]
                        if prevPlayer == player:
                            count = count + 1
                        else:
                            break
                if count == 3:
                    return prevPlayer
            
            prevPlayer = game[2][0]
            if prevPlayer != None:
                count = 1
                rowCount = 1
                columnCount = 1

                while rowCount >= 0 and columnCount <= 2:
                    player = game[rowCount][columnCount]
                    if player == prevPlayer:
                        count = count + 1
                    else:
                        break
                    rowCount = rowCount - 1
                    columnCount = columnCount + 1
                if count == 3:
                    return prevPlayer
        
        
        numberofmoves = len(moves)
        if numberofmoves == 9:
            return "Draw"
        elif numberofmoves < 9:
            return  "Pending"
        else:
            return None
                
                    
                 
                
        
                        
            
            
        