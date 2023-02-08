"""
Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список
игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

from check_input import check_num_input

def main():
    n = input('Введите кол-во завершенных игр или "Q": ')
    if n == "Q":
        exit('Программа завершена пользователем!')
    n = check_num_input(n)
    n = int(n)
    team_table = dict()
    gm_count = 1

    while n > 0:
        game_input = input(f'Введите результат игры {gm_count}:')
        game_input = game_input.split(';')
        tm1, tm2 = game_input[0], game_input[2]
        tm1_sc, tm2_sc = int(game_input[1]), int(game_input[3])

        game_res_tm1 = [
            1,
            1 if tm1_sc > tm2_sc else 0,
            1 if tm1_sc == tm2_sc else 0,
            1 if tm1_sc < tm2_sc else 0,
            3 if tm1_sc > tm2_sc else(0 if tm1_sc < tm2_sc else 1),
        ]

        game_res_tm2 = [
            1,
            1 if tm1_sc < tm2_sc else 0,
            1 if tm1_sc == tm2_sc else 0,
            1 if tm1_sc > tm2_sc else 0,
            3 if tm1_sc < tm2_sc else(0 if tm1_sc > tm2_sc else 1),
        ]

        update_table(tm1, team_table, game_res_tm1)
        update_table(tm2, team_table, game_res_tm2)


        n -= 1
        gm_count += 1

    items = sorted([(sum(tup[1]), tup) for tup in tuple(team_table.items())], key=lambda i: i[0], reverse=True)
    spot = 1
    print()
    print('Результаты матчей:')
    print('__________________')
    print('{p}\t{a:12s}{b:2s}{c:2s}{d:2s}{e:2s}{f:2s}'.format(p = 'Мс.', a = 'Команда', b = 'И', c = 'В', d = 'Н', e = 'П', f = 'О'))
    for _ in items:
        res = _[1]
        print(f'{spot}. \t{res[0]:12s}', end='')
        print(' '.join(map(str, res[1])))
        spot += 1


def update_table(tm, table, game_res) -> dict:
    if tm not in table:
        table[tm] = game_res
    else:
        val = table.get(tm)
        for i in range(len(val)):
            val[i] += game_res[i]
    return table

main()

