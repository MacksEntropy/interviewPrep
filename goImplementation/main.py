from typing import List
import logging
from collections import deque

logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def isAlive(board : List[List[str]], visited : List[List[bool]], queue : deque, x0 : int, y0 : int) -> bool:

    # Mark initial position as true
    visited[x0][y0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    
    # Check surrounding cells 
    for dx, dy in directions:
        
        # Constrain x,y to the dimentions of the board
        x, y = max(min(x0 + dx, len(board)-1),0), max(min(y0 + dy,len(board[0])-1),0)
        logger.debug(f"Searching for null at ({x},{y}), which has value {board[x][y]}")

        # Check for alive condition which is a null cell
        if board[x][y] == '':
            logger.debug(f"Alive condition found at {x},{y}")
            return True
        
        # Next cell candidate only added if it hasnt been visited, is of the same value as the initial cell, 
        # and is not already a candidate.
        if not visited[x][y] and board[x][y] == board[x0][y0] and [x,y] not in queue:
            queue.append([x,y])
            logger.debug(queue)

    # Recusively search through board   
    while queue:
        xq, yq = queue.popleft()
        logger.info(f"Moving to {xq},{yq}")
        return isAlive(board,visited,queue,xq,yq)
        
    return False



if __name__ == "__main__":
    n = 5
    board = [
        ['','B','B','B',''],
        ['B','W','W','B',''],
        ['B','W','W','B',''],
        ['','B','B','B',''],
        ['','','','','B']
    ]
    visited = [[False]*n for i in range(n)]
    q = deque()
    print("Cell is alive? : ",isAlive(board,visited,q,1,1))
    

