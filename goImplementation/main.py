from typing import List

def isAlive(board : List[List[str]], visited : List[List[bool]], x0 : int, y0 : int) -> bool:

    # Mark initial position as true
    visited[x0][y0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Check surrounding cells
    for dx, dy in directions:
        
        # Constrain x,y to the dimentions of the board
        x, y = max(min(x0 + dx, len(board)-1),0), max(min(y0 + dy,len(board[0])-1),0)

        #If a null cell is encountered, then automatically alive 
        if board[x][y] == '':
            return True

        # Recusively search through board
        if not visited[x][y] and board[x0][y0] == board[x][y]:
            return isAlive(board,visited,x,y)
           
    return False



if __name__ == "__main__":
    n = 5
    # board = [['']*n for i in range(n)]
    board = [
        ['','W','W','W',''],
        ['W','B','B','W',''],
        ['','B','B','W',''],
        ['','W','W','W',''],
        ['','','','','']
    ]
    visited = [[False]*n for i in range(n)]
    print("Cell is alive? : ",isAlive(board,visited,1,1))
    

