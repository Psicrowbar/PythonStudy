# Tic tac toe game
# by Ratmir Saifutdinov


board = list(range(1, 10))


# Drawing field func
def draw_field(board):
    print("-" * 13)
    empty_field = []
    emptystring = ""
    for i, v in enumerate(board):
        if str(v).isdigit():
            empty_field.insert(i, "|-|")
        else:
            empty_field.insert(i, "|" + v + "|")
    for i in range(0, 9, 4):
        empty_field.insert(i, "\n")
    print(emptystring.join(empty_field))
    print("-" * 13)


# Take player input func
def player_input(sign):
    valid = False  # value for cheking if player inputed X or O else not valid sign inputted or no input yet
    while not valid:
        player_number = int(input("Выберите место  от 1 до 9 для " + sign + "! "))
        if 1 <= int(player_number) <= 9:  # number is valid
            if str(board[player_number - 1]) not in "XO":  # check if board space already has X or O
                board[player_number - 1] = sign
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


# wining condition
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


# mail func
def main(board):
    counter = 0  # value checks how many X or O on board
    win = False
    while not win:
        draw_field(board)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)  # cash current field
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_field(board)


main(board)

input("Нажмите Enter для выхода!")
