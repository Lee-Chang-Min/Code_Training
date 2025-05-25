def winner(board, player) -> bool:
    #가로 확인
    for row in board:
        #print(row)
        for each in row:
            #print(each)
            if each != player:
                break
        else:
            return True
        
    #세로 확인
    for col in range(3):
        # 이 열의 0,1,2번째 행을 순서대로 확인
        for row_idx in range(3):
            if board[row_idx][col] != player:
                break
        else:
            return True
        
    #대각선 확인
    for idx in range(3):
        if board[idx][idx] != player:
            break
    else:
        return True
    
    for idx in range(3):
        if board[idx][2 - idx] != player:
            break
    else:
        return True
    
    ## 성공한게 없을때
    return False


def solution(board):
    
    countO = sum(row.count('O') for row in board)
    countX = sum(row.count('X') for row in board)
    
    #개수가 같거나 0 하나 더 많아야함
    if not (countO == countX or countO == countX+1):
        return 0
    
    O_wins = winner(board, 'O')
    X_wins = winner(board, 'X')
    
    #O가 이겼을때
    if O_wins and countO != countX + 1:
        return 0
    if X_wins and countO ==countX:
        return 0 
    return 1
