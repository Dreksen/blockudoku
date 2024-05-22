def check_for_disappeared(board):
    for row in range(9):
        if all(board[row, :]):
            return True
    for col in range(9):
        if all(board[:, col]):
            return True
    return False