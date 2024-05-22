def find_matching_rows_and_cols(board):
    """Находит совпадающие строки и столбцы в игровом поле Блокудоку.

    Args:
        board: Двумерный массив с числами, представляющий игровое поле.

    Returns:
        Два массива: один с совпадающими строками, другой с совпадающими столбцами.
    """

    # Массивы для совпадающих строк и столбцов
    matching_rows = []
    matching_cols = []

    # Проверка строк
    for i, row in enumerate(board):
        # Преобразование строки в множество
        row_set = set(row)

        # Если множество содержит только один элемент, строка совпадает
        if len(row_set) == 1:
            matching_rows.append(i)

    # Проверка столбцов
    for j in range(len(board)):
        # Создание столбца
        column = [row[j] for row in board]

        # Преобразование столбца в множество
        column_set = set(column)

        # Если множество содержит только один элемент, столбец совпадает
        if len(column_set) == 1:
            matching_cols.append(j)

    # Возврат массивов совпадающих строк и столбцов
    return matching_rows, matching_cols

def reset_matching_rows_and_cols(board, matching_rows, matching_cols):
    """Обнуляет совпадающие строки и столбцы в игровом поле Блокудоку.

    Args:
        board: Двумерный массив с числами, представляющий игровое поле.
        matching_rows: Массив с совпадающими строками.
        matching_cols: Массив с совпадающими столбцами.
    """

    # Обнуление совпадающих строк
    for row in matching_rows:
        for i in range(len(board)):
            board[row][i] = 0

    # Обнуление совпадающих столбцов
    for col in matching_cols:
        for i in range(len(board)):
            board[i][col] = 0
