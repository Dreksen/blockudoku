def is_valid_move(board, block, position):
    if not position:
        return False
    for x, y in block:
        if x + position[0] >= 9 or y + position[1] >= 9 or x + position[0] < 0 or y + position[1] < 0:
            print('нажатие за рамки')
            return False
        if board[x+position[0], y+position[1]] != 0:
            return False
    return True
