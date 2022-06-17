def tictactoe(moves):
    ticT = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    
    isFilled = True
    
    for i in range(len(moves)):
        x,y  = moves[i] 
        if i % 2 == 0:
            ticT[x][y] = "X"
        else:
            ticT[x][y] = "O"
        
    
    if ticT[0][0] == ticT[1][1] == ticT[2][2]:
        if ticT[0][0] != " ":
            return "A" if ticT[0][0] == "X" else "B"
    
    if ticT[0][2] == ticT[1][1] == ticT[2][0]:
        if ticT[0][2] != " ":
            return "A" if ticT[0][2] == "X" else "B"
    
    for i in range(3):
        if ticT[i][0] == ticT[i][1] == ticT[i][2]:
            if ticT[i][0] != " ":
                return "A" if ticT[i][0] == "X" else "B"
    

        if ticT[0][i] == ticT[1][i] == ticT[2][i]:
            if ticT[0][i] != " ":
                return "A" if ticT[0][i] == "X" else "B"
    
    
    for i in ticT:
        if " " in i:
            isFilled = False
    # len(moves) == 9 --- at this point it a draw
    
    if not isFilled:
        return "Pending"
    else:
        return "Draw"



def main():
    moves  = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    print(tictactoe(moves))

    return 0


main()