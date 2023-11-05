board_size = 3 # количество  клеток

board = [1,2,3,4,5,6,7,8,9,] # игровое поле

def draw_board(): # выводим игровое поле
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('',board[i * 3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|')*3)
    pass
def game_step(index, char): # игровой ход
    if(index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False
    board[index-1] = char
    return True
def check_win(): # проверка победы
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # по горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # по вертикали
        (0, 4, 8), (2, 4, 6)             # по диагонали
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win
def start_game():
    current_player = 'X' # текущий игрок
    step = 1 # номер шага
    draw_board()

    while(step<10) and (check_win() == False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')

        if (index == 0):
            break

        if (game_step(int(index), current_player)): # если удалось сделать шаг
            print('Ход засчитан')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            step += 1 # увеличим номер хода
        else:
            print('Неверный ход! Повторите ход!')

    if (step == 10):
        print('Игра окончена! Ничья! Победила дружба!)')
    else:
        print('Выиграл игрок играющий за ' + check_win())

print('Добро пожаловать в игру Крестики и Нолики')
start_game()