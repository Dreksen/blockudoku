import copy

def is_board_complete(board, block):
    """Проверяет, завершена ли игра Блокудоку, т.е. можно ли поставить еще хотя бы один блок.

    Args:
        board: Двумерный массив с числами, представляющий игровое поле.

    Returns:
        True, если игра завершена, False в противном случае.
    """

    # # Проверка заполнения всех клеток
    # for row in board:
    #     for cell in row:
    #         if cell == 0:
    #             return False

    # Создание списка всех возможных блоков
    # blocks = generate_all_blocks()
    blocks = [block]
    # Перебор всех возможных блоков
    for block in blocks:
        # Получение всех возможных позиций для блока
        positions = get_all_positions(block, board)

        # Если есть хотя бы одна возможная позиция, игра не завершена
        if len(positions) > 0:
            return False

    # Если ни один блок нельзя поставить, игра завершена
    return True


def generate_all_blocks():
    """Генерирует список всех возможных блоков Блокудоку."""

    blocks = []

    # Все возможные размеры блоков
    sizes = [1, 2, 3]

    # Все возможные формы блоков
    shapes = [
        [(0, 0)],
        [(0, 0), (0, 1)],
        [(0, 0), (1, 0)],
        [(0, 0), (0, 1), (1, 0)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
    ]

    # Перебор всех возможных размеров и форм
    for size in sizes:
        for shape in shapes:
            # Создание блока
            block = []
            for i in range(size):
                for j in range(size):
                    if (i, j) in shape:
                        block.append(1)
                    else:
                        block.append(0)

            # Добавление блока в список
            blocks.append(block)

    return blocks


def get_all_positions(block, board):
    """Получает все возможные позиции для блока на игровом поле."""

    positions = []

    # Перебор всех клеток игрового поля
    for i in range(len(board)):
        for j in range(len(board)):
            # Проверка, можно ли поставить блок в текущую клетку
            if is_valid_position(block, board, i, j):
                # Добавление позиции в список
                positions.append((i, j))

    return positions


def is_valid_position(block, board, row, col):
    """Проверяет, можно ли поставить блок в заданную позицию игрового поля."""

    # Проверка выхода за пределы игрового поля
    # if row + len(block) > len(board) or col + len(block) > len(board):
    #     return False


    for x, y in block:
        if row + x >= 9 or col + y >= 9 or row + x < 0 or col + y < 0:
            return False
        if board[row + x][col + y] == 1:
            return False

    return True
