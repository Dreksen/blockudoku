def find_matching_rows_and_cols_and_blocks(board):
    # Массивы для совпадающих строк и столбцов
    matching_rows = []
    matching_cols = []
    matching_blocks = []
    # Проверка строк
    for i, row in enumerate(board):
        row_set = set(row)

        # Если множество содержит только один элемент, строка совпадает
        if len(row_set) == 1 and row_set.pop() == 1:
            matching_rows.append(i)

    # Проверка столбцов
    for j in range(len(board)):
        # Создание столбца
        column = [row[j] for row in board]

        # Преобразование столбца в множество
        column_set = set(column)

        # Если множество содержит только один элемент, столбец совпадает
        if len(column_set) == 1 and column_set.pop() == 1:
            matching_cols.append(j)

    #blocks cheking
    for i in range(3):
        for j in range(3):
            is_full = True
            for x in range(3):
                for y in range(3):
                    if board[i * 3 + x][j * 3 + y] == 0:
                        is_full = False
                        break
            if is_full:
                matching_blocks.append([i, j])
    return matching_rows, matching_cols, matching_blocks

def reset_matching_rows_and_cols_and_blocks(board, matching_rows, matching_cols, matching_blocks):
    # Обнуление совпадающих строк
    to_del = set()
    parts = 0
    for row in matching_rows:
        for i in range(len(board)):
            to_del.add((row, i))
        parts += 1

    # Обнуление совпадающих столбцов
    for col in matching_cols:
        for i in range(len(board)):
            to_del.add((i, col))
        parts += 1

    for i, j in matching_blocks:
        for x in range(3):
            for y in range(3):
                to_del.add((i * 3 + x, j * 3 + y))
        parts += 1
    for x, y in to_del:
        board[x][y] = 0
    # print('parts', parts)
    return len(to_del), parts


