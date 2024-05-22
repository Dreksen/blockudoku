def place_block(board, block, position):
    for x, y in block:
        board[x+position[0], y+position[1]] = 1