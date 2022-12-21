pieceVals = {'p':1, 'n':3, 'b':3, 'r':5,'q':9, 'k':0}

def printPointsFEN(fenString):
    pieces = fenString.split()[0]
    white = 0
    black = 0
    for piece in pieces:
        if(piece.isalpha()):
            if(piece.isupper()):
                white += pieceVals[piece.lower()]
            else: 
                black += pieceVals[piece]
    
    print("White:", white)
    print("Black:", black)
    if(black > white):
        print("Black up in points by", black-white)
    else:
        print("White up in points by", white-black)
    return (white, black)



if __name__ == "__main__":
    fenCLI = input("Give me a chess position... ")
    printPointsFEN(fenCLI)
