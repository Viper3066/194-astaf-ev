def is_word_fit(position, direction, word):
    board_size = 15

    row_char = position[0]
    col_str = position[1:]

    row = ord(row_char.upper()) - ord('A')
    col = int(col_str) - 1

    if row < 0 or row >= board_size or col < 0 or col >= board_size:
        return False

    if direction == 'horizontal':

        if col + len(word) > board_size:
            return False
    elif direction == 'vertical':

        if row + len(word) > board_size:
            return False
    else:

        raise ValueError("Direction must be 'horizontal' or 'vertical'")

    return True


print(is_word_fit('G7', 'horizontal', 'HELLO'))
print(is_word_fit('O14', 'horizontal', 'HELLO'))
print(is_word_fit('M15', 'vertical', 'WORLD'))
print(is_word_fit('A1', 'vertical', 'PYTHON'))

